from idealista_api import Idealista, Search

idealista = Idealista(
    api_key="API_KEY_HERE", api_secret="API_SECRET_HERE"
)

s = Search(
    "es",
    location_id="0-EU-ES-01",
    property_type="homes",
    operation="sale",
    max_items=50,
    num_page=2
)
print(idealista.query(s))
