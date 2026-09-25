from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_SAUCEDEMO = "https://www.saucedemo.com/"


def iniciar_navegador():
    """Inicia Chrome y abre SauceDemo."""
    
    opciones = Options()
    opciones.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opciones)
    driver.get(URL_SAUCEDEMO)

    return driver

def iniciar_sesion(driver):
    """Ingresa las credenciales válidas y realiza el login."""

    wait = WebDriverWait(driver, 10)

    usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    usuario.send_keys("standard_user")

    contraseña = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    contraseña.send_keys("secret_sauce")

    boton_login = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    boton_login.click()

def obtener_primer_producto(driver):
    """Obtiene el nombre y precio del primer producto del catálogo."""

    wait = WebDriverWait(driver, 10)

    producto = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".inventory_item")
        )
    )

    nombre = producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio = producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    return nombre, precio

def agregar_primer_producto_al_carrito(driver):
    """Agrega el primer producto del catálogo al carrito."""

    wait = WebDriverWait(driver, 10)

    producto = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".inventory_item")
        )
    )

    boton_agregar = producto.find_element(
        By.CSS_SELECTOR, "button"
    )

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".inventory_item button")
        )
    )

    boton_agregar.click()

def cerrar_navegador(driver):
    """Cierra el navegador."""

    driver.quit()
