<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 1️⃣ Variables in Python

## 2️⃣ Definition \& Deep Explanation

**Definition**: Variables in Python are named references (or "labels") that point to objects in memory. Unlike languages like C++ or Java, Python variables don't declare types upfront—Python dynamically determines the type based on the assigned value.

**Why variables are essential in modern Python development**:

- **Store and reuse data**: Without variables, you'd repeat values everywhere, making code unmaintainable
- **Memory efficiency**: Python reuses the same object for identical immutable values (interning)
- **Dynamic nature**: Same variable can hold different types at different times, perfect for rapid prototyping
- **Real project usage**: Every Python app (web APIs, data pipelines, automation) uses variables to track users, database results, config settings, API responses

**Where used in real projects**:

```
- Web apps: `user_id`, `session_token`, `request_data`
- Data science: `df` (DataFrame), `model_accuracy`, `features_list`
- Automation: `file_path`, `config_settings`, `processed_count`
- Backend APIs: `db_connection`, `user_cart`, `api_response`
```

**Key Rules \& Important Points**:

1. **Naming**: `snake_case` (lowercase + underscores), start with letter/underscore, no spaces
2. **Dynamic typing**: `x = 5; x = "hello"` ✅ (type changes automatically)
3. **Assignment**: Single `=` creates reference: `a = b` (a points to same object as b)
4. **Scope**: LEGB rule (Local, Enclosing, Global, Built-in)
5. **Mutability**: `a = [1,2]; b = a; b.append(3)` changes `a` too!
6. **None**: Default "null" value: `result = None`
7. **Type hints** (Python 3.6+): `name: str = "John"` (IDE support, not enforced)

**Memory Model**: Variables are like sticky notes pointing to objects. Change the note, object stays. Point to new object, old one garbage collected.

## 3️⃣ Code Examples with Explanation

## ✅ Definition

A **variable** is a name that stores data in memory.

A **data type** defines what kind of data the variable holds.

Example:

```python
name = "Alice"
age = 25
```

Here:

* `name` → string (`str`)
* `age` → integer (`int`)

---

### Basic Variable Operations

```python
# Real-world: User registration form processing
user_name: str = "john_doe"           # String (text)
user_age: int = 25                    # Integer (whole numbers)
account_balance: float = 1250.75      # Float (decimals)
is_premium: bool = True               # Boolean (True/False)
user_tags = ["vip", "active"]         # List (mutable collection)

print(f"User: {user_name}, Age: {user_age}")  # f-string formatting
print(type(user_name))  # <class 'str'>
```

**What we did**: Created variables for different data types with type hints.

**How it works**: Python allocates memory for each object. Variables are references (pointers) to these objects. `type()` reveals the underlying object type.

**Why this way**: Type hints improve code readability and IDE autocompletion. f-strings are fastest string formatting (Python 3.6+).

### Variable Assignment \& Mutability

```python
# Real-world: Shopping cart example
cart1 = ["laptop", "mouse"]           # New list object
cart2 = cart1                         # Reference same object!
cart2.append("keyboard")

print(cart1)  # ['laptop', 'mouse', 'keyboard']  <- BOTH changed!
print(cart2)

# Fix: Create COPY
cart3 = cart1.copy()  # or list(cart1), cart1[:]
cart3.append("monitor")
print(cart1)  # Unchanged!
```

**What we did**: Demonstrated reference vs copy behavior.

**How it works**: Python passes references by value. `cart2 = cart1` copies the *reference*, not the list. `.copy()` creates new object.

**Best practices**: Always copy mutable objects (`list.copy()`, `dict.copy()`, `deepcopy` for nested).

### Multiple Assignment \& Unpacking

```python
# Real-world: Database query result
user_id, user_name, is_active = 123, "alice", True
first_name, *middle_names, last_name = "John", "Lee", "Smith", "middle"

print(f"User {user_id}: {user_name}, Active: {is_active}")
print(f"Full name: {first_name} {last_name}")  # middle_names = ['Lee', 'Smith']
```

**Why this way**: Pythonic (idiomatic). Unpacks tuples/databases efficiently. `*` captures remaining items.

## 4️⃣ Practice Exercises (Beginner Level)

**Exercise 1: User Profile** (Easy)

```python
# Create variables for your profile and print formatted summary
# Expected: "Hi, I'm Alice, 28 years old, Software Engineer at Google"
```

*Hint*: Use f-strings, str/int/bool

**Exercise 2: Shopping Budget** (Medium)

```python
# Variables: budget=1000, laptop=850, accessories=120
# Print: "Enough for laptop? True/False, Remaining: 30"
```

*Hint*: Calculate `remaining = budget - total`

**Exercise 3: Team Roster** (Medium)

```python
# teams = ["Dev", "Design", "QA"]
# team_count = 3
# Print each: "Team 1: Dev", "Team 2: Design", etc.
```

*Hint*: `enumerate(teams)`

**Exercise 4: Config Settings** (Real-world)

```python
# config = {"debug": True, "port": 8080, "timeout": 30}
# Print all values with labels
```

*Hint*: Loop through dictionary

**🔥 Challenge**: Create a function `process_order(items, budget)` that returns `True` if affordable, with copy protection.

**Common Errors to Avoid**:

```
❌ BAD: 1stUserName = "john"  # Number start, camelCase
❌ BAD: user name = "john"    # Spaces  
✅ GOOD: user_name = "john"
```

Master variables = master Python foundation! What's next: functions or data structures?