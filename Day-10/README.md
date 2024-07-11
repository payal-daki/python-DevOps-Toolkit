python Real-Time Example: List Operations and Exception Handling
In this tutorial, we'll explore how to perform operations on lists in Python and handle exceptions effectively.

List Operations Example
📋 List Operations:

Create a List: Lists in Python are versatile and can hold elements of different data types.
numbers = [1, 2, 3, 4, 5]
Add Elements: Use append() to add new elements to the list.
numbers.append(6)
Access Elements: Access elements by index (numbers[0] for the first element).
first_element = numbers[0]
Iterate Through List: Use a for loop to iterate through all elements.
for num in numbers:    print(num)
Remove Elements: Remove elements with pop() and get the removed element.
removed_number = numbers.pop()
List Length: Find the number of elements in the list using len().
list_length = len(numbers)
Exception Handling Example
🚨 Exception Handling:

Index Error Handling: Catch errors when accessing an index that doesn't exist.
try:    print(numbers[10])except IndexError as e:    print(f"Error: {e}. Index out of range!")
Value Error Handling: Manage errors when converting data types (int()).
try:    num_str = "abc"    num_int = int(num_str)except ValueError as e:    print(f"Error: {e}. Cannot convert '{num_str}' to an integer.")
Generic Exception Handling: Handle unexpected errors gracefully.
try:    result = 10 / 0except Exception as e:    print(f"Error: {e}. Something went wrong!")
Finally Block: Execute cleanup code regardless of exceptions.
finally:    print("Execution completed.")
Interactive Elements
🚀 Run and Modify:

Execute the examples in your Python environment.
Experiment with adding more elements to the list or causing different types of exceptions.
🔍 Explore Further:

Try different operations and observe how Python handles exceptions.
Customize the list contents and exception scenarios to suit your learning needs.
