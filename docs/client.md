# Client

The `Idealista` class is the main client for interacting with the Idealista API. It handles authentication, manages API requests, and returns structured responses.

## Initialization

To create an instance of the `Idealista` client, you need to provide either:

- An API key and secret (to generate a bearer token), or
- A pre-generated bearer token.

> [!CAUTION]
> Ensure that your API key and secret are kept secure and not hard-coded in your source code!

### Constructor Parameters

| Parameter    | Type  | Required | Description                                                                        |
| ------------ | ----- | -------- | ---------------------------------------------------------------------------------- |
| `api_key`    | `str` | No       | Your Idealista API key. Required if `token` is not provided.                       |
| `api_secret` | `str` | No       | Your Idealista API secret. Required if `token` is not provided.                    |
| `token`      | `str` | No       | A pre-generated bearer token. If provided, `api_key` and `api_secret` are ignored. |

### Example Usage

```python
from idealista_api.client import Idealista

# Authenticate using API key and secret
client = Idealista(api_key="your_api_key", api_secret="your_api_secret")

# Authenticate using a pre-generated token
client = Idealista(token="your_bearer_token")
```

### Exceptions

- Raises an `Exception` if neither a token nor an API key/secret pair is provided.

---

## Methods

### `query(request: Search) -> Response`

The `query` method sends a search request to the Idealista API and returns the results as a `Response` object.

#### Parameters

| Parameter | Type     | Description                                                                  |
| --------- | -------- | ---------------------------------------------------------------------------- |
| `request` | `Search` | A `Search` object containing the query parameters (e.g., location, filters). |

#### Returns

| Type       | Description                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------- |
| `Response` | A `Response` object containing the API results, including properties and pagination details. |

#### Example Usage

```python
from idealista_api.client import Idealista
from idealista_api.models import Search

# Create the client
client = Idealista(api_key="your_api_key", api_secret="your_api_secret")

# Define the search parameters
search = Search(
    country="es",
    operation="sale",
    property_type="homes",
    location_id="0-EU-ES-01",  # Madrid
    max_items=50,
    num_page=1
)

# Make the query
response = client.query(search)

# Access the results
print(response.total)  # Total number of properties
for property in response.element_list:
    print(property)
```

#### Notes

- The `query` method sends a `POST` request to the Idealista API endpoint (`https://api.idealista.com/3.5/es/search`).
- If the API returns an error (non-200 status code), an `APIException` is raised with details about the error.

---

## Error Handling

### `APIException`

If the API returns an error, the `query` method raises an `APIException`. This exception includes:

- The error message returned by the API.
- The full response dictionary for debugging.

#### Example:

```python
from idealista_api.exceptions import APIException

try:
    response = client.query(search)
except APIException as e:
    print(f"API error: {e}")
    print(f"Response: {e.response}")
```

---

## Notes

- The `Idealista` client automatically manages authentication headers using the provided token.
- Ensure that your API key and secret are kept secure and not hard-coded in your source code.
