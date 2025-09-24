from dataclasses import dataclass, field


@dataclass
class Search:
    """Represents a search query"""

    country: str
    operation: str
    property_type: str
    center: str | None = None
    distance: float | None = None
    location_id: str | None = None
    locale: str | None = None
    max_items: int | None = None
    num_page: int | None = None
    max_price: int | None = None
    min_price: int | None = None
    since_date: str | None = None
    order: str | None = None
    sort: str | None = None
    ad_ids: list[str] | None = None
    has_multimedia: bool | None = None
    bank_offer: bool | None = None

    # Other, per-property type, filters:
    custom_filters: dict[str, str | bool | int | float] = field(default_factory=dict)

    def to_json(self) -> dict[str, str | bool | int | float]:
        """Convert the search query to a JSON-serializable dictionary"""
        data = {}

        for element in self.__dict__:
            if element != "custom_filters":
                keys = element.split("_")
                key = keys[0] + "".join([k.capitalize() for k in keys[1:]])
                data[key] = getattr(self, element)
        if self.custom_filters:
            data.update(self.custom_filters)
        # Remove None values and exclude 'custom_filters' key
        return {k: v for k, v in data.items() if v is not None and k != "custom_filters"}


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

    def to_dict(self) -> dict:
        return self.raw_data

    def __str__(self) -> str:
        return f"Property({self.property_code}, {self.address}, {self.price})"


class Response:
    """Represents the API response"""

    actual_page: int
    items_per_page: int
    lower_range_position: int
    upper_range_position: int
    paginable: bool
    summary: list[str]
    total: int
    total_pages: int
    element_list: list[Property]

    def __init__(self, raw_data: dict):
        print(raw_data)
        self.actual_page = raw_data.get("actualPage", 1)
        self.items_per_page = raw_data.get("itemsPerPage", 0)
        self.lower_range_position = raw_data.get("lowerRangePosition", 0)
        self.upper_range_position = raw_data.get("upperRangePosition", 0)
        self.paginable = raw_data.get("paginable", False)
        self.summary = raw_data.get("summary", [])
        self.total = raw_data.get("total", 0)
        self.total_pages = raw_data.get("totalPages", 0)
        self.element_list = [Property(item) for item in raw_data.get("elementList", [])]

    def __str__(self) -> str:
        return f"Response(page={self.actual_page}, items_per_page={self.items_per_page}, total={self.total}, total_pages={self.total_pages}, element_list={self.element_list})"
