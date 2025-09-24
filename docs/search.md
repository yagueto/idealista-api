# Search

The `Search` class is used to define the parameters for a search query when interacting with the Idealista API. It allows you to specify filters such as location, property type, operation type (e.g., sale or rent), and other optional parameters to refine your search.

## Attributes

The `Search` class includes the following attributes:

| Attribute         | Type               | Required | Description                                                                 |
|-------------------|--------------------|----------|-----------------------------------------------------------------------------|
| `country`         | `str`             | Yes      | The country code (e.g., `"es"` for Spain).                                  |
| `operation`       | `str`             | Yes      | The operation type (`"sale"` or `"rent"`).                                  |
| `property_type`   | `str`             | Yes      | The type of property (`"homes"`, `"offices"`, etc.).                        |
| `center`          | `str` or `None`   | No       | Coordinates of the search center in the format `"lat,lon"`.                |
| `distance`        | `float` or `None` | No       | Search radius in meters.                                               |
| `location_id`     | `str` or `None`   | No       | Idealista's internal location ID.        |
| `locale`          | `str` or `None`   | No       | Language for the results (e.g., `"en"` or `"es"`).                         |
| `max_items`       | `int` or `None`   | No       | Maximum number of items to retrieve per page (maximum 50).                              |
| `num_page`        | `int` or `None`   | No       | Page number for paginated results.                                         |
| `max_price`       | `int` or `None`   | No       | Maximum price for the properties.                                          |
| `min_price`       | `int` or `None`   | No       | Minimum price for the properties.                                          |
| `since_date`      | `str` or `None`   | No       | Filter properties listed since a specific date (possible filters: `W: last week, M: last month, T: last day (for rent except rooms), Y: last 2 days (sale and rooms)`).   |
| `order`           | `str` or `None`   | No       | [See below](#order).                                    |
| `sort`            | `str` or `None`   | No       | Sorting criteria (`asc` or `desc`).                            |
| `ad_ids`          | `list[str]` or `None` | No    | List of specific ad IDs to retrieve.                                       |
| `has_multimedia`  | `bool` or `None`  | No       | Filter properties with multimedia content (e.g., photos or videos).        |
| `bank_offer`      | `bool` or `None`  | No       | Filter properties that are bank offers.                                    |
| `custom_filters`  | `dict`            | No       | Additional filters specific to property types (e.g., `"bedrooms": 3`), refer to API docs.     |



### Example usage:
```python
search = Search(
    country="es",
    operation="sale",
    property_type="homes",
    location_id="0-EU-ES-01",
    max_items=50,
    num_page=1,
    custom_filters={"bedrooms": 3, "bathrooms": 2}
)
```


## Order

### Allowed Values for `order` by Property Type

The `order` parameter determines how search results are sorted. The available values depend on the selected `property_type`:

| Property Type | Allowed `order` Values                                                                                           |
|---------------|------------------------------------------------------------------------------------------------------------------|
| **garages**   | `distance`, `price`, `street`, `photos`, `publicationDate`, `modificationDate` (rent only), `weigh`, `pricedown` |
| **premises**  | `distance`, `price`, `street`, `photos`, `publicationDate`, `modificationDate`, `size`, `floor`, `ratioeurm2` (rent only), `weigh`, `pricedown` |
| **offices**   | `distance`, `price`, `street`, `photos`, `publicationDate`, `modificationDate`, `size`, `floor`, `ratioeurm2`, `weigh`, `pricedown` |
| **homes**     | `distance`, `price`, `street`, `photos`, `publicationDate`, `modificationDate`, `size`, `floor`, `rooms`, `ratioeurm2` (rent only), `weigh`, `pricedown` |
| **rooms**     | `distance`, `price`, `street`, `photos`, `publicationDate`, `modificationDate`, `floor`                          |

## Notes
- Some values (e.g., `modificationDate`, `ratioeurm2`) are only available for specific operations such as rent.
- Refer to the Idealista API documentation for the most up-to-date list of allowed values and their usage.
- **Required Fields**: Ensure that `country`, `operation`, and `property_type` are always provided.
- **Custom Filters**: Use the `custom_filters` dictionary to add property-specific filters (e.g., number of bedrooms, bathrooms, etc.).
- **Pagination**: Use `max_items` and `num_page` to handle paginated results.

For more details on the available filters, refer to the Idealista API documentation (provided by Idealista when requesting API access).