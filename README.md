# Idealista API Client

![License](https://img.shields.io/github/license/yagueto/idealista-api)

Unofficial Python client for the Idealista API, providing access to real estate data, including property listings, pricing, and location details. 

Data is retrieved from the official Idealista API (https://developers.idealista.com/).

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Developer account on Idealista (you can get API access at https://developers.idealista.com/)
- Python 3.9 or higher
- Packages listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yagueto/idealista-api.git
   cd idealista-api
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv env
   source env/bin/activate
   ```

3. Install the library:
   ```sh
   pip install .
   ```

## Usage

To make queries, you need to have an API key and its secret (provided by Idealista when requesting access to their API).

The parameters for the queries are those specified in the API documentation, passed through a Search object.

### Example usage

```python
from idealista_api import Idealista, Search

API_KEY = os.getenv("IDEALISTA_API_KEY")
API_SECRET = os.getenv("IDEALISTA_API_SECRET")

idealista = Idealista(
    api_key=API_KEY, api_secret=API_SECRET
)

request = Search(
    "es",
    location_id="0-EU-ES-01", # Idealista internal location ID
    property_type="homes",
    operation="sale",
    max_items=50,
    num_page=2
)

ans = idealista.query(request)
```

This returns a Response object, which provides the API response, including the number of returned elements, pagination information, and a list of elements.

```
print(ans)

> Response(page=2, items_per_page=50, total=79, total_pages=2, element_list=[...])
```

> [!TIP] For more information on the Search and Response objects, please refer to the [documentation](./docs).

## Contributing

Contributions are welcome! For any questions or suggestions, please open an issue / pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
