from pprint import pprint

from idealista_client import Idealista

idealista = Idealista("../config.ini")

pprint(idealista.query(
    {"locationId": "0-EU-ES-01",
     "propertyType": "storageRooms",
     "operation": "sale",
     "maxItems": 50})
)
