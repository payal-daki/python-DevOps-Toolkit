

## Introduction

Welcome to Day 2 of our Python tutorial series where we dive into strings and their handling functions. In this session, we'll explore practical examples and essential theory to strengthen your understanding of string operations in Python.

## Table of Contents

1. [Overview](#overview)
2. [String Basics](#string-basics)
3. [String Handling Functions](#string-handling-functions)
4. [Practical Examples](#practical-examples)
5. [Conclusion](#conclusion)

## Overview

Python strings are fundamental data types that allow you to work with textual data efficiently. They are immutable sequences, meaning once defined, their content cannot be changed.

## String Basics

Strings can be defined using single (''), double ("") or triple (''''' or """") quotes in Python. They support various escape sequences (\n, \t) for formatting.

```python
# Example of defining strings
single_quoted = 'Hello'
double_quoted = "World"
multiline = '''This is a
multi-line string'''
```

## String Handling Functions

Python provides numerous built-in functions to manipulate strings:

- `len()`: Determines the length of a string.
- `str.upper()` and `str.lower()`: Convert strings to uppercase or lowercase.
- `str.strip()`: Removes leading and trailing whitespace.
- `str.split()`: Splits a string into a list based on a delimiter.
- `str.join()`: Joins elements of a list into a string using the specified delimiter.

## Practical Examples

Let's explore practical examples using these functions:

### Example 1: Length of a String

```python
text = "Python is amazing!"
print(len(text))  # Output: 18
```

### Example 2: Convert Case

```python
text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!
print(text.lower())  # Output: hello, world!
```

### Example 3: Splitting and Joining Strings

```python
text = "Python,Java,Ruby"
languages = text.split(',')
print(languages)  # Output: ['Python', 'Java', 'Ruby']

joined_string = '-'.join(languages)
print(joined_string)  # Output: Python-Java-Ruby
```

## Conclusion

Strings are versatile in Python, offering powerful methods to manipulate text efficiently. By mastering these basic operations, you'll be well-equipped to handle more complex string manipulations in your Python journey.
