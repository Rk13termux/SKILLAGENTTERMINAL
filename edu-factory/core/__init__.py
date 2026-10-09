"""Núcleo de edu-factory: modelo de datos y parser del plan maestro."""

from core.parser import (
    CurriculumError,
    Lesson,
    MasterLesson,
    Module,
    parse_master_lesson,
    parse_texto,
    slugify,
)

__all__ = [
    "CurriculumError",
    "Lesson",
    "MasterLesson",
    "Module",
    "parse_master_lesson",
    "parse_texto",
    "slugify",
]
