"""Agente de cursos: genera temario y unidades de curso por módulo."""

from __future__ import annotations

from pathlib import Path

from agents import BaseAgent, formato_lista
from core.parser import Lesson, MasterLesson, Module, slugify


class CourseAgent(BaseAgent):
    nombre = "course"
    descripcion = "Contenido de curso (temario y unidades por módulo)"

    def generar(self, plan: MasterLesson, salida: Path) -> list[Path]:
        base = salida / "cursos" / plan.slug
        archivos: list[Path] = []

        temario = self._temario(plan)
        archivos.append(self._escribir(base / "temario.md", temario))

        for modulo in plan.modulos:
            contenido = self._unidad(plan, modulo)
            nombre = f"modulo-{modulo.numero}-{slugify(modulo.titulo)}.md"
            archivos.append(self._escribir(base / nombre, contenido))

        return archivos

    def _temario(self, plan: MasterLesson) -> str:
        meta = plan.metadata
        lineas = [
            f"# Temario — {plan.titulo}",
            "",
            f"- **Identificador:** {meta.get('id', 'sin-id')}",
            f"- **Nivel:** {meta.get('nivel', '-')}",
            f"- **Duración:** {meta.get('duracion', '-')}",
            f"- **Audiencia:** {meta.get('audiencia', '-')}",
            "",
            "## Objetivos",
            "",
            formato_lista(plan.objetivos),
            "",
            "## Estructura",
            "",
        ]
        for modulo in plan.modulos:
            lineas.append(f"### Módulo {modulo.numero}: {modulo.titulo}")
            lineas.append("")
            for leccion in modulo.lecciones:
                lineas.append(
                    f"{leccion.numero}. {leccion.titulo} — {leccion.resumen}"
                )
            lineas.append("")
        return "\n".join(lineas)

    def _unidad(self, plan: MasterLesson, modulo: Module) -> str:
        lineas = [
            f"# Módulo {modulo.numero}: {modulo.titulo}",
            "",
            f"Curso: {plan.titulo} · Nivel: {plan.metadata.get('nivel', '-')}",
            "",
        ]
        for leccion in modulo.lecciones:
            lineas.append(self._seccion_leccion(plan, modulo, leccion).rstrip())
            lineas.append("")
        return "\n".join(lineas)

    def _seccion_leccion(
        self, plan: MasterLesson, modulo: Module, leccion: Lesson
    ) -> str:
        return self._render(
            "course_lesson.md.tmpl",
            titulo_plan=plan.titulo,
            modulo_numero=str(modulo.numero),
            modulo_titulo=modulo.titulo,
            leccion_numero=str(leccion.numero),
            leccion_titulo=leccion.titulo,
            resumen=leccion.resumen,
            temas=formato_lista(leccion.temas),
            ejercicios=formato_lista(leccion.ejercicios),
            recursos=formato_lista(leccion.recursos),
        )
