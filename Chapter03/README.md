# Chapter 3 : Writing Statements

In this chapter, we will learn how to write statements in Python. A statement is simply an instruction that tells Python what to do. For example, when you write x = 5, you are giving Python a statement to store the value 5 in the variable x.

Before we can fully understand statements, we need to look at two important ideas: expressions and operators.

* An expression is like a small piece of code that produces a value, such as 2 + 3 or name.upper().
* An operator is a symbol (like +, -, *, ==) that lets us perform actions on values.

Once we understand expressions and operators, we will see how they come together in different types of statements, such as assignments, decisions, and loops. These statements are the tools we use to build programs step by step.

## 🎯 Objectives

By the end of this chapter, you will be able to:

1. Recognize what an expression is and how Python evaluates it.
2. Use different operators to perform calculations and comparisons.
3. Explain what a statement is in Python.
4. Write different types of statements to make your programs do useful work.

## Expression

An expression is a combination of variables, values, and operators that Python evaluates to produce a result.

- You can think of an expression as a question you ask Python, and Python gives you the answer.
- Every expression has a value after it is evaluated.

    ```
    # Arithmetic Expression
    2 + 3        # evaluates to 5

    # Using a variable
    x = 4
    x * 5        # evaluates to 20

    # String Expression
    "Hello" + " World"   # evaluates to "Hello World"

    # Function call inside an expression
    len("Python")        # evaluates to 6
    ```

**Key Points to Remember**
1. Expressions always return a value.
    - Example: 10 - 3 returns 7.
2. Expressions can include variables.
    - Example

        ```
        price = 100
        tax = 0.05
        price * tax     # evaluates to 5.0
        ```
3. Expressions can also be function calls.
    - Example
        ```
        name = "Alice"
        name.upper()    # evaluates to "ALICE"
        ```
4. Expressions are the building blocks of statements.
    - For example, an assignment statement uses an expression:
        ```
        total = 2 + 3   # "2 + 3" is an expression
        ```

**Summary:**

An expression is any piece of code that Python can evaluate to a value. Mastering expressions is important because they appear everywhere in Python—inside statements, function calls, and even in conditions for loops and if-statements.

## Operators

An operator is a special symbol (like +, -, *, ==, and) that tells Python to perform a specific action on one or more values (called operands). Operators are used inside expressions to manipulate data and make decisions.

For example:
```
a = 10
b = 3
print(a + b)   # 13  → '+' adds two numbers
print(a > b)   # True → '>' compares two values
```

### Operator Types in Python
| Type           | Operators                     |
| -------------- | ----------------------------- |
| **Arithmetic** | `+` `-` `*` `/` `%` `//` `**` |
| **Comparison** | `==` `!=` `<` `>` `<=` `>=`   |
| **Logical**    | `and` `or` `not`              |
| **Assignment** | `=` `+=` `-=` `*=` `/=` ...   |
| **Membership** | `in` `not in`                 |
| **Identity**   | `is` `is not`                 |

### Examples of Operators

1. Arithmetic Operators
    ```
    x = 10
    y = 3
    print(x + y)   # 13
    print(x - y)   # 7
    print(x * y)   # 30
    print(x / y)   # 3.333...
    print(x % y)   # 1  (remainder)
    print(x // y)  # 3  (floor division)
    print(x ** y)  # 1000 (power: 10^3)
    ```

2. Comparison Operators
    ```
    a = 5
    b = 8
    print(a == b)  # False
    print(a != b)  # True
    print(a < b)   # True
    print(a >= b)  # False
    ```

3. Logical Operators
    ```
    x = True
    y = False
    print(x and y)  # False
    print(x or y)   # True
    print(not x)    # False
    ```

4. Assignment Operators
    ```
    num = 10
    num += 5   # same as num = num + 5
    print(num)  # 15

    num *= 2   # same as num = num * 2
    print(num)  # 30
    ```

5. Membership Operators
    ```
    fruits = ["apple", "banana", "cherry"]
    print("apple" in fruits)      # True
    print("mango" not in fruits)  # True
    ```

6. Identity Operators
    ```
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print(a is b)      # True  (same object in memory)
    print(a is c)      # False (different object, same content)
    print(a is not c)  # True
    ```

