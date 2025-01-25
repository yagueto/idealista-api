import configparser
from datetime import datetime

import requests

import utils

time_format = "%Y-%m-%d %H:%M:%S"


class Idealista:
    """Idealista API client."""

    def __init__(self, config_file: str = None):
        """
        Inicializa el cliente de la API de Idealista.

        Args:
            config_file (str): Ruta al archivo de configuración.
        """
        if config_file is None:
            raise Exception("El archivo de configuración es obligatorio.")

        config = configparser.ConfigParser()
        config.read(config_file)

        if "AUTH" not in config:
            raise Exception("El archivo de configuración debe contener una sección 'AUTH' con API_KEY y SECRET")
        elif "API_KEY" not in config["AUTH"] or "SECRET" not in config["AUTH"]:
            raise Exception("El archivo de configuración debe contener una sección 'AUTH' con API_KEY y SECRET")

        elif "TOKEN" not in config or datetime.strptime(config["TOKEN"]["date"], time_format) < datetime.now():
            print("Token caducado o inexistente, solicitando nuevo.")

            self.token, self.expires = utils.get_bearer_token(**config["AUTH"])

            config["TOKEN"] = {}
            config["TOKEN"]["token"] = self.token
            config["TOKEN"]["date"] = self.expires.strftime(time_format)

            with open("config.ini", "w") as configfile:
                config.write(configfile)

        else:
            self.token = config["TOKEN"]["token"]

    def query(self, request: dict) -> dict:
        """
        Realiza una consulta a la API de Idealista.

        Args:
            request (dict): Datos de la solicitud. Los parámetros deben ser los especificados en la documentación de la API.

        Returns:
            dict: Respuesta de la API en formato JSON.
        """
        response = requests.post(
            "https://api.idealista.com/3.5/es/search",
            headers={
                "Authorization": f"Bearer {self.token}",
                "User-Agent": "curl/8.3.0"
            },
            data=request,
        )
        return response.json()
