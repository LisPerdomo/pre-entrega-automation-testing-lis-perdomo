import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.funciones_auxiliares import (
    iniciar_sesion,
    obtener_primer_producto,
    agregar_primer_producto_al_carrito
)


def test_login_exitoso(driver):

    iniciar_sesion(driver)
    logging.info("Login realizado correctamente")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url
    logging.info("Redirección a la página de inventario validada")

    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"
    assert "Swag Labs" in driver.title


def test_catalogo_productos(driver):

    iniciar_sesion(driver)
    logging.info("Login realizado correctamente")

    wait = WebDriverWait(driver, 10)

    # Verificar que estamos en la página de inventario
    wait.until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url

    # Verificar título de la página
    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    # Verificar que exista al menos un producto
    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    assert len(productos) > 0

    # Obtener nombre y precio del primer producto
    nombre, precio = obtener_primer_producto(driver)

    logging.info(
        f"Primer producto encontrado: {nombre} - {precio}"
    )

    print(f"\nPrimer producto: {nombre}")
    print(f"Precio: {precio}")

    assert nombre != ""
    assert precio != ""

    # Verificar elementos importantes de la interfaz
    menu = wait.until(
        EC.presence_of_element_located(
            (By.ID, "react-burger-menu-btn")
        )
    )

    filtro = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "product_sort_container")
        )
    )

    assert menu.is_displayed()
    assert filtro.is_displayed()


def test_agregar_producto_al_carrito(driver):

    iniciar_sesion(driver)
    logging.info("Login realizado correctamente")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("/inventory.html")
    )

    # Guardar el nombre del primer producto
    nombre_producto, _ = obtener_primer_producto(driver)

    # Agregar el primer producto al carrito
    agregar_primer_producto_al_carrito(driver)

    logging.info(
        f"Producto agregado al carrito: {nombre_producto}"
    )

    # Verificar que el contador del carrito sea 1
    contador_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador_carrito.text == "1"

    # Ir al carrito
    carrito = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    )

    carrito.click()

    # Verificar que estamos en el carrito
    wait.until(
        EC.url_contains("/cart.html")
    )

    assert "/cart.html" in driver.current_url

    # Verificar que el producto agregado aparezca
    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    nombre_carrito = producto_carrito.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    assert nombre_carrito == nombre_producto

    logging.info(
        "Producto verificado correctamente dentro del carrito"
    )