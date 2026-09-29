# Pre-Entrega Automatización QA - Lis Perdomo

Proyecto de automatización de pruebas funcionales para el sitio web SauceDemo, desarrollado como parte de la formación de Automatización QA de Talento Tech.

## Objetivo

Automatizar pruebas funcionales sobre SauceDemo utilizando Selenium WebDriver, Python y Pytest.

El proyecto verifica los principales flujos solicitados:

- Login exitoso.
- Acceso al catálogo de productos.
- Visualización de productos.
- Verificación de elementos importantes de la interfaz.
- Obtención del nombre y precio del primer producto.
- Agregado de un producto al carrito.
- Verificación del contador del carrito.
- Verificación del producto dentro del carrito.

## Tecnologías utilizadas

- Python 3.10
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Chrome / ChromeDriver
- Git
- GitHub

## Estructura del proyecto

```text
pre-entrega-automation-testing-lis-perdomo/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_saucedemo.py
│
├── utils/
│   ├── __init__.py
│   └── funciones_auxiliares.py
│
├── screenshots/
│
├── logs/
│
├── reports/
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## URL del repositorio

[Ver repositorio en GitHub](https://github.com/LisPerdomo/pre-entrega-automation-testing-lis-perdomo.git)

Para clonar el repositorio:

```bash
git clone https://github.com/LisPerdomo/pre-entrega-automation-testing-lis-perdomo.git
```