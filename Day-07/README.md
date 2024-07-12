

# Python Tutorial: Conditional Handling with if, elif, else

Welcome to the Python tutorial on conditional handling! This guide covers if statements, elif (else if) statements, and else statements in Python, essential for executing code based on specific conditions.

## Overview

Conditional handling is fundamental in programming to control the flow of execution based on different scenarios. Python provides clear and intuitive syntax for implementing these conditions, making it versatile for various applications.

### Key Concepts Covered:
- **if Statement**: Executes a block of code if a specified condition is true.
- **elif (else if) Statement**: Checks additional conditions sequentially after the initial if statement.
- **else Statement**: Provides a default action when none of the preceding conditions are met.

## Tutorial Content

This tutorial builds on the Python for DevOps series by Abhishek Veeramalla, focusing on mastering conditional statements for effective program control.

### Key Takeaways:
-  📚 Conditional handling in Python is crucial for executing code based on specific conditions using if, elif, and else statements.
-  🛠️ These keywords (if, elif, else) are essential across programming languages, each serving similar purposes with consistent syntax.
-  🖊️ Using the `if` keyword allows executing code blocks conditionally, enhancing program logic and decision-making.
- 🧩 The `else` keyword provides an alternative action if the condition specified by `if` is not met, ensuring comprehensive program control.
- 💡 Utilize `elif` (else if) statements to handle multiple conditions efficiently, ensuring precise logic flow in Python programs.

## Example: Handling Three Conditions

Here's an example Python script demonstrating how to handle three conditions using if, elif, and else:

```python
# Example: Handling instance types with different pricing

instance_type = input("Enter instance type: ")

if instance_type == "t2.micro":
    print("This will charge you $2 per day.")
elif instance_type == "t2.medium":
    print("This will charge you $4 per day.")
elif instance_type == "t2.xlarge":
    print("This will charge you $8 per day.")
else:
    print("Please provide a valid instance type.")

```

In this example:
- The script prompts the user to enter an instance type.
- Based on the user input, it prints the corresponding pricing information using if, elif, and else statements.
- If the user provides an invalid instance type, it prompts them to provide a valid one.

## Next Steps

Practice implementing conditional handling in Python by modifying and expanding upon the provided example. For more advanced concepts, stay tuned for upcoming tutorials in the Python for DevOps series.
