Python strings are:

# IMMUTABLE

Matlab:

❌ existing string directly change nahi hoti.

Jab bhi tum string “update” karte ho:

✅ actually Python NEW string create karta hai.

---

# Your Example

```python
str1 = "vancouver"

update = str1[0:1] + "V" + str1[1:]

print(update)
```

Output:

```python
vVancouver
```

But shayad tumhara goal tha:

```python
Vancouver
```

Correct code:

```python
str1 = "vancouver"

update = "V" + str1[1:]

print(update)
```

Output:

```python
Vancouver
```

---

# Now Understand Deeply

---

# STEP 1

```python
str1[0:1]
```

String:

```python
"vancouver"
```

Indexes:

| Index | Character |
| ----- | --------- |
| 0     | v         |
| 1     | a         |
| 2     | n         |
| 3     | c         |
| 4     | o         |
| 5     | u         |
| 6     | v         |
| 7     | e         |
| 8     | r         |

---

# SLICING RULE

```python
[start:end]
```

Means:

✅ start included
❌ end excluded

---

# Example

```python
str1[0:1]
```

Means:

Take characters from:

* index 0 included
* index 1 excluded

So result:

```python
"v"
```

---

# STEP 2

```python
"V"
```

New capital letter.

---

# STEP 3

```python
str1[1:]
```

Means:

Start from index 1 till END.

Output:

```python
"ancouver"
```

---

# STEP 4 → CONCATENATION

```python
"v" + "V" + "ancouver"
```

Result:

```python
"vVancouver"
```

---

# Correct Workflow

If you want replace first letter:

---

## ORIGINAL

```python
"vancouver"
```

---

## TAKE FIRST LETTER OUT

```python
str1[1:]
```

↓

```python
"ancouver"
```

---

## ADD NEW LETTER

```python
"V" + "ancouver"
```

↓

```python
"Vancouver"
```

---

# FINAL

```python
str1 = "vancouver"

update = "V" + str1[1:]

print(update)
```

---

# WHY THIS WORKS?

Because:

❌ Python string modify nahi karta

✅ new string create karta hai

---

# MEMORY CONCEPT

```python
str1 = "hello"
```

Memory:

```python
"hello"
```

Now:

```python
str1[0] = "H"
```

❌ ERROR

Because immutable.

---

# So Python does THIS instead

```python
new_string = "H" + str1[1:]
```

Creates:

```python
"Hello"
```

NEW object.

---

# COMMON STRING UPDATE METHODS

---

# 1. Replace Character Using Slicing

MOST COMMON

```python
name = "john"

updated = "J" + name[1:]

print(updated)
```

Output:

```python
John
```

---

# 2. `replace()` Method

Very important.

```python
text = "hello world"

updated = text.replace("world", "Python")

print(updated)
```

Output:

```python
hello Python
```

---

# How replace() Works

```python
replace(old, new)
```

Python:

* old text find karta hai
* new text se replace karta hai
* NEW string return karta hai

---

# Replace Limited Times

```python
text = "apple apple apple"

print(text.replace("apple", "mango", 1))
```

Output:

```python
mango apple apple
```

---

# 3. Convert to List → Modify → Join

Professional trick.

Because lists mutable hoti hain.

---

## STEP 1

```python
text = "hello"

chars = list(text)

print(chars)
```

Output:

```python
['h', 'e', 'l', 'l', 'o']
```

---

## STEP 2

Modify list.

```python
chars[0] = "H"
```

---

## STEP 3

Convert back.

```python
updated = "".join(chars)

print(updated)
```

Output:

```python
Hello
```

---

# WHY USE THIS METHOD?

Useful when:

✅ many characters modify karne ho
✅ loops use karne ho
✅ dynamic editing ho

---

# Workflow

```python
STRING
   ↓
LIST
   ↓
MODIFY
   ↓
JOIN
   ↓
NEW STRING
```

---

# 4. String Formatting

```python
name = "john"

updated = f"{name[0].upper()}{name[1:]}"
```

Output:

```python
John
```

---

# Breakdown

```python
name[0].upper()
```

↓

```python
"J"
```

---

```python
name[1:]
```

↓

```python
"ohn"
```

---

Combine:

```python
"J" + "ohn"
```

↓

```python
John
```

---

# 5. Using `capitalize()`

Easiest way.

```python
text = "vancouver"

print(text.capitalize())
```

Output:

```python
Vancouver
```

---

# Difference

| Method       | Use                  |
| ------------ | -------------------- |
| slicing      | manual control       |
| replace()    | replace text         |
| list + join  | heavy modifications  |
| capitalize() | first letter capital |
| upper()      | all uppercase        |

---

# DELETE Operations in Strings

Since strings immutable:

Deletion also creates NEW string.

---

# 1. Delete Using Slicing

```python
text = "Python"

updated = text[:2] + text[3:]

print(updated)
```

Output:

```python
Pyhon
```

Deleted:

```python
t
```

---

# Breakdown

```python
text[:2]
```

↓

```python
Py
```

---

```python
text[3:]
```

↓

```python
hon
```

---

Combine:

```python
Pyhon
```

---

# 2. Using replace()

```python
text = "banana"

updated = text.replace("a", "")

print(updated)
```

Output:

```python
bnn
```

---

# Empty String

```python
""
```

means remove.

---

# 3. Remove Spaces

```python
text = "hello world"

updated = text.replace(" ", "")
```

↓

```python
helloworld
```

---

# ADVANCED STRING WORKFLOW

# Real Developer Thinking

---

# Case 1 → Small Changes

Use:

```python
slicing
replace()
```

---

# Case 2 → Many Changes

Use:

```python
list()
join()
```

---

# Case 3 → Pattern Based

Use:

```python
regex
```

---

# Most Common Professional Methods

| Method          | Industry Usage |
| --------------- | -------------- |
| replace()       | VERY HIGH      |
| slicing         | VERY HIGH      |
| split/join      | VERY HIGH      |
| regex           | ADVANCED       |
| list conversion | MODERATE       |

---

# IMPORTANT INTERVIEW QUESTION

# Why Strings Immutable?

Benefits:

✅ memory optimization
✅ security
✅ faster hashing
✅ safe dictionary keys

---

# FINAL GOLDEN RULE

## Strings cannot be changed directly.

Every update:

```python
OLD STRING
   ↓
NEW STRING CREATED
```

Always remember this.
