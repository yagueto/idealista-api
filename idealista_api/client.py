import requests
from .utils import get_bearer_token
from .models import Response, Search
from .exceptions import APIException


time_format = "%Y-%m-%d %H:%M:%S"


class Idealista:
    """Idealista API client."""

    session: requests.Session

    def __init__(
        self,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
    ):
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

    def query(self, request: Search) -> Response:
        """
        Realiza una consulta a la API de Idealista.

        Args:
            request (Search): Datos de la solicitud. Los parámetros deben ser los especificados en la documentación de la API.

        Returns:
            list[Property]: Lista de propiedades devueltas por la API.
        """
        response = self.session.post(
            "https://api.idealista.com/3.5/es/search",
            data=request.to_json(),
        )
        response_dict = response.json()
        print(response_dict)
        if response.status_code != 200:
            # TODO: error in query does not always return an "error" key in the json. Sometimes it returns just a {"message": "..."} (i.e. when the query contains an invalid value)
            error_description = response_dict.get("error_description") or response_dict.get("message") or "No description available"
            raise APIException(
                f"Error querying API: {response_dict.get('error', 'Unknown error')} - {error_description}",
                response=response_dict
            )
        return Response(response_dict)
