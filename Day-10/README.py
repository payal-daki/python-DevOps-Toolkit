
In this tutorial, we'll explore how to perform operations on lists in Python and handle exceptions effectively.

#### List Operations Example

Lists in Python are versatile data structures that allow you to store and manipulate collections of items. Here’s a practical example of list operations:

```python
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Adding a new number to the list
numbers.append(6)
print(f"Updated list: {numbers}")

# Accessing elements in the list
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# Iterating through the list
print("All elements:")
for num in numbers:
    print(num)

# Removing an element from the list
removed_number = numbers.pop()
print(f"Removed element: {removed_number}")
print(f"Updated list after removal: {numbers}")

# Finding the length of the list
print(f"Length of the list: {len(numbers)}")
```

#### Exception Handling Example

Exception handling in Python allows you to gracefully manage errors that may occur during execution. Here’s how to handle exceptions effectively:

```python
try:
    # Attempting to access an index that doesn't exist
    print(numbers[10])  # Index 10 does not exist in this list
except IndexError as e:
    print(f"Error: {e}. Index out of range!")

try:
    # Converting a string to an integer (potential ValueError)
    num_str = "abc"
    num_int = int(num_str)
except ValueError as e:
    print(f"Error: {e}. Cannot convert '{num_str}' to an integer.")

try:
    # Handling generic exceptions
    result = 10 / 0  # Division by zero
except Exception as e:
    print(f"Error: {e}. Something went wrong!")

finally:
    print("Execution completed.")
```

#### Theory: List Operations and Exception Handling

**Lists:**  
Lists are ordered collections in Python that can hold elements of different data types. They are mutable, meaning you can modify their content after creation. Common operations include adding elements (`append()`), accessing elements by index, iterating through the list using loops, removing elements (`pop()`), and finding the length (`len()`).

**Exception Handling:**  
Exception handling allows you to manage and respond to errors in your code gracefully. In Python, exceptions are raised when an error occurs during execution. The `try`, `except`, `else`, and `finally` blocks are used to handle exceptions:
- `try`: Encloses the code that may raise an exception.
- `except`: Catches and handles specific exceptions.
- `else`: Executes if no exceptions are raised in the `try` block.
- `finally`: Executes cleanup code regardless of whether an exception occurred.

### Interactive Elements

🚀 Feel free to run and modify the examples above in your Python environment! Experiment with adding more elements to the list or causing different types of exceptions to see how the code behaves.

🔍 Explore different ways to handle exceptions and enhance the list operations based on your needs and applications.

