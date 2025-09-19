import requests
from .utils import get_bearer_token
from .models import Property


time_format = "%Y-%m-%d %H:%M:%S"


class Idealista:
    """Idealista API client."""

    session: requests.Session

    def __init__(self, api_key: str | None = None, api_secret: str | None = None, token: str | None = None):
        if token is not None:
            self.token = token
        elif api_key is not None and api_secret is not None:
            self.api_key = api_key
            self.api_secret = api_secret

            self.token = get_bearer_token(api_key=api_key, secret=api_secret)
        else:
            raise Exception(
                "No valid authentication method provided. Either a token or an API key and secret are required."
            )
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.token}",
                "User-Agent": "idealista_api_python/1.0",
            }
        )

    def query(self, request: dict) -> list[Property]:
        """
        Realiza una consulta a la API de Idealista.

        Args:
            request (dict): Datos de la solicitud. Los parámetros deben ser los especificados en la documentación de la API.

        Returns:
            list[Property]: Lista de propiedades devueltas por la API.
        """
        response = self.session.post(
            "https://api.idealista.com/3.5/es/search",
            data=request,
        )
        return [Property(raw_data) for raw_data in response.json().get("elementList", [])]
