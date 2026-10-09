"""Agente director: genera los scripts tutorrec cinematográficos.

Por cada lección con comandos genera dos ejecutables:
- `tutorrec.py` (modo demo): simula output realista sin ejecutar nada.
- `tutorrec_real.py` (modo real): escribe y ejecuta los comandos de verdad.

Ambos importan el motor `tutorrec.cinematic` localizando la raíz del
proyecto de forma relativa. Compatibles con Termux, Fedora y macOS.
"""

from __future__ import annotations

from pathlib import Path

from agents import BaseAgent
from core.parser import Lesson, MasterLesson, Module, parse_master_lesson, slugify

MODOS = {"demo": "tutorrec.py", "real": "tutorrec_real.py"}


class DirectorAgent(BaseAgent):
    nombre = "director"
    descripcion = "Scripts tutorrec cinematográficos (demo y real) para grabar pantalla"

    def generar(self, plan: MasterLesson, salida: Path) -> list[Path]:
        base = salida / "direccion"
        archivos: list[Path] = []
        entradas: list[tuple[Module, Lesson, Path, str]] = []
        omitidas: list[tuple[Module, Lesson]] = []

        for modulo in plan.modulos:
            for leccion in modulo.lecciones:
                if not leccion.comandos:
                    omitidas.append((modulo, leccion))
                    continue
                carpeta = (
                    base
                    / f"modulo-{modulo.numero}-{slugify(modulo.titulo)}"
                    / f"leccion-{leccion.numero}-{slugify(leccion.titulo)}"
                )
                contexto = {
                    "id_plan": plan.metadata.get("id", "sin-id"),
                    "titulo_plan": plan.titulo,
                    "titulo_modulo": modulo.titulo,
                    "titulo_leccion": leccion.titulo,
                    "total_comandos": str(len(leccion.comandos)),
                    "cuerpo": self._cuerpo_comandos(leccion),
                }
                for modo, plantilla in MODOS.items():
                    plantilla_archivo = f"{plantilla}.tmpl"
                    contenido = self._render(plantilla_archivo, **contexto)
                    ruta = self._escribir(carpeta / plantilla, contenido)
                    ruta.chmod(ruta.stat().st_mode | 0o111)
                    archivos.append(ruta)
                    entradas.append((modulo, leccion, ruta, modo))

        indice = self._indice(plan, entradas, omitidas, base)
        archivos.append(self._escribir(base / "indice.md", indice))
        return archivos

    def _cuerpo_comandos(self, leccion: Lesson) -> str:
        total = len(leccion.comandos)
        pasos = []
        for indice, comando in enumerate(leccion.comandos, start=1):
            descripcion = f"Paso {indice} de {total}: {leccion.titulo}"
            pasos.append(
                "    {\n"
                f"        'comando': {comando!r},\n"
                f"        'descripcion': {descripcion!r},\n"
                "    },"
            )
        return "\n".join(pasos)

    def _indice(
        self,
        plan: MasterLesson,
        entradas: list[tuple[Module, Lesson, Path, str]],
        omitidas: list[tuple[Module, Lesson]],
        base: Path,
    ) -> str:
        lineas = [
            f"# Índice de tutorrec — {plan.titulo}",
            "",
            "Cada lección genera un `tutorrec.py` (modo demo, simula el output) "
            "y un `tutorrec_real.py` (modo real, ejecuta los comandos). Ambos "
            "escriben los comandos con velocidad humana y limpian la pantalla "
            "entre pasos para grabar pantalla.",
            "",
        ]
        if not entradas:
            lineas.append(
                "No hay lecciones con `**Comandos:**` en este plan; no se genera "
                "ningún tutorrec."
            )
        else:
            for modulo, leccion, ruta, modo in entradas:
                relativo = ruta.relative_to(base)
                lineas.append(
                    f"- Módulo {modulo.numero}.{leccion.numero} «{leccion.titulo}» "
                    f"({len(leccion.comandos)} comandos) [{modo}] → `{relativo}`"
                )
        if omitidas:
            lineas.append("")
            lineas.append("Sin comandos en el plan (sin tutorrec):")
            for modulo, leccion in omitidas:
                lineas.append(
                    f"  - Módulo {modulo.numero}.{leccion.numero} «{leccion.titulo}»"
                )
        lineas.append("")
        return "\n".join(lineas)


def generate_director_content(
    master_lesson_path: str | Path, output_dir: str | Path
) -> list[Path]:
    plan = parse_master_lesson(Path(master_lesson_path))
    return DirectorAgent().ejecutar(plan, Path(output_dir))


def generate_tutorrec_cinematic(
    master_lesson_path: str | Path, output_dir: str | Path
) -> list[Path]:
    return generate_director_content(master_lesson_path, output_dir)