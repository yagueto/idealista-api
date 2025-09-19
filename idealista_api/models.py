class Property:
    """Represents a property listing"""

    raw_data: dict

    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def __getitem__(self, item):
        return self.raw_data.get(item)

    @property
    def property_code(self):
        """Return the property ID"""
        return self.raw_data.get("propertyCode")

    @property
    def property_type(self):
        """Return the property type"""
        return self.raw_data.get("propertyType")

    @property
    def address(self):
        """Return the property address"""
        return self.raw_data.get("address")

    @property
    def price(self):
        """Return the property price"""
        return self.raw_data.get("price")

    @property
    def operation(self):
        """Return the operation type (rent, sale)"""
        return self.raw_data.get("operation")

    def __str__(self) -> str:
        return f"Property({self.property_code}, {self.address}, {self.price})"