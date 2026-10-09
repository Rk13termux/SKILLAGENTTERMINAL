"""Agente de redes sociales: adapta el plan maestro a guiones por plataforma.

Genera tres formatos por lección:
- video_short.md  (TikTok / Reels / Shorts, 60 s)
- video_long.md   (Facebook / YouTube, 3-8 min)
- post_static.md  (Instagram / LinkedIn, post estático)
"""

from __future__ import annotations

from pathlib import Path

from agents import BaseAgent, formato_lista
from core.parser import Lesson, MasterLesson, Module, parse_master_lesson, slugify

_MAX_HASHTAGS = 14
_MIN_HASHTAGS = 10


class SocialAgent(BaseAgent):
    nombre = "social"
    descripcion = "Guiones de video y post estático adaptados por plataforma"

    def generar(self, plan: MasterLesson, salida: Path) -> list[Path]:
        base = salida / "social"
        archivos: list[Path] = []
        entradas: list[tuple[Module, Lesson, Path]] = []

        for modulo in plan.modulos:
            for leccion in modulo.lecciones:
                carpeta = (
                    base
                    / f"modulo-{modulo.numero}-{slugify(modulo.titulo)}"
                    / f"leccion-{leccion.numero}-{slugify(leccion.titulo)}"
                )
                contexto = self._contexto(plan, modulo, leccion)
                for plantilla, nombre in (
                    ("video_short.md.tmpl", "video_short.md"),
                    ("video_long.md.tmpl", "video_long.md"),
                    ("post_static.md.tmpl", "post_static.md"),
                ):
                    contenido = self._render(plantilla, **contexto)
                    archivos.append(self._escribir(carpeta / nombre, contenido))
                entradas.append((modulo, leccion, carpeta))

        indice = self._indice(plan, entradas, base)
        archivos.append(self._escribir(base / "indice.md", indice))
        return archivos

    def _contexto(
        self, plan: MasterLesson, modulo: Module, leccion: Lesson
    ) -> dict[str, str]:
        meta = plan.metadata
        primer_tema = leccion.temas[0] if leccion.temas else leccion.titulo
        primer_ejercicio = (
            leccion.ejercicios[0] if leccion.ejercicios else "repasar los temas vistos"
        )
        return {
            "titulo_plan": plan.titulo,
            "id_plan": meta.get("id", "sin-id"),
            "nivel": meta.get("nivel", "sin nivel"),
            "duracion": meta.get("duracion", "sin duración"),
            "audiencia": meta.get("audiencia", "audiencia general"),
            "modulo_numero": str(modulo.numero),
            "modulo_titulo": modulo.titulo,
            "leccion_numero": str(leccion.numero),
            "leccion_titulo": leccion.titulo,
            "resumen": leccion.resumen,
            "temas": formato_lista(leccion.temas),
            "ejercicios": formato_lista(leccion.ejercicios),
            "comandos": self._bloque_comandos(leccion),
            "gancho_texto": self._gancho_texto(leccion, primer_tema),
            "gancho_visual": self._gancho_visual(leccion),
            "contexto_short": self._contexto_short(leccion, primer_tema),
            "demo_short": self._demo_short(leccion),
            "resultado_short": self._resultado_short(leccion, primer_tema),
            "cta_short": self._cta_short(plan, primer_ejercicio),
            "voz_en_off": self._voz_en_off(plan, modulo, leccion, primer_tema),
            "hashtags": self._hashtags(plan, leccion),
            "intro_gancho": self._intro_gancho(leccion, primer_tema),
            "intro_problema": self._intro_problema(plan, leccion, primer_tema),
            "conceptos": self._conceptos(plan, leccion),
            "demo_pasos": self._demo_pasos(leccion),
            "errores_comunes": self._errores_comunes(plan, leccion),
            "cta_curso": self._cta_curso(plan, modulo, leccion),
            "parrafo_hook": self._parrafo_hook(plan, leccion, primer_tema),
            "parrafo_valor": self._parrafo_valor(leccion, primer_ejercicio),
            "parrafo_cta": self._parrafo_cta(plan),
            "primer_comentario": self._primer_comentario(plan, leccion, primer_tema),
        }

    def _bloque_comandos(self, leccion: Lesson) -> str:
        if not leccion.comandos:
            return (
                "Sin comandos registrados en el plan para esta lección. "
                "Usa los temas como guion de la demo y anota los comandos "
                "reales en el master-lesson.md antes de grabar."
            )
        bloques = []
        for comando in leccion.comandos:
            bloques.append(f"```\n{comando}\n```")
        return "\n\n".join(bloques)

    def _gancho_texto(self, leccion: Lesson, primer_tema: str) -> str:
        return (
            f"«{primer_tema}» paso a paso, sin relleno "
            f"(lección {leccion.numero})."
        )

    def _gancho_visual(self, leccion: Lesson) -> str:
        if leccion.comandos:
            return (
                f"Plano de pantalla ejecutando el primer comando: "
                f"`{leccion.comandos[0]}`. Sin zoom lento: el resultado debe verse "
                "desde el primer segundo."
            )
        return (
            "Plano de pantalla con el título de la lección en texto claro y "
            "una demo breve del tema en marcha."
        )

    def _contexto_short(self, leccion: Lesson, primer_tema: str) -> str:
        return (
            f"Qué se resuelve: {primer_tema}. "
            f"{leccion.resumen} "
            "Plantea el problema en una frase y di que el comando o el proceso "
            "de la lección lo cierra."
        )

    def _demo_short(self, leccion: Lesson) -> str:
        if leccion.comandos:
            lineas = [
                f"{indice}. Ejecuta en pantalla `{comando}` y comenta en voz alta "
                "qué hace cada parte."
                for indice, comando in enumerate(leccion.comandos[:3], start=1)
            ]
            if len(leccion.comandos) > 3:
                lineas.append(
                    f"4. Menciona que hay {len(leccion.comandos)} comandos en total "
                    "y que el resto está en el material del curso."
                )
            return "\n".join(lineas)
        lineas = [
            f"{indice}. Muestra en pantalla: {tema}. Explica la idea en una frase "
            "mientras aparece el texto."
            for indice, tema in enumerate(leccion.temas[:3], start=1)
        ]
        return "\n".join(lineas)

    def _resultado_short(self, leccion: Lesson, primer_tema: str) -> str:
        return (
            f"Cierre en pantalla: resultado correcto de «{primer_tema}» visible. "
            f"Frase final: «esto es lo que hace falta para {primer_tema.lower()}; "
            "el resto es práctica»."
        )

    def _cta_short(self, plan: MasterLesson, primer_ejercicio: str) -> str:
        return (
            f"«Guarda este video y practica esto hoy: {primer_ejercicio} "
            f"Sígueme para el siguiente paso de {plan.titulo}»."
        )

    def _voz_en_off(
        self,
        plan: MasterLesson,
        modulo: Module,
        leccion: Lesson,
        primer_tema: str,
    ) -> str:
        partes = [
            f"Lección {leccion.numero} del módulo {modulo.numero} de {plan.titulo}.",
            leccion.resumen,
        ]
        if leccion.temas:
            partes.append(
                "Primero vemos " + ", ".join(leccion.temas[:-1] or leccion.temas)
                + (f" y después {leccion.temas[-1]}." if len(leccion.temas) > 1 else ".")
            )
        if leccion.comandos:
            partes.append(
                f"En pantalla ejecuto {len(leccion.comandos)} comandos, empezando por "
                f"`{leccion.comandos[0]}`. Observa qué cambia antes y después."
            )
        else:
            partes.append(
                f"En pantalla recorro el proceso de «{primer_tema}» paso a paso, "
                "sin saltos."
            )
        partes.append(
            "El resultado debe verse completo antes de cerrar; si algo falla, "
            "revisa el mensaje de error en lugar de repetir a ciegas."
        )
        if leccion.ejercicios:
            partes.append(f"Para practicar: {leccion.ejercicios[0]}")
        partes.append(
            f"En el material de {plan.titulo} encontrarás la lección completa "
            "con ejercicios y revisión."
        )
        texto = " ".join(partes)
        palabras = texto.split()
        if len(palabras) > 145:
            texto = " ".join(palabras[:145])
        return texto

    def _hashtags(self, plan: MasterLesson, leccion: Lesson) -> str:
        candidatos: list[str] = []

        def agregar(valor: str) -> None:
            etiqueta = slugify(valor).replace("-", "")
            if etiqueta and etiqueta not in candidatos:
                candidatos.append(etiqueta)

        for tema in leccion.temas:
            agregar(tema)
            for palabra in tema.split():
                if len(palabra.strip("«».,;:()")) >= 5:
                    agregar(palabra.strip("«».,;:()"))
        agregar(plan.titulo)
        agregar(leccion.titulo)
        for objetivo in plan.objetivos:
            for palabra in objetivo.split():
                limpia = palabra.strip("«».,;:()")
                if len(limpia) >= 6:
                    agregar(limpia)
        if len(candidatos) < _MIN_HASHTAGS:
            agregar(plan.metadata.get("audiencia", ""))
            agregar(plan.metadata.get("nivel", ""))
        seleccion = candidatos[:_MAX_HASHTAGS]
        return " ".join(f"#{etiqueta}" for etiqueta in seleccion)

    def _intro_gancho(self, leccion: Lesson, primer_tema: str) -> str:
        return (
            f"«{primer_tema}» es lo que separa un resultado reproducible de uno "
            f"que depende de la suerte. En esta lección ({leccion.titulo}) lo vemos "
            "completo, con el proceso en pantalla."
        )

    def _intro_problema(
        self, plan: MasterLesson, leccion: Lesson, primer_tema: str
    ) -> str:
        return (
            f"Problema real: {plan.metadata.get('audiencia', 'quienes trabajan en el tema')} "
            f"suelen bloquearse con {primer_tema} porque falta el orden de pasos. "
            f"{leccion.resumen} Hoy cerramos ese hueco en pocos minutos."
        )

    def _conceptos(self, plan: MasterLesson, leccion: Lesson) -> str:
        audiencia = plan.metadata.get("audiencia", "el público del curso")
        bloques = []
        for indice, tema in enumerate(leccion.temas[:3], start=1):
            bloques.append(
                f"### Concepto {indice}: {tema}\n\n"
                f"Explica «{tema}» en una frase, sin jerga innecesaria. "
                f"Conéctalo con un caso que {audiencia} reconozca al instante. "
                "Muestra un ejemplo mínimo en pantalla y cierra con una frase "
                "que enlace al siguiente concepto."
            )
        if len(leccion.temas) > 3:
            bloques.append(
                f"Tema extra (si el tiempo lo permite): {', '.join(leccion.temas[3:])}."
            )
        return "\n\n".join(bloques)

    def _demo_pasos(self, leccion: Lesson) -> str:
        if leccion.comandos:
            bloques = []
            for indice, comando in enumerate(leccion.comandos, start=1):
                bloques.append(
                    f"**Paso {indice}.** Ejecuta y muestra:\n\n```\n{comando}\n```"
                )
            bloques.append(
                "**Verificación.** Compara el resultado en pantalla con el esperado "
                "antes de avanzar."
            )
            return "\n\n".join(bloques)
        bloques = []
        for indice, tema in enumerate(leccion.temas, start=1):
            bloques.append(
                f"**Paso {indice}.** Demuestra «{tema}» en pantalla con un ejemplo "
                "concreto y comenta qué se observa."
            )
        return "\n\n".join(bloques)

    def _errores_comunes(self, plan: MasterLesson, leccion: Lesson) -> str:
        lineas = []
        if leccion.temas:
            lineas.append(
                f"- **Saltarse «{leccion.temas[0]}».** Sin ese punto, el resto del "
                "proceso falla de forma silenciosa. Verifícalo antes de continuar."
            )
        if leccion.comandos:
            lineas.append(
                "- **Copiar comandos sin leerlos.** Revisa cada opción antes de "
                "ejecutar: un parámetro mal puesto cambia el resultado."
            )
        lineas.append(
            f"- **Practicar una sola vez.** En un nivel "
            f"{plan.metadata.get('nivel', 'inicial')} el proceso se consolida "
            "repitiéndolo hasta que salga sin guion."
        )
        return "\n".join(lineas)

    def _cta_curso(
        self, plan: MasterLesson, modulo: Module, leccion: Lesson
    ) -> str:
        meta = plan.metadata
        return (
            f"«Esta lección es parte de {plan.titulo} ({meta.get('id', 'sin-id')}), "
            f"nivel {meta.get('nivel', '-')}, duración {meta.get('duracion', '-')}. "
            f"El módulo {modulo.numero} completo, con ejercicios y revisión, está en "
            "el curso. Enlace en el perfil»."
        )

    def _parrafo_hook(
        self, plan: MasterLesson, leccion: Lesson, primer_tema: str
    ) -> str:
        return (
            f"{primer_tema} es la parte que más se salta y la que más problemas "
            f"provoca después. En la lección {leccion.numero} de {plan.titulo} lo "
            "desarmamos en el orden correcto, con el proceso en pantalla."
        )

    def _parrafo_valor(self, leccion: Lesson, primer_ejercicio: str) -> str:
        puntos = "; ".join(leccion.temas) if leccion.temas else leccion.titulo
        return (
            f"En esta lección: {puntos}. {leccion.resumen} Al terminar te llevas un "
            f"ejercicio concreto para practicar: {primer_ejercicio}"
        )

    def _parrafo_cta(self, plan: MasterLesson) -> str:
        meta = plan.metadata
        return (
            f"Guarda esta publicación para practicarla con calma y compártela con "
            f"quien esté en el nivel {meta.get('nivel', '-')} de {plan.titulo}. "
            "El material completo del curso está en el perfil."
        )

    def _primer_comentario(
        self, plan: MasterLesson, leccion: Lesson, primer_tema: str
    ) -> str:
        return (
            f"Cuéntanos: ¿en qué parte de «{primer_tema}» te has atascado más hasta "
            "ahora? Describe el caso concreto y respondemos con el paso que falta."
        )

    def _indice(
        self,
        plan: MasterLesson,
        entradas: list[tuple[Module, Lesson, Path]],
        base: Path,
    ) -> str:
        lineas = [
            f"# Índice de guiones sociales — {plan.titulo}",
            "",
            f"Plan: {plan.metadata.get('id', 'sin-id')} · "
            f"Nivel: {plan.metadata.get('nivel', '-')} · "
            f"Audiencia: {plan.metadata.get('audiencia', '-')}",
            "",
            "Cada lección genera tres archivos: `video_short.md` (TikTok/Reels/Shorts), "
            "`video_long.md` (Facebook/YouTube) y `post_static.md` (Instagram/LinkedIn).",
            "",
        ]
        for modulo, leccion, carpeta in entradas:
            relativo = carpeta.relative_to(base)
            lineas.append(
                f"- Módulo {modulo.numero}.{leccion.numero} «{leccion.titulo}» → "
                f"`{relativo}/`"
            )
        lineas.append("")
        return "\n".join(lineas)


def generate_social_content(
    master_lesson_path: str | Path, output_dir: str | Path
) -> list[Path]:
    plan = parse_master_lesson(Path(master_lesson_path))
    return SocialAgent().ejecutar(plan, Path(output_dir))