### ⚠️ Common Mistakes with Operators

1. Using = instead of ==
    - = is assignment, == is comparison.

        ```
        x = 5
        print(x == 5)   # True
        ```

2. Confusing is with ==
    - == checks if values are equal.
    - is checks if two variables point to the same object in memory.

        ```
        a = [1, 2]
        b = [1, 2]
        print(a == b)   # True (same content)
        print(a is b)   # False (different objects)
        ```

3. Forgetting floor division vs. normal division
    - / always returns a float.
    - // returns the integer (floor) result.

        ```
        print(7 / 2)   # 3.5
        print(7 // 2)  # 3
        ```

### Summary
- Operators are symbols that tell Python to perform actions on values.
- They are grouped into types: arithmetic, comparison, logical, assignment, membership, and identity.
- Operators are the building blocks of expressions and allow you to calculate, compare, and control your program’s logic.
- Watch out for common mistakes like mixing = and ==, or confusing is with ==.

## Statements

A statement is the smallest instruction in a Python program. It tells Python to do something, such as assign a value, perform a calculation, loop through data, define a function, or import a module.

A Python program is simply a sequence of statements executed from top to bottom.

Statements may include:
- Expressions → code that produces a value.
- Keywords → reserved words like if, for, def, import.
- Operators → symbols like +, ==, and.

```
x = 10          # Assignment statement
print(x + 5)    # Expression statement
import math     # Import statement
def greet():    # Function definition statement
    print("Hello!")

```

> Statements are the building blocks of every Python program.

### Types of Statement

In Python, there are different types of statements, each with a specific role in a program:

|Type	|Description|
|-------|-----------|
|Expression Statement| These evaluate an expression and produce a value.|
|Control Flow Statements| These control the order in which statements are executed. |
|Function / Class Definition| These introduce reusable pieces of code (def) or new data structures (class).|
|Import Statements|	These bring in functions, classes, or constants from other modules so you can use them in your program.|

>Each type of statement serves a unique purpose, and together they allow you to build complete Python programs.

### Expression Statements

An expression statement is a statement that consists of just a single expression.

- Its main purpose is to evaluate the expression.
- Often, the result is not saved and may be discarded.
- Expression statements are very common in everyday Python coding.

**Common Usage of Expression Statements**

1. Evaluating values in REP<br />
In the Python interactive shell (REPL), you can type an expression, and Python will immediately show its value.
    ```
    >>> 2 + 3
    5
    >>> "Hello".upper()
    'HELLO'
    ```

2. Assigning a value to a variable<br/>
Assignments use expressions to calculate a value and then store it.
    ```
    x = 10 + 5   # assignment statement with an expression
    print(x)     # 15
    ```

3. Function calls<br/>
Calling a function is also an expression statement.
    ```
    print("Hello, World!")   # function call as a statement

    name = "Alice"
    length = len(name)       # function call used in assignment
    print(length)            # 5
    ```

**Summary**

- An expression statement is simply an expression written as a statement.
- Its result may be discarded, unless it’s stored in a variable or displayed.
- Common forms: evaluating values, assigning variables, and function calls.

### Control Flow Statements

Control flow statements decide how and when parts of your program run. Instead of executing statements strictly from top to bottom, control flow allows your program to make decisions, repeat tasks, or skip certain parts of code.

Control flow statements in Python can be grouped into:
1. Conditional Statements – choose between options.
2. Looping Statements – repeat actions.
3. Branching Statements – change or exit the normal flow inside loops.
4. No Operation Statement – placeholder for “do nothing.”

#### 1. Conditional Statements

`if`, `elif`, `else` Statement

