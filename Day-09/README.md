

# Loops and Control Statements in Python

In Python, loops and control statements are essential for iterating over data and controlling program flow. This guide explores the usage of `for` loops, `while` loops, `break`, and `continue` statements with practical examples.

## For Loop

The `for` loop in Python iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each element.

### Example

```python
# Example of a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

This loop will iterate through each item in the `fruits` list and print each fruit name.

## While Loop

The `while` loop continues to execute a block of code as long as a specified condition is true.

### Example

```python
# Example of a while loop
count = 0
while count < 5:
    print(count)
    count += 1
```

This loop prints numbers from 0 to 4 because the condition `count < 5` is true until `count` reaches 5.

## Break Statement

The `break` statement terminates the loop prematurely, even if the loop's condition is still true.

### Example

```python
# Example of a break statement
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)
```

In this example, the loop stops as soon as `number` equals 3, and only prints `1` and `2`.

## Continue Statement

The `continue` statement skips the current iteration of a loop and proceeds to the next iteration.

### Example

```python
# Example of a continue statement
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)
```

Here, the loop prints all numbers except 3 because the `continue` statement skips printing `3`.

---

Explore these examples in Python to understand how loops and control statements enhance program functionality. Experiment with different conditions and sequences to master their usage.

🔍 Dive deeper into Python loops and control statements with these interactive examples!
