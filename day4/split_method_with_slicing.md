Chalo is line ko completely breakdown karte hain:

```python
result = text.split("is ")[1].split(" and")[0]
```

Ye line beginner ko confusing lagti hai because ismein:

* method chaining ho rahi hai
* lists return ho rahi hain
* indexing use ho rahi hai `[0]`, `[1]`

Ab step-by-step dekhte hain.

---

# Original String

```python
text = "My name is Friday and I live in India"
```

---

# STEP 1 → `split("is ")`

```python
text.split("is ")
```

## `split()` kya karta hai?

Ye string ko todta hai.

Jo value tum `split()` ke andar dete ho, us jagah string cut hoti hai.

---

## Example

```python
text = "apple-mango-banana"

print(text.split("-"))
```

Output:

```python
['apple', 'mango', 'banana']
```

---

# Ab hamara actual example

```python
text.split("is ")
```

String:

```python
"My name is Friday and I live in India"
```

Python `"is "` ko dhundega.

Jahan `"is "` milega, wahaan string cut hogi.

Result:

```python
['My name ', 'Friday and I live in India']
```

---

# IMPORTANT

`split()` ALWAYS LIST return karta hai.

Yahan:

```python
['My name ', 'Friday and I live in India']
```

Ye ek LIST hai.

---

# LIST INDEXING

List ke andar har item ka number hota hai.

```python
['My name ', 'Friday and I live in India']
```

| Index | Value                        |
| ----- | ---------------------------- |
| 0     | 'My name '                   |
| 1     | 'Friday and I live in India' |

---

# `[1]` ka matlab

```python
text.split("is ")[1]
```

Means:

👉 split hone ke baad LIST ka item number 1 lao.

So:

```python
'Friday and I live in India'
```

mil gaya.

---

# STEP 2

Ab ye part execute hota hai:

```python
'Friday and I live in India'.split(" and")
```

Again split.

Python `" and"` pe string cut karega.

Result:

```python
['Friday', ' I live in India']
```

Again LIST mili.

---

# LIST INDEXING AGAIN

```python
['Friday', ' I live in India']
```

| Index | Value              |
| ----- | ------------------ |
| 0     | 'Friday'           |
| 1     | ' I live in India' |

---

# `[0]` ka matlab

```python
.split(" and")[0]
```

Means:

👉 list ka first item lao.

So:

```python
'Friday'
```

---

# Final Result

```python
result = 'Friday'
```

---

# VISUAL FLOW

## Step 1

```python
text.split("is ")
```

↓

```python
['My name ', 'Friday and I live in India']
```

↓

```python
[1]
```

↓

```python
'Friday and I live in India'
```

---

## Step 2

```python
'Friday and I live in India'.split(" and")
```

↓

```python
['Friday', ' I live in India']
```

↓

```python
[0]
```

↓

```python
'Friday'
```

---

# SIMPLE RULE

## `[0]`

First item

---

## `[1]`

Second item

---

## `[2]`

Third item

---

# Example

```python
numbers = [10, 20, 30, 40]
```

| Index | Value |
| ----- | ----- |
| 0     | 10    |
| 1     | 20    |
| 2     | 30    |
| 3     | 40    |

---

```python
print(numbers[0])
```

Output:

```python
10
```

---

```python
print(numbers[2])
```

Output:

```python
30
```

---

# Why Python starts from 0?

Programming languages mostly zero-indexed hoti hain.

Memory addressing aur internal implementation ki wajah se.

So:

```python
[0]
```

means:

👉 first position.

---

# VERY IMPORTANT CONCEPT

Methods can return objects.

Example:

```python
text.split()
```

returns LIST.

Fir tum us LIST pe indexing use kar sakte ho.

---

# Method Chaining

```python
text.split("is ")[1].split(" and")[0]
```

Isko method chaining kehte hain.

Python left-to-right execute karta hai.

---

# Easier Version (Readable)

Professional developers aksar isko readable banate hain:

```python
text = "My name is Friday and I live in India"

step1 = text.split("is ")

print(step1)
```

Output:

```python
['My name ', 'Friday and I live in India']
```

---

```python
step2 = step1[1]

print(step2)
```

Output:

```python
Friday and I live in India
```

---

```python
step3 = step2.split(" and")

print(step3)
```

Output:

```python
['Friday', ' I live in India']
```

---

```python
result = step3[0]

print(result)
```

Output:

```python
Friday
```

---

# BEST PRACTICE

For beginners:

❌ Avoid huge chained lines

```python
text.split("is ")[1].split(" and")[0]
```

✅ Use step-by-step variables

Because debugging easy hoti hai.

---

# Golden Concept

## `split()` returns LIST

## `[index]` extracts item from LIST

Yahi pura game hai.