```
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

`match` Statement (Python 3.10+) 

Match Statement take an expression and compare it’s value to successive patterns given as one or more case blocks.

- Case Values : 

    literlals booleans, numbers, strings, enums
    ```
    status = 404

    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Server Error")
        case _:
            print("Unknown Status")  # wildcard case
    ```

- Case Patterns:

    structures like sequences, mappings, classes, gurded patterns<br/>

    `sequence`
    ```
    data = [1, 2, 3]
    match data:
        case [1, 2, 3]:
            print("Exact match")
        case [1, *rest]:
            print("Starts with 1:", rest)
    ```

    `mappings`
    ```
    person = {"name": "Alice", "age": 30}
    match person:
        case {"name": name, "age": age}:
            print(f"{name} is {age} years old")
    ```

    `classes`
    ```
    class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    p = Point(2, 3)

    match p:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x, y):
            print(f"Point at {x}, {y}")    
    ```

    `guraded`
    ```
    value = 10
    match value:
        case x if x > 5:
            print("Greater than 5")
    ```

- Case Wildcard:

    matches anything (default).
    ```
    match 42:
        case _:
            print("Always matches")
    ```

#### 2. Looping Statements

Looping statements in Python are used to execute a block of code repeatedly. This is useful for iterating over sequences like lists, tuples, or strings, or for performing an action a specific number of times. Python's primary looping constructs are the for loop and the while loop.

`for` Statement

The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string). It's a definite loop, meaning the number of iterations is known before the loop starts. A common use case is iterating through the elements of a list.

```
for i in range(3):
    print("Iteration:", i)
```

`while` Statement

The while loop is used to execute a block of code as long as a certain condition is true. It's an indefinite loop because it will continue until the condition becomes false. This type of loop is ideal when you don't know the exact number of iterations beforehand, such as waiting for a user to input a specific value.

```
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

#### 3. Branching Statements
Python also provides control statements to alter the flow of a loop:

`continue` Statement

The continue statement in Python is a control flow statement used to skip the rest of the current iteration of a loop and immediately move on to the next one. It is used inside for and while loops.

When the continue statement is encountered, the code that follows it within the current loop iteration is ignored, and the loop's control is passed to the top of the loop to begin the next iteration. This is particularly useful when you want to handle a specific condition within a loop without exiting the loop entirely.

```
for number in range(1, 6):
    if number == 3:
        continue  # Skips the print statement for number 3
    print(number)

print("Loop has finished.")
```

In this example, the loop will print the numbers 1, 2, 4, and 5. When number becomes 3, the continue statement is executed, and the print(number) line is skipped for that iteration. The loop then proceeds to the next number, which is 4.


`break` Statement

The break statement in Python is a control flow statement used to exit or terminate a loop prematurely. When the break statement is encountered inside a for or while loop, the program's execution immediately jumps to the code that follows the loop, bypassing any remaining iterations.

The break statement is typically used in conjunction with a conditional statement (like an if statement). This allows you to stop a loop when a specific condition is met, even if the loop's natural iteration has not finished. This can be useful for improving efficiency by exiting a loop as soon as you find what you're looking for.

```
for number in range(1, 10):
    if number == 5:
        break  # Exit the loop when number is 5
    print(number)

print("Loop has been terminated.")
```


`for` loop with an `else` clause

In python, else block can be used with looping statements. The else block executes only when the loop completes its entire iteration over the sequence. If a break statement is used to exit the loop early, the else block will be skipped.

```
# The else block WILL execute
for i in range(3):
    print(i)
else:
    print("Loop finished successfully.")

# Output:
# 0
# 1
# 2
# Loop finished successfully.

# The else block WILL NOT execute
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished successfully.")

# Output:
# 0
```


`while` Loop with an `else` Clause

Similarly, for a while loop, the else block will execute only when the loop's condition becomes false. If a break statement is used, the else block is skipped.

```
# The else block WILL execute
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished successfully.")

# Output:
# 0
# 1
# 2
# Loop finished successfully.

# The else block WILL NOT execute
i = 0
while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print("Loop finished successfully.")

# Output:
# 0
```

#### 4. No Operation Statements

Placeholder for “do nothing.” Useful when a statement is required syntactically, but no action is needed.

```
def todo():
    pass   # to be implemented later
```

**Summary**

- Conditional Statements choose different paths (if, elif, else, match).
- Looping Statements repeat tasks (for, while).
- Branching Statements alter the loop flow (break, continue, return).
- No Operation Statement (pass) is a placeholder that does nothing.
- The match statement in Python provides powerful pattern matching with literals, sequences, mappings, classes, wildcards, and guards.

> We will cover Function and Class definitions, as well as Import statements, in the upcoming chapters.


After learning about this chapter, you have to try assignment.<br/>
[Got to Assignment](assignment/README.md)