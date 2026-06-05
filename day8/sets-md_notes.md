# Python Sets — Complete Beginner to Advanced Guide

Python mein **Set** ek built-in data structure hai jo:

* unique values store karta hai
* unordered hota hai
* mutable hota hai
* mathematical set operations support karta hai

Set bahut powerful hai aur real-world programming mein extremely useful hota hai — especially:

* duplicate removal
* fast searching
* comparisons
* filtering
* data analysis
* permissions systems
* recommendation engines
* graph algorithms

---

# What is a Set?

Set ek collection hai:

✅ unique elements
❌ duplicate values allowed nahi
❌ indexing nahi hoti
❌ order fixed nahi hota

---

# Creating a Set

```python
fruits = {"apple", "banana", "mango"}

print(fruits)
```

Output:

```python
{'apple', 'banana', 'mango'}
```

---

# Duplicate Values Automatically Remove Ho Jati Hain

```python
numbers = {1, 2, 3, 3, 3, 4}

print(numbers)
```

Output:

```python
{1, 2, 3, 4}
```

---

# Why?

Set internally uniqueness maintain karta hai.

---

# Empty Set

⚠️ Important

```python
my_set = {}
```

Ye EMPTY DICTIONARY banata hai.

Correct way:

```python
my_set = set()
```

---

# Set Properties

| Property               | Set |
| ---------------------- | --- |
| Ordered                | No  |
| Indexed                | No  |
| Duplicate Allowed      | No  |
| Mutable                | Yes |
| Hashable Elements Only | Yes |

---

# Accessing Set Values

Set unordered hota hai.

Isliye:

```python
my_set[0]
```

❌ ERROR

---

# Loop Through Set

```python
colors = {"red", "blue", "green"}

for color in colors:
    print(color)
```

---

# Add Elements

## `add()`

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

Output:

```python
{1, 2, 3, 4}
```

---

# Add Multiple Values

## `update()`

```python
numbers = {1, 2}

numbers.update([3, 4, 5])

print(numbers)
```

---

# Remove Elements

---

## `remove()`

```python
numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)
```

⚠️ If value not found → ERROR

---

## `discard()`

```python
numbers.discard(10)
```

No error.

---

## `pop()`

```python
numbers.pop()
```

Random item remove karega.

Because set unordered hai.

---

## `clear()`

```python
numbers.clear()
```

Sab remove.

---

# Membership Testing (VERY IMPORTANT)

Sets ka biggest advantage:

## EXTREMELY FAST SEARCHING

```python
names = {"Ali", "Ahmed", "John"}

print("Ali" in names)
```

Output:

```python
True
```

---

# Why Sets Are Fast?

Sets internally use:

# HASH TABLES

Isi wajah se:

* searching fast
* insertion fast
* deletion fast

Average complexity:

| Operation | Time |
| --------- | ---- |
| Search    | O(1) |
| Insert    | O(1) |
| Delete    | O(1) |

---

# Compare With List

## LIST SEARCH

```python
100000 items check
```

Slow.

Because Python one-by-one search karta hai.

---

## SET SEARCH

Direct hash lookup.

Very fast.

---

# Real-World Usage of Sets

---

# 1. Remove Duplicates

MOST COMMON USE

```python
numbers = [1, 2, 2, 3, 4, 4]

unique = set(numbers)

print(unique)
```

Output:

```python
{1, 2, 3, 4}
```

---

# Convert Back to List

```python
unique_list = list(set(numbers))
```

---

# 2. Fast Lookup System

```python
blocked_users = {"john", "mike", "alex"}

username = "john"

if username in blocked_users:
    print("Blocked")
```

---

