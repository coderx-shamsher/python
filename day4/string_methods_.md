# Python String Mastery — Complete Deep Guide

Strings Python ki sabse important data types mein se ek hain.

Almost har real-world application mein strings use hoti hain:

* web development
* APIs
* databases
* automation
* AI
* data cleaning
* cybersecurity
* scripting
* file processing

Agar tum strings master kar lete ho:

✅ text processing easy ho jati hai
✅ coding speed improve hoti hai
✅ problem solving strong hoti hai

---

# WHAT IS A STRING?

String = characters ka sequence.

```python id="vjxv92"
name = "Friday"
```

---

# STRING TYPES

```python id="s4bwju"
'a'
"hello"
'''multi line'''
"""multi line"""
```

---

# Strings Are Immutable

```python id="h0ry6n"
text = "hello"

text[0] = "H"
```

❌ ERROR

Because strings immutable hoti hain.

---

# STRING INDEXING

```python id="jpsclg"
text = "python"
```

| Index | Character |
| ----- | --------- |
| 0     | p         |
| 1     | y         |
| 2     | t         |
| 3     | h         |
| 4     | o         |
| 5     | n         |

---

# Negative Indexing

| Index | Character |
| ----- | --------- |
| -1    | n         |
| -2    | o         |
| -3    | h         |

---

# Access Characters

```python id="a5p8nj"
text[0]
```

↓

```python id="b3glwm"
'p'
```

---

# SLICING

## Syntax

```python id="qgk8hf"
string[start:end:step]
```

---

# Example

```python id="oijzz4"
text = "python"

print(text[0:4])
```

Output:

```python id="do2zsa"
pyth
```

---

# Reverse String

```python id="q7vqwh"
text[::-1]
```

Output:

```python id="p3dj73"
nohtyp
```

---

# STRING METHODS

Now real mastery starts.

---

# 1. `upper()`

Convert ALL characters to uppercase.

```python id="fryc5u"
text = "hello"

print(text.upper())
```

Output:

```python id="3onqfy"
HELLO
```

---

# Internal Workflow

```python id="5v6x9x"
h → H
e → E
l → L
```

---

# Use Cases

✅ usernames
✅ normalization
✅ comparisons

---

# 2. `lower()`

Lowercase conversion.

```python id="fjnrgs"
text = "HELLO"

print(text.lower())
```

Output:

```python id="mjlwmg"
hello
```

---

# 3. `capitalize()`

First character uppercase.

```python id="frz3te"
text = "python"

print(text.capitalize())
```

Output:

```python id="3ocx1f"
Python
```

---

# 4. `title()`

Every word first letter uppercase.

```python id="gh18pw"
text = "python programming"

print(text.title())
```

Output:

```python id="5d6f2p"
Python Programming
```

---

# 5. `swapcase()`

Upper ↔ lower reverse.

```python id="im8fq4"
text = "PyThOn"

print(text.swapcase())
```

Output:

```python id="4f08bo"
pYtHoN
```

---

# 6. `strip()`

Spaces remove karta hai.

```python id="4v3vr5"
text = "   hello   "

print(text.strip())
```

Output:

```python id="p6grgh"
hello
```

---

# `lstrip()`

Left spaces remove.

```python id="3b3rpn"
text.lstrip()
```

---

# `rstrip()`

Right spaces remove.

```python id="zjlwm7"
text.rstrip()
```

---

# Real Use

Very important for:

✅ form inputs
✅ CSV data cleaning
✅ APIs

---

# 7. `replace()`

Text replace.

```python id="n8z6dr"
text = "I love Java"

print(text.replace("Java", "Python"))
```

Output:

```python id="grm6pv"
I love Python
```

---

# Replace Limited Times

```python id="a77n5n"
text = "apple apple apple"

print(text.replace("apple", "mango", 2))
```

Output:

```python id="zh6rkx"
mango mango apple
```

---

# 8. `find()`

Substring ka first index.

```python id="3mt9kh"
text = "python programming"

print(text.find("program"))
```

Output:

```python id="kqv52r"
7
```

---

# If Not Found

```python id="zthjql"
print(text.find("java"))
```

↓

```python id="9grt7u"
-1
```

---

# 9. `index()`

`find()` jaisa but:

❌ not found → ERROR

```python id="rrwwtz"
text.index("python")
```

---

# Difference

| Method  | Not Found |
| ------- | --------- |
| find()  | -1        |
| index() | error     |

---

# 10. `startswith()`

```python id="nxm8gj"
text = "python"

print(text.startswith("py"))
```

↓

```python id="8p6cg4"
True
```

---

# 11. `endswith()`

```python id="vfjlwm"
text.endswith("on")
```

↓

```python id="00ztjr"
True
```

---

# Real Usage

✅ file extensions
✅ URL validation
✅ API routing

---

# 12. `split()`

MOST IMPORTANT METHOD.

String → LIST

```python id="vqv3lv"
text = "apple banana mango"

print(text.split())
```

Output:

```python id="3l4qpi"
['apple', 'banana', 'mango']
```

---

# Split By Separator

```python id="6dtxm8"
text = "a,b,c"

print(text.split(","))
```

↓

```python id="s8fxr8"
['a', 'b', 'c']
```

