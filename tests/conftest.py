from pathlib import Path

import pytest

from utils.funciones_auxiliares import (
    iniciar_navegador,
    cerrar_navegador
)


@pytest.fixture
def driver():
    """Inicia el navegador para cada test y lo cierra al finalizar."""

    navegador = iniciar_navegador()

    yield navegador

    cerrar_navegador(navegador)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda una captura de pantalla cuando un test falla."""

    outcome = yield
    reporte = outcome.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver")

        if navegador:
            carpeta = Path("screenshots")
            carpeta.mkdir(exist_ok=True)

            nombre_archivo = carpeta / f"{item.name}.png"

            navegador.save_screenshot(str(nombre_archivo))