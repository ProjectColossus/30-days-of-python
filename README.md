# Day 1 & Day 2: Python Basics — Variables, Data Types, and Operators

Combined notes and exercises covering the fundamentals from Days 1–2 of the original challenge.

## Topics Covered

**1. Arithmetic Operators**
- Addition, subtraction, multiplication, division
- Modulus (`%`), exponentiation (`**`), floor division (`//`)

**2. Print & Basic Output**
- Using `print()` for strings and expressions

**3. Data Types & `type()`**
- Primitive types: `int`, `float`, `str`, `bool`, `NoneType`, `complex`
- Collection types: `list`, `tuple`, `set`, `dict`
- Key distinctions: tuples are immutable, sets are unordered

**4. Variables & Multiple Assignment**
- Declaring variables individually
- Assigning multiple variables in a single line (tuple unpacking style)

**5. String Operations**
- `len()` to get string length
- Comparing strings with `==`

**6. Formatted Strings (f-strings)**
- Embedding expressions and variables inline
- Controlling decimal precision (e.g., `{value:.2f}`)

**7. The `math` Module**
- `math.sqrt()` — used to calculate Euclidean distance between two points
- `math.pi` — used to calculate area and circumference of a circle

**8. User Input**
- Taking input with `input()` and converting it with `int()`

## Files

| File | Original Day | Description |
|---|---|---|
| `pythonday1.py` | Day 1 | Arithmetic operators, data types, Euclidean distance calculation |
| `pythonday2.py` | Day 2 | Variable assignment, string methods, circle area/circumference calculation |

## Key Takeaways
- Python's dynamic typing means `type()` is a quick way to sanity-check what you're working with.
- f-strings with format specifiers (`:.2f`) are the cleanest way to control numeric output — worth using by default over string concatenation.
- The `math` module comes up early and often; comfortable with `sqrt`, `pi`, and power operations from Day 1 itself.

---
*Part of my [30 Days of Python](.) challenge, following the roadmap toward AI/ML engineering.*