# 3. Common Elements Find Karna

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
```

Output:

```python
{3, 4}
```

---

# Set Operations (VERY IMPORTANT)

---

# Union

Combine all unique values.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

Output:

```python
{1, 2, 3, 4, 5}
```

---

# Intersection

Common values.

```python
print(a & b)
```

Output:

```python
{3}
```

---

# Difference

```python
print(a - b)
```

Output:

```python
{1, 2}
```

---

# Symmetric Difference

Non-common values.

```python
print(a ^ b)
```

Output:

```python
{1, 2, 4, 5}
```

---

# Methods Version

| Operator | Method                 |         |
| -------- | ---------------------- | ------- |
| `        | `                      | union() |
| `&`      | intersection()         |         |
| `-`      | difference()           |         |
| `^`      | symmetric_difference() |         |

---

# Example

```python
a.union(b)
```

---

# Subset

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

Output:

```python
True
```

---

# Superset

```python
print(b.issuperset(a))
```

---

# Disjoint

No common elements.

```python
a = {1, 2}
b = {5, 6}

print(a.isdisjoint(b))
```

Output:

```python
True
```

---

# Immutable Set → `frozenset`

Normal set mutable hota hai.

Agar immutable chahiye:

```python
fs = frozenset([1, 2, 3])
```

Now:

```python
fs.add(4)
```

❌ ERROR

---

# Why Frozenset Useful?

Dictionary key bana sakte ho.

Because normal set hashable nahi hota.

---

# Set Comprehension

Like list comprehension.

```python
squares = {x*x for x in range(5)}

print(squares)
```

Output:

```python
{0, 1, 4, 9, 16}
```

---

# Important Limitation

Set ke andar:

✅ immutable values allowed

* int
* str
* tuple

❌ mutable values allowed nahi

* list
* dictionary
* set

---

# Example

```python
my_set = {[1, 2], [3, 4]}
```

❌ ERROR

---

# Because Lists Hashable Nahi Hoti

---

# Internal Working (Advanced)

Python sets use:

# Hash Tables

Each element ka hash banta hai.

Example:

```python
hash("apple")
```

Python hash calculate karta hai.

Then memory bucket mein value store hoti hai.

Isi wajah se searching bahut fast hoti hai.

---

# Set vs List

| Feature                 | List | Set  |
| ----------------------- | ---- | ---- |
| Ordered                 | Yes  | No   |
| Duplicates              | Yes  | No   |
| Indexing                | Yes  | No   |
| Search Speed            | Slow | Fast |
| Mathematical Operations | No   | Yes  |

---

# When To Use Set?

Use set when:

✅ duplicates remove karne ho
✅ fast searching chahiye
✅ unique values maintain karni ho
✅ mathematical operations karni ho
✅ comparisons karne ho

---

# When NOT To Use Set?

Avoid set when:

❌ order important ho
❌ indexing chahiye
❌ duplicate values preserve karni ho

---

# Real Industry Examples

---

# Web Development

## Permission systems

```python
user_permissions = {"read", "write"}
```

---

# Data Science

Unique categories extraction.

```python
unique_countries = set(country_column)
```

---

# Cybersecurity

Blocked IPs lookup.

---

# Search Engines

Fast keyword matching.

---

# Recommendation Systems

Common interests detection.

---

# Graph Algorithms

Visited nodes tracking.

```python
visited = set()
```

---

# Performance Example

```python
numbers = set(range(1000000))

print(999999 in numbers)
```

Extremely fast.

---

# Important Interview Questions

---

# Difference Between `{}` and `set()`

```python
{}
```

Dictionary.

```python
set()
```

Empty set.

---

# Can Set Store Duplicate Values?

No.

---

# Why Set Faster Than List?

Hash table implementation.

---

# Can We Index Set?

No.

---

# Can Set Store List?

No.

Because list mutable and unhashable hoti hai.

---

# Final Summary

# Sets are best for:

✅ uniqueness
✅ fast lookup
✅ comparisons
✅ filtering
✅ duplicate removal
✅ mathematical operations

---

# Most Important Things to Remember

```python
set()
```

empty set

---

```python
in
```

very fast with sets

---

```python
|
&
-
^
```

main set operators

---

```python
set(list)
```

duplicates remove

---

```python
frozenset()
```

immutable set
