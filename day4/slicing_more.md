Tum jis `step` ki baat kar rahe ho wo slicing ka third part hai:

```python
string[start:end:step]
```

Isko deeply samjhte hain easy language mein.

---

# SLICING STRUCTURE

```python
text[start:end:step]
```

| Part  | Meaning                 |
| ----- | ----------------------- |
| start | kahan se start karna    |
| end   | kahan tak jana          |
| step  | kitne gap se move karna |

---

# Example String

```python id="wgn3lc"
text = "PYTHON"
```

Indexes:

| Index | Character |
| ----- | --------- |
| 0     | P         |
| 1     | Y         |
| 2     | T         |
| 3     | H         |
| 4     | O         |
| 5     | N         |

---

# 1. NORMAL SLICING

```python id="9ihkba"
text[0:4]
```

Means:

* index 0 se start
* index 4 se pehle stop

Output:

```python id="6jfmpp"
PYTH
```

---

# Now STEP Add Karte Hain

```python id="jlwmn0"
text[0:6:1]
```

Output:

```python id="a6rqxk"
PYTHON
```

---

# What is STEP?

Step ka matlab:

# "Kitne indexes jump karne hain"

---

# STEP = 1

```python id="9x2lb8"
text[0:6:1]
```

Means:

```python id="jlwmqq"
0 → 1 → 2 → 3 → 4 → 5
```

Har next index pe jao.

Output:

```python id="u7v11y"
PYTHON
```

---

# STEP = 2

```python id="a3jlwm"
text[0:6:2]
```

Means:

```python id="pk3gw6"
0 → 2 → 4
```

Indexes:

| Index | Character |
| ----- | --------- |
| 0     | P         |
| 2     | T         |
| 4     | O         |

Output:

```python id="lfjlwm"
PTO
```

---

# VISUAL FLOW

```python id="agjlwm"
P  Y  T  H  O  N
0  1  2  3  4  5
```

Step = 2:

```python id="iv3p0o"
Take 0
Skip 1

Take 2
Skip 3

Take 4
Skip 5
```

↓

```python id="jlwm5q"
PTO
```

---

# STEP = 3

```python id="prn57w"
text[0:6:3]
```

Movement:

```python id="jlwmr8"
0 → 3
```

Characters:

| Index | Character |
| ----- | --------- |
| 0     | P         |
| 3     | H         |

Output:

```python id="djlwmn"
PH
```

---

# Most Important Example

# Reverse String

```python id="3mjlwm"
text[::-1]
```

Output:

```python id="jlwm9u"
NOHTYP
```

---

# HOW?

---

# Missing Start & End

```python id="5i70va"
text[::-1]
```

Python automatically samajhta hai:

```python id="jlwmvq"
start = end se start karo
end = beginning tak jao
step = -1
```

---

# Negative Step Means

# BACKWARD move karo

---

# VISUAL

```python id="ujlwmz"
P  Y  T  H  O  N
0  1  2  3  4  5
```

Step = -1

Movement:

```python id="jlwm34"
5 → 4 → 3 → 2 → 1 → 0
```

Characters:

```python id="jlwmpp"
N O H T Y P
```

↓

```python id="3jlwmx"
NOHTYP
```

---

# Another Example

```python id="jlwm74"
text[::-2]
```

Movement:

```python id="jlwmah"
5 → 3 → 1
```

Characters:

| Index | Character |
| ----- | --------- |
| 5     | N         |
| 3     | H         |
| 1     | Y         |

Output:

```python id="jlwm4r"
NHY
```

---

# REAL UNDERSTANDING OF STEP

Step means:

# "Next character lene se pehle kitna jump karna hai"

---

# Example

```python id="jlwm7d"
text[::2]
```

Means:

```python id="jlwmjk"
Take every 2nd character
```

Output:

```python id="0jlwmq"
PTO
```

---

# Example

```python id="jlwmq9"
text[1::2]
```

Start from index 1.

Movement:

```python id="jlwm9n"
1 → 3 → 5
```

Characters:

```python id="jlwm4w"
Y H N
```

Output:

```python id="9jlwm2"
YHN
```

---

# Common Step Patterns

| Code     | Meaning           |
| -------- | ----------------- |
| `[::1]`  | normal            |
| `[::2]`  | every 2nd char    |
| `[::3]`  | every 3rd char    |
| `[::-1]` | reverse           |
| `[::-2]` | reverse every 2nd |

---

# Important Thing

```python
[start:end:step]
```

Python internally:

1. start pe jata hai
2. character leta hai
3. `step` jitna jump karta hai
4. next character leta hai
5. repeat until end

---

# Deep Visual Example

```python id="jlwm4x"
text = "ABCDEFGHIJ"
```

Indexes:

| A | B | C | D | E | F | G | H | I | J |
| - | - | - | - | - | - | - | - | - | - |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

---

# Example

```python id="jlwmg2"
text[1:9:2]
```

Start = 1

↓

```python id="1jlwm8"
B
```

Step 2:

```python id="4jlwmq"
1 → 3 → 5 → 7
```

Characters:

```python id="jlwm1q"
B D F H
```

Output:

```python id="6jlwmh"
BDFH
```

---

# Memory Trick

# STEP = Jump Size

```python id="5jlwm6"
step = 1 → no skipping
step = 2 → skip one
step = 3 → skip two
step = -1 → reverse
```

---

# MOST IMPORTANT USES OF STEP

---

# 1. Reverse String

```python id="1jlwm0"
text[::-1]
```

---

# 2. Alternate Characters

```python id="7jlwmv"
text[::2]
```

---

# 3. Even/Odd Index Extraction

Even indexes:

```python id="5jlwmw"
text[::2]
```

Odd indexes:

```python id="4jlwmr"
text[1::2]
```

---

# FINAL GOLDEN RULE

```python
[start:end:step]
```

means:

# "Start here → move with this jump size → stop before end"
