# main_v2 - Python Functions, Loops & Output

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-orange?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

---

## Scenario

Imagine you are a developer writing your first structured Python program. Rather than putting all logic directly in the script body, you are asked to organise your code into reusable functions that handle greeting, arithmetic, and iteration separately. The goal is to demonstrate that you understand how to define functions, call them from a central `main()` entry point, and produce clean, readable terminal output - foundational skills for any collaborative Python project.

---

## What the Script Does

`main_v2.py` executes top to bottom in 5 clear steps:

1. Defines a `greet()` function that accepts a name and returns a formatted greeting string
2. Defines an `add()` function that accepts two numbers and returns their sum
3. Calls `greet("Alice")` and prints the result to the terminal
4. Calls `add(3, 5)`, stores the result in a variable, and prints it using an f-string
5. Runs a `for` loop counting from 1 to 3, printing each count value on its own line

---

## File Structure

```
main_v2/
├── main_v2.py     ← The script (run this)
└── README.md
```

---

## Python Concepts Used

### 1. `def` - Function Definition
**Definition:** The `def` keyword declares a named, reusable block of code that accepts parameters and can return a value.  
**Why I used it:** Both `greet()` and `add()` are defined with `def` so their logic is encapsulated and callable from anywhere in the script - keeping the `main()` function clean and readable rather than cluttered with raw expressions.

---

### 2. `return`
**Definition:** Exits a function and passes a value back to the caller.  
**Why I used it:** Both functions use `return` so that the computed values - the greeting string and the arithmetic result - can be captured in variables or passed directly to `print()`, rather than being printed inside the function itself. This separates logic from output.

---

### 3. f-strings (`f"..."`)
**Definition:** An f-string is a Python string prefixed with `f` that allows variables and expressions to be embedded directly inside curly braces `{}`, evaluated at runtime.  
**Why I used it:** Used in `greet()` to embed the `name` parameter inline (`f"Hello, {name}!"`) and in `main()` to display the addition result (`f"3 + 5 = {result}"`). F-strings produce cleaner, more readable output formatting than string concatenation.

---

### 4. `print()`
**Definition:** Outputs a value or string to standard output (the terminal), followed by a newline by default.  
**Why I used it:** Used three times in `main()` to display the greeting, the addition result, and each loop count - giving visible confirmation that each function and control structure is working correctly.

---

### 5. `for` loop with `range()`
**Definition:** A `for` loop iterates over a sequence; `range(1, 4)` generates the integers 1, 2, and 3 (the stop value is exclusive).  
**Why I used it:** Demonstrates that Python can repeat an action a fixed number of times without manually writing each step. Counting from 1 to 3 is a minimal, clear example of iteration that avoids off-by-one confusion by using explicit `range()` bounds.

---

### 6. `if __name__ == "__main__"` guard
**Definition:** A standard Python idiom that checks whether the script is being run directly (not imported as a module). When true, it calls `main()` to start execution.  
**Why I used it:** Protects the script's entry point so that if `main_v2.py` is ever imported into another file, none of its output code runs automatically. This is considered best practice for any Python script that defines reusable functions.

---

## Functions Summary

| Function | Parameters | Returns | Purpose |
|---|---|---|---|
| `greet(name)` | `name` - a string | Formatted greeting string | Produces a personalised hello message |
| `add(a, b)` | `a`, `b` - numbers | Sum of `a` and `b` | Performs and returns basic addition |
| `main()` | None | None | Entry point - calls all other functions and drives output |

---

## Expected Output

```text
Hello, Alice!
3 + 5 = 8
Count: 1
Count: 2
Count: 3
```

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/<yourUser>/<repo-name>.git

# Navigate into the directory
cd <repo-name>

# Run the script
python main_v2.py
```

---

## Git Workflow Used

```bash
git status
git add .
git status
git commit -m "Add main_v2 Python script with functions, loop, and entry point guard"
git push
```
