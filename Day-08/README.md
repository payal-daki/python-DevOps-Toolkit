

# Python Lists and Tuples

This repository provides an interactive guide to Python lists and tuples, covering their definitions, usage, and differences.

## Lists

Lists are ordered collections of items that can be changed or mutated. They are defined using square brackets `[]`.

### Example:
```python
# Creating a list
my_list = ["apple", "banana", "cherry"]

# Accessing elements
first_item = my_list[0]  # "apple"

# Modifying elements
my_list.append("orange")

# Length of the list
list_length = len(my_list)  # 4
```

## Tuples

Tuples are similar to lists but are immutable once created. They are defined using parentheses `()`.

### Example:
```python
# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing elements
first_item = my_tuple[0]  # "apple"

# Tuples are immutable
# my_tuple[0] = "orange"  # This will raise an error

# Length of the tuple
tuple_length = len(my_tuple)  # 3
```

## Differences between Lists and Tuples

- [Lists vs Tuples](#) 🔄 Lists and tuples both are sequences, but lists are mutable whereas tuples are immutable.
- [Mutable Lists](#) 📝 Lists can be modified after creation with operations like append, extend, and remove.
- [Immutable Tuples](#) 🛡️ Tuples cannot be changed after creation, ensuring data integrity.
- [Use Cases](#) 🧩 Lists are ideal for collections of items that may change over time, while tuples are suitable for fixed collections that shouldn't change.

## Interactive Examples

Explore and execute the examples provided in Python to understand the concepts better. Try modifying elements in lists and tuples to observe how Python handles mutability and immutability.

## Further Learning

For more detailed explanations and advanced usage, refer to Python's official documentation and additional resources.