---

# Real Uses

✅ CSV parsing
✅ data extraction
✅ tokenization

---

# 13. `join()`

LIST → STRING

```python id="6p7ql2"
words = ['Python', 'is', 'awesome']

print(" ".join(words))
```

Output:

```python id="4vyu7u"
Python is awesome
```

---

# Internal Workflow

```python id="tqz6yw"
" ".join(words)
```

↓

```python id="h4ek7v"
word1 + " " + word2 + " " + word3
```

---

# 14. `count()`

Count occurrences.

```python id="vvl7i5"
text = "banana"

print(text.count("a"))
```

↓

```python id="3vvrls"
3
```

---

# 15. `isalpha()`

Only alphabets?

```python id="5jvtn0"
"text".isalpha()
```

↓

```python id="j5e1gh"
True
```

---

# 16. `isdigit()`

Only digits?

```python id="hfyxd7"
"123".isdigit()
```

↓

```python id="g2yk18"
True
```

---

# 17. `isalnum()`

Alphabet + numbers only.

```python id="n8j9ic"
"abc123".isalnum()
```

↓

```python id="wwx0g7"
True
```

---

# 18. `isspace()`

Only spaces?

```python id="5gxjlwm"
"   ".isspace()
```

↓

```python id="3ux72x"
True
```

---

# 19. `center()`

Text center align.

```python id="8udtx5"
text = "Python"

print(text.center(20))
```

---

# 20. `ljust()`

Left align.

```python id="h1e58o"
text.ljust(20)
```

---

# 21. `rjust()`

Right align.

```python id="x90bfi"
text.rjust(20)
```

---

# 22. `zfill()`

Zeros add.

```python id="u2nlr0"
"5".zfill(4)
```

↓

```python id="n6jx72"
0005
```

---

# Useful In

✅ invoice numbers
✅ IDs
✅ formatting

---

# 23. `partition()`

Split into 3 parts.

```python id="osz3dr"
text = "hello world"

print(text.partition(" "))
```

Output:

```python id="jlwmci"
('hello', ' ', 'world')
```

---

# Structure

```python id="w10fyz"
(before, separator, after)
```

---

# 24. `format()`

String formatting.

```python id="t5nkh0"
name = "Friday"

print("Hello {}".format(name))
```

---

# Modern Way → f-strings

```python id="msjlwm"
name = "Friday"

print(f"Hello {name}")
```

---

# BEST METHOD TODAY

✅ f-strings

Fast + readable.

---

# ESCAPE CHARACTERS

| Escape | Meaning   |
| ------ | --------- |
| \n     | new line  |
| \t     | tab       |
| \      | backslash |
| "      | quote     |

---

# Example

```python id="v4nqva"
print("Hello\nWorld")
```

Output:

```python id="9g5jlwm"
Hello
World
```

---

# RAW STRINGS

```python id="hcyt0f"
path = r"C:\Users\Friday"
```

Useful for Windows paths.

---

# STRING COMPARISON

```python id="d2n2x8"
"apple" == "apple"
```

↓

```python id="w3qtjc"
True
```

---

# Lexicographical Comparison

```python id="7v9mwe"
"apple" < "banana"
```

↓

```python id="iq5xq5"
True
```

---

# STRING ITERATION

```python id="06v8ae"
for char in "python":
    print(char)
```

---

# STRING COMPREHENSION STYLE

```python id="4ekr3j"
text = "python"

result = "".join([c.upper() for c in text])

print(result)
```

---

# ADVANCED — TRANSLATION TABLE

```python id="7f2xd7"
text = "hello"

table = str.maketrans("h", "H")

print(text.translate(table))
```

---

# REAL-WORLD STRING WORKFLOW

# Data Cleaning Pipeline

```python id="r1dywp"
text = "   PYTHON Programming   "
```

---

## STEP 1 → remove spaces

```python id="uz2m2j"
text.strip()
```

↓

```python id="6ylxg8"
"PYTHON Programming"
```

---

## STEP 2 → lowercase

```python id="8d1t8g"
.lower()
```

↓

```python id="9zvjlwm"
"python programming"
```

---

## STEP 3 → split

```python id="mffq1w"
.split()
```

↓

```python id="z0vxsb"
['python', 'programming']
```

---

# PROFESSIONAL STRING SKILLS

To master strings:

---

# 1. Learn These PERFECTLY

✅ indexing
✅ slicing
✅ split()
✅ join()
✅ replace()
✅ find()
✅ strip()

---

# 2. Then Learn

✅ regex
✅ encoding
✅ parsing
✅ text normalization

---

# MOST IMPORTANT METHODS IN INDUSTRY

| Method          | Importance     |
| --------------- | -------------- |
| split()         | EXTREMELY HIGH |
| join()          | EXTREMELY HIGH |
| replace()       | EXTREMELY HIGH |
| strip()         | VERY HIGH      |
| find()          | VERY HIGH      |
| format/f-string | VERY HIGH      |

---

# FINAL GOLDEN RULE

Strings mastery =

```python id="waz4dt"
INDEXING
+
SLICING
+
split()
+
join()
+
replace()
+
formatting
```

These are the core foundation of professional Python string manipulation.
