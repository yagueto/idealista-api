# Idealista API Client

Este repositorio contiene un wrapper para la API de Idealista, que permite realizar consultas sobre propiedades en venta o alquiler.
Los datos son extraídos de la API oficial de idealista (https://developers.idealista.com/).

## Requisitos

- Cuenta de desarrollador en Idealista (se puede obtener acceso a la API en https://developers.idealista.com/)
- Python 3.7 o superior
- Paquetes listados en `requirements.txt`

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/yagueto/idealista-api.git
    cd idealista-api
    ```

2. Crea un entorno virtual y activa el entorno:
    ```sh
    python -m venv env
    source env/bin/activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

Para hacer consultas, es necesario tener un archivo `config.ini` en el que guardar la clave de la API y el secreto (proporcionados por Idealista al obtener acceso)

```ini
[AUTH]
api_key = tu_api_key
secret = tu_secret
```

## Uso

Los parámetros de las queries son los especificados en la documentación de la API, pasados como diccionario de clave-valor.

### Ejemplo de uso

```python
from pprint import pprint
from idealista_client import Idealista

idealista = Idealista("config.ini")

request = {
    "locationId": "0-EU-ES-01",
    "propertyType": "storageRooms",
    "operation": "sale",
    "maxItems": 50
}

resultado = idealista.query(request)
pprint(resultado)
```

## Contribuciones

¡Las contribuciones son bienvenidas! Para cualquier duda o sugerencia, abre un issue / pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
