"""Lectura y validación del plan maestro de lecciones (master-lesson.md)."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

METADATOS_REQUERIDOS = ("id", "nivel", "duracion", "audiencia")
CAMPOS_LECCION = ("resumen", "temas", "ejercicios", "recursos", "comandos")
CAMPOS_LISTA = ("temas", "ejercicios", "recursos", "comandos")

_RE_H1 = re.compile(r"^#\s+(?P<titulo>\S.*)$")
_RE_H2 = re.compile(r"^##\s+(?P<titulo>\S.*)$")
_RE_H3 = re.compile(r"^###\s+(?P<titulo>\S.*)$")
_RE_CAMPO = re.compile(r"^\*\*(?P<campo>[^:*]+):\*\*\s*(?P<valor>\S.*)?$")
_RE_ITEM = re.compile(r"^[-*]\s+(?P<valor>\S.*)$")
_RE_METADATO = re.compile(r"^[-*]\s+(?P<clave>[^:]+):\s*(?P<valor>\S.*)$")
_RE_MODULO = re.compile(
    r"^M[oó]dulo\s*(?P<numero>\d+)?\s*[:.\-–]?\s*(?P<titulo>\S.*)$", re.IGNORECASE
)
_RE_LECCION = re.compile(
    r"^Lecci[oó]n\s*(?P<numero>\d+)?\s*[:.\-–]?\s*(?P<titulo>\S.*)$", re.IGNORECASE
)


class CurriculumError(ValueError):
    """Se lanza cuando el plan maestro no supera la validación."""


@dataclass(frozen=True)
class Lesson:
    numero: int
    titulo: str
    resumen: str
    temas: tuple[str, ...]
    ejercicios: tuple[str, ...]
    recursos: tuple[str, ...]
    comandos: tuple[str, ...] = ()


@dataclass(frozen=True)
class Module:
    numero: int
    titulo: str
    lecciones: tuple[Lesson, ...]


@dataclass(frozen=True)
class MasterLesson:
    titulo: str
    metadata: dict[str, str]
    objetivos: tuple[str, ...]
    modulos: tuple[Module, ...]

    @property
    def slug(self) -> str:
        base = self.metadata.get("id") or self.titulo
        return slugify(base)

    @property
    def total_lecciones(self) -> int:
        return sum(len(m.lecciones) for m in self.modulos)


def slugify(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    sin_acentos = "".join(c for c in normalizado if not unicodedata.combining(c))
    base = re.sub(r"[^a-zA-Z0-9]+", "-", sin_acentos).strip("-").lower()
    return base or "sin-titulo"


def parse_master_lesson(ruta: Path) -> MasterLesson:
    ruta = Path(ruta)
    if not ruta.is_file():
        raise CurriculumError(f"No se encuentra el plan de estudios: {ruta}")
    texto = ruta.read_text(encoding="utf-8")
    return parse_texto(texto, origen=str(ruta))


def parse_texto(texto: str, origen: str = "<texto>") -> MasterLesson:
    lineas = texto.splitlines()
    errores: list[str] = []
    titulo = ""
    metadata: dict[str, str] = {}
    objetivos: list[str] = []
    modulos: list[Module] = []

    contexto = "raiz"
    modulo_titulo = ""
    modulo_lecciones: list[Lesson] = []
    leccion_pendiente: dict | None = None
    campo_actual: str | None = None
    objetivos_pendientes: list[str] = []

    def cerrar_leccion() -> None:
        nonlocal leccion_pendiente, campo_actual
        if leccion_pendiente is None:
            return
        numero = len(modulo_lecciones) + 1
        datos = leccion_pendiente
        modulo_lecciones.append(
            Lesson(
                numero=numero,
                titulo=datos["titulo"],
                resumen=" ".join(datos["resumen"]).strip(),
                temas=tuple(datos["temas"]),
                ejercicios=tuple(datos["ejercicios"]),
                recursos=tuple(datos["recursos"]),
                comandos=tuple(datos["comandos"]),
            )
        )
        leccion_pendiente = None
        campo_actual = None

    def cerrar_modulo() -> None:
        nonlocal modulo_lecciones, modulo_titulo
        if not modulo_titulo:
            return
        numero = len(modulos) + 1
        modulos.append(
            Module(numero=numero, titulo=modulo_titulo, lecciones=tuple(modulo_lecciones))
        )
        modulo_lecciones = []
        modulo_titulo = ""

    def cerrar_seccion_metadata() -> None:
        nonlocal contexto
        if contexto == "metadata":
            contexto = "raiz"

    for numero_linea, linea in enumerate(lineas, start=1):
        crudo = linea.rstrip()
        linea_limpia = crudo.strip()
        if not linea_limpia:
            continue

        if _RE_H1.match(linea_limpia):
            match = _RE_H1.match(linea_limpia)
            if titulo:
                errores.append(f"L{numero_linea}: solo se admite un título H1")
                continue
            titulo = match.group("titulo").strip()
            continue

        if _RE_H2.match(linea_limpia):
            match = _RE_H2.match(linea_limpia)
            encabezado = match.group("titulo").strip()
            cerrar_leccion()
            cerrar_modulo()
            cerrar_seccion_metadata()
            if encabezado.lower() == "metadata":
                contexto = "metadata"
            elif encabezado.lower() == "objetivos":
                contexto = "objetivos"
            else:
                modulo_match = _RE_MODULO.match(encabezado)
                if modulo_match:
                    modulo_titulo = modulo_match.group("titulo").strip()
                else:
                    modulo_titulo = encabezado
                contexto = "modulo"
            continue

        if _RE_H3.match(linea_limpia):
            match = _RE_H3.match(linea_limpia)
            encabezado = match.group("titulo").strip()
            if contexto != "modulo":
                errores.append(
                    f"L{numero_linea}: la lección «{encabezado}» está fuera de un módulo"
                )
                continue
            cerrar_leccion()
            leccion_match = _RE_LECCION.match(encabezado)
            if leccion_match:
                leccion_titulo = leccion_match.group("titulo").strip()
            else:
                leccion_titulo = encabezado
            leccion_pendiente = {
                "titulo": leccion_titulo,
                "resumen": [],
                "temas": [],
                "ejercicios": [],
                "recursos": [],
                "comandos": [],
            }
            campo_actual = None
            continue

        campo_match = _RE_CAMPO.match(linea_limpia)
        if campo_match:
            campo = campo_match.group("campo").strip().lower()
            valor = (campo_match.group("valor") or "").strip()
            if campo not in CAMPOS_LECCION:
                errores.append(
                    f"L{numero_linea}: campo desconocido «{campo}» en lección "
                    f"(permitidos: {', '.join(CAMPOS_LECCION)})"
                )
                campo_actual = None
                continue
            if leccion_pendiente is None:
                errores.append(
                    f"L{numero_linea}: el campo «{campo}» aparece fuera de una lección"
                )
                continue
            campo_actual = campo
            if campo == "resumen" and valor:
                leccion_pendiente["resumen"].append(valor)
            continue

        item_match = _RE_ITEM.match(linea_limpia)
        if item_match:
            valor = item_match.group("valor").strip()
            if contexto == "metadata":
                meta_match = _RE_METADATO.match(linea_limpia)
                if meta_match:
                    clave = meta_match.group("clave").strip().lower()
                    metadata[clave] = meta_match.group("valor").strip()
                else:
                    errores.append(
                        f"L{numero_linea}: metadato inválido «{valor}» (usa «clave: valor»)"
                    )
                continue
            if contexto == "objetivos":
                objetivos.append(valor)
                continue
            if leccion_pendiente is not None and campo_actual in CAMPOS_LISTA:
                leccion_pendiente[campo_actual].append(valor)
                continue
            if leccion_pendiente is not None and campo_actual == "resumen":
                errores.append(
                    f"L{numero_linea}: lista inesperada dentro del resumen "
                    "(usa Temas, Ejercicios o Recursos)"
                )
                continue
            errores.append(f"L{numero_linea}: lista inesperada «{valor}»")
            continue

        if leccion_pendiente is not None and campo_actual == "resumen":
            leccion_pendiente["resumen"].append(linea_limpia)
            continue

        errores.append(f"L{numero_linea}: línea no reconocida «{linea_limpia}»")

    cerrar_leccion()
    cerrar_modulo()

    if not titulo:
        errores.append("Falta el título del plan (encabezado H1)")
    if not metadata:
        errores.append("Falta la sección «## Metadata»")
    else:
        for clave in METADATOS_REQUERIDOS:
            if clave not in metadata or not metadata[clave]:
                errores.append(f"Falta el metadato requerido «{clave}»")
    if not objetivos:
        errores.append("Falta la sección «## Objetivos» o está vacía")
    if not modulos:
        errores.append("El plan debe definir al menos un módulo («## Módulo …»)")
    for modulo in modulos:
        if not modulo.lecciones:
            errores.append(f"El módulo {modulo.numero} «{modulo.titulo}» no tiene lecciones")
        for leccion in modulo.lecciones:
            if not leccion.resumen:
                errores.append(
                    f"La lección {leccion.numero} «{leccion.titulo}» no tiene resumen"
                )
            if not leccion.temas:
                errores.append(
                    f"La lección {leccion.numero} «{leccion.titulo}» no tiene temas"
                )

    if errores:
        detalle = "\n".join(f"  - {e}" for e in errores)
        raise CurriculumError(
            f"Plan inválido ({origen}) con {len(errores)} error(es):\n{detalle}"
        )

    objetivos_pendientes = objetivos
    return MasterLesson(
        titulo=titulo,
        metadata=metadata,
        objetivos=tuple(objetivos_pendientes),
        modulos=tuple(modulos),
    )
