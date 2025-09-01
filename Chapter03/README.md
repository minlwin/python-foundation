# Chapter 3 : Writing Statements

In this chapter, we will learn how to write statements in Python. A statement is simply an instruction that tells Python what to do. For example, when you write x = 5, you are giving Python a statement to store the value 5 in the variable x.

Before we can fully understand statements, we need to look at two important ideas: expressions and operators.

- An expression is like a small piece of code that produces a value, such as 2 + 3 or name.upper().
- An operator is a symbol (like +, -, *, ==) that lets us perform actions on values.

Once we understand expressions and operators, we will see how they come together in different types of statements, such as assignments, decisions, and loops. These statements are the tools we use to build programs step by step.

<strong>Target of this Chapter</strong>

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

<strong>Key Points to Remember</strong>
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

<strong>Summary:</strong>

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

#### Common Usage of Expression Statements

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

- Case Values : <br />
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

- Case Patterns<br/>
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
