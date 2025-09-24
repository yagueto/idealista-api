# Property

The `Property` class represents an individual property listing returned by the Idealista API. It provides access to key details about the property, such as its ID, price, address, and operation type.

## Attributes

| Attribute         | Type     | Description                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| `raw_data`        | `dict`   | The raw dictionary data for the property, as returned by the API.           |
| `property_code`   | `str`    | The unique identifier for the property.                                     |
| `property_type`   | `str`    | The type of property (e.g., `"home"`, `"office"`, etc.).                    |
| `address`         | `str`    | The address of the property.                                                |
| `price`           | `int`    | The price of the property.                                                  |
| `operation`       | `str`    | The operation type (`"sale"` or `"rent"`).                                  |


#### Example:
```python
property = response.element_list[0]
print(property)
# Output:
# Property(12345, Madrid, 250000)

print(property.property_code)  # 12345
print(property.address)        # Madrid
print(property.price)          # 250000

# Access raw data
print(property["propertyType"])  # home

# Convert to dictionary
print(property.to_dict())
```

### Notes
- The `raw_data` attribute contains all the data returned by the API for the property. Use it to access additional fields not explicitly defined as attributes.
- The `Property` class is designed to be lightweight and extensible, making it easy to add new attributes or methods as needed.
