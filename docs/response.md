# Response

The `Response` class represents the data returned by the Idealista API after making a query. It provides information about the results, including pagination details, the total number of items, and a list of properties matching the query.

## Attributes

| Attribute              | Type            | Description                                                                 |
|------------------------|-----------------|-----------------------------------------------------------------------------|
| `actual_page`          | `int`          | The current page number of the results.                                    |
| `items_per_page`       | `int`          | The number of items returned per page.                                     |
| `lower_range_position` | `int`          | The starting position of the current page in the overall result set.       |
| `upper_range_position` | `int`          | The ending position of the current page in the overall result set.         |
| `paginable`            | `bool`         | Indicates whether the results are paginable.                               |
| `summary`              | `list[str]`    | A summary of the search results.                  |
| `total`                | `int`          | The total number of items matching the query.                              |
| `total_pages`          | `int`          | The total number of pages available.                                       |
| `element_list`         | `list[Property]` | A list of `Property` objects representing the individual property listings. |

## Example usage:
```python
response = idealista.query(request)
print(response)
# Output:
# Response(page=1, items_per_page=50, total=200, total_pages=4, element_list=[...])
print(response.total)  # 200
print(response.element_list)  # List of Property objects
```


### Notes
- The `element_list` contains `Property` objects, which provide detailed information about each property.
- Use the `total` and `total_pages` attributes to handle pagination in your application.