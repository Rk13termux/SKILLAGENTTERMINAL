#!/usr/bin/env python3
"""edu-factory: genera contenido educativo a partir de un plan maestro.

Uso:
    python3 edu_factory.py validate [plan]
    python3 edu_factory.py social   [plan] [-s SALIDA]
    python3 edu_factory.py course   [plan] [-s SALIDA]
    python3 edu_factory.py director [plan] [-s SALIDA]
    python3 edu_factory.py all      [plan] [-s SALIDA]
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from agents.course_agent import CourseAgent
from agents.director_agent import DirectorAgent
from agents.social_agent import SocialAgent
from core.parser import CurriculumError, MasterLesson, parse_master_lesson, slugify

RAIZ = Path(__file__).resolve().parent
PLAN_DEFECTO = RAIZ / "curriculum" / "master-lesson.md"
SALIDA_DEFECTO = RAIZ / "productions"

AGENTES = {
    "social": SocialAgent,
    "course": CourseAgent,
    "director": DirectorAgent,
}


def resumen_plan(plan: MasterLesson) -> str:
    lineas = [
        f"Plan: {plan.titulo}",
        f"  Identificador: {plan.metadata.get('id', 'sin-id')}",
        f"  Nivel: {plan.metadata.get('nivel', '-')}",
        f"  Duración: {plan.metadata.get('duracion', '-')}",
        f"  Audiencia: {plan.metadata.get('audiencia', '-')}",
        f"  Objetivos: {len(plan.objetivos)}",
        f"  Módulos: {len(plan.modulos)}",
        f"  Lecciones: {plan.total_lecciones}",
    ]
    for modulo in plan.modulos:
        lineas.append(f"    Módulo {modulo.numero}: {modulo.titulo}")
        for leccion in modulo.lecciones:
            lineas.append(f"      {modulo.numero}.{leccion.numero} {leccion.titulo}")
    return "\n".join(lineas)


def ejecutar_agentes(
    nombres: list[str], plan: MasterLesson, salida: Path, plantillas: Path | None
) -> int:
    errores = 0
    for nombre in nombres:
        agente = AGENTES[nombre](plantillas_dir=plantillas)
        print(f"[{agente.nombre}] {agente.descripcion} ...")
        try:
            archivos = agente.ejecutar(plan, salida)
        except Exception as exc:
            print(f"  Error en el agente «{nombre}»: {exc}", file=sys.stderr)
            errores += 1
            continue
        for ruta in archivos:
            print(f"  + {ruta}")
        print(f"  {len(archivos)} archivo(s) generados.")
    return errores


def ejecutar_tutorrec(
    plan: MasterLesson,
    salida: Path,
    leccion: str | None,
    modo: str,
    sin_pausas: bool,
    no_limpiar: bool,
    prompt: str | None = None,
    banner: bool = False,
    mostrar_descripcion: bool = False,
    backend: str = "ansi",
    output: str | None = None,
) -> int:
    plantilla = "tutorrec.py" if modo == "demo" else "tutorrec_real.py"
    base = salida / "direccion"
    disponibles: list[tuple[str, Path]] = []
    for modulo in plan.modulos:
        for leccion_obj in modulo.lecciones:
            if not leccion_obj.comandos:
                continue
            carpeta = (
                base
                / f"modulo-{modulo.numero}-{slugify(modulo.titulo)}"
                / f"leccion-{leccion_obj.numero}-{slugify(leccion_obj.titulo)}"
            )
            clave = f"{modulo.numero}.{leccion_obj.numero}"
            ruta = carpeta / plantilla
            disponibles.append((clave, ruta))

    if not disponibles:
        print("El plan no tiene lecciones con `**Comandos:**`. Nada que ejecutar.")
        return 1

    elegidas = disponibles
    if leccion:
        candidatas = {clave: ruta for clave, ruta in disponibles if clave == leccion}
        if not candidatas:
            print(
                f"No existe la lección «{leccion}» con comandos. "
                f"Disponibles: {', '.join(c for c, _ in disponibles)}",
                file=sys.stderr,
            )
            return 1
        elegidas = [(clave, ruta) for clave, ruta in disponibles if clave == leccion]
    else:
        print("Lecciones disponibles con comandos:")
        for clave, ruta in disponibles:
            print(f"  {clave} → {ruta.relative_to(salida)}")
        print("\nEjecuta una con: python3 edu_factory.py tutorrec <plan> -l <N.M> -m demo|real")
        return 0

    for clave, ruta in elegidas:
        if not ruta.is_file():
            print(
                f"Falta el script {ruta}.\n"
                "Regéralo primero con: python3 edu_factory.py director <plan> -s <salida>",
                file=sys.stderr,
            )
            return 1
        print(f"▶ Tutorial {clave} (modo {modo}): {ruta}", file=sys.stderr)
        env_naturales = "0" if sin_pausas else "1"
        cmd = [sys.executable, str(ruta)]
        entorno = dict(
            TUTORREC_PAUSAS=env_naturales,
            TUTORREC_NO_LIMPIAR="1" if no_limpiar else "0",
        )
        if prompt is not None:
            entorno["TUTORREC_PROMPT"] = prompt
        if banner:
            entorno["TUTORREC_BANNER"] = "1"
        if mostrar_descripcion:
            entorno["TUTORREC_DESCRIPCION"] = "1"
        if backend == "asciinema":
            entorno["TUTORREC_BACKEND"] = "asciinema"
            if output is None:
                entorno["TUTORREC_OUTPUT"] = str(ruta.parent / f"leccion-{clave}.cast")
        elif output is not None:
            entorno["TUTORREC_OUTPUT"] = output
        retorno = subprocess.call(cmd, env={**os.environ, **entorno})
        if retorno != 0:
            print(f"  El script devolvió {retorno}.", file=sys.stderr)
            return retorno
    return 0


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="edu_factory.py",
        description="Genera contenido educativo a partir de un plan maestro.",
    )
    parser.add_argument(
        "comando",
        choices=["validate", "social", "course", "director", "tutorrec", "all"],
        help="comando a ejecutar",
    )
    parser.add_argument(
        "plan",
        nargs="?",
        default=str(PLAN_DEFECTO),
        help=f"ruta al master-lesson.md (defecto: {PLAN_DEFECTO})",
    )
    parser.add_argument(
        "-s",
        "--salida",
        default=str(SALIDA_DEFECTO),
        help=f"carpeta de salida (defecto: {SALIDA_DEFECTO})",
    )
    parser.add_argument(
        "--plantillas",
        default=None,
        help="carpeta alternativa de plantillas",
    )
    parser.add_argument(
        "-l",
        "--leccion",
        default=None,
        help="lección a ejecutar en formato <módulo>.<lección> (ej: 1.1); "
        "sin esta opción, tutorrec lista las disponibles",
    )
    parser.add_argument(
        "-m",
        "--modo",
        choices=["demo", "real"],
        default="demo",
        help="modo de los tutorrec (demo simula output; real ejecuta)",
    )
    parser.add_argument(
        "--sin-pausas",
        action="store_true",
        help="desactivar las pausas naturales en la escritura",
    )
    parser.add_argument(
        "--no-limpiar",
        action="store_true",
        help="no limpiar la pantalla entre comandos",
    )
    parser.add_argument(
        "--prompt",
        default=None,
        help="prompt de la terminal (defecto: usuario@hostname:carpeta$)",
    )
    parser.add_argument(
        "--banner",
        action="store_true",
        help="mostrar la bienvenida de Termux al inicio (demo)",
    )
    parser.add_argument(
        "--mostrar-descripcion",
        action="store_true",
        help="mostrar la línea «▶ descripción» antes de cada comando",
    )
    parser.add_argument(
        "--backend",
        choices=["ansi", "asciinema"],
        default="ansi",
        help="ansi simula output en colores; asciinema graba la terminal real "
        "del usuario a un archivo .cast",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="archivo .cast de salida (solo backend asciinema); se guarda junto "
        "al script de la lección si no se indica",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    ruta_plan = Path(args.plan).expanduser().resolve()
    salida = Path(args.salida).expanduser().resolve()
    plantillas = Path(args.plantillas).expanduser().resolve() if args.plantillas else None

    try:
        plan = parse_master_lesson(ruta_plan)
    except CurriculumError as exc:
        print(f"Error de validación:\n{exc}", file=sys.stderr)
        return 1

    if args.comando == "validate":
        print("Plan válido.")
        print(resumen_plan(plan))
        return 0

    if args.comando == "tutorrec":
        return ejecutar_tutorrec(
            plan,
            salida,
            leccion=args.leccion,
            modo=args.modo,
            sin_pausas=args.sin_pausas,
            no_limpiar=args.no_limpiar,
            prompt=args.prompt,
            banner=args.banner,
            mostrar_descripcion=args.mostrar_descripcion,
            backend=args.backend,
            output=args.output,
        )

    print(resumen_plan(plan))
    print()

    nombres = list(AGENTES) if args.comando == "all" else [args.comando]
    errores = ejecutar_agentes(nombres, plan, salida, plantillas)
    if errores:
        print(f"\n{errores} agente(s) fallaron.", file=sys.stderr)
        return 2
    print(f"\nListo. Contenido en: {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
