"""Agentes generadores de contenido y base común."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from string import Template
from typing import Sequence

from core.parser import MasterLesson, slugify

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent


class BaseAgent(ABC):
    nombre: str = "agente"
    descripcion: str = ""

    def __init__(self, plantillas_dir: Path | None = None) -> None:
        self.plantillas_dir = plantillas_dir or RAIZ_PROYECTO / "templates"

    def ejecutar(self, plan: MasterLesson, salida: Path) -> list[Path]:
        destino = Path(salida).resolve()
        destino.mkdir(parents=True, exist_ok=True)
        return self.generar(plan, destino)

    @abstractmethod
    def generar(self, plan: MasterLesson, salida: Path) -> list[Path]:
        ...

    def _plantilla(self, nombre: str) -> Template:
        ruta = self.plantillas_dir / nombre
        if not ruta.is_file():
            raise FileNotFoundError(f"No existe la plantilla: {ruta}")
        return Template(ruta.read_text(encoding="utf-8"))

    def _render(self, nombre: str, **contexto: str) -> str:
        return self._plantilla(nombre).safe_substitute(**contexto).rstrip() + "\n"

    def _escribir(self, ruta: Path, contenido: str) -> Path:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(contenido.rstrip() + "\n", encoding="utf-8")
        return ruta


def formato_lista(items: Sequence[str]) -> str:
    if not items:
        return "- (pendiente de completar)"
    return "\n".join(f"- {item}" for item in items)


__all__ = ["BaseAgent", "RAIZ_PROYECTO", "formato_lista", "slugify"]
