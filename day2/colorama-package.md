# 1️⃣ Terminal Colors in Python (Colorama)

## 2️⃣ Definition & Deep Explanation

**Definition**: Colorama ek Python package hai jo terminal/console output ko colors deta hai. Ye ANSI escape codes use karta hai jo terminal ko samjhata hai ki text ka color kya ho.

**Why use karte hain**:
- **Errors ko highlight**: Red mein error, Green mein success
- **Logs better**: Blue info, Yellow warning
- **CLI tools**: Professional apps banane ke liye (pip install, CLI commands)
- **Windows/Linux dono mein**: Colorama cross-platform hai

**Real projects mein**:
```
- CLI tools (pip list, git status jaisa)
- Logging systems (error=red, info=blue)
- Progress bars, menus
- DevOps scripts
```

**Key Points**:
1. **Install**: `pip install colorama`
2. **Import**: `from colorama import Fore, Style, init`
3. **init()**: Windows ke liye must (sirf ek baar call karo)
4. **Fore.RED + "text" + Style.RESET_ALL**: Color + reset (warna next text bhi color ho jayega)

## 3️⃣ Installation & Code Examples

### Step 1: Install (Terminal/Command Prompt mein)
```
pip install colorama
```
**Ya**:
```
python -m pip install colorama
```

### Step 2: Basic Color Code
```python
from colorama import init, Fore, Back, Style

# Windows/Linux ke liye (sirf pehli baar)
init()

print(Fore.GREEN + "✅ Success!" + Style.RESET_ALL)
print(Fore.RED + "❌ Error found!" + Style.RESET_ALL)
print(Fore.YELLOW + "⚠️ Warning" + Style.RESET_ALL)
print(Fore.BLUE + "ℹ️ Information" + Style.RESET_ALL)
print(Style.RESET_ALL)  # Safe reset
```

**Output**:
```
✅ Success! (Green)
❌ Error found! (Red)
⚠️ Warning (Yellow)
ℹ️ Information (Blue)
```

**What we did**: Imported colors, `init()` activate kiya, Fore.COLOR se color lagaya.

**How it works**: `Fore.RED` ek string hai jo terminal ko "red kar do" bolta hai. `Style.RESET_ALL` normal karta hai.

### Example 3: Real-world Error Handler
```python
from colorama import init, Fore, Style
init()

def check_age(age):
    if age < 18:
        print(Fore.RED + f"❌ Sorry, {age} years old - under age!" + Style.RESET_ALL)
    elif age > 100:
        print(Fore.YELLOW + f"🤔 {age}? Age verification needed!" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"✅ Welcome! Age {age} verified." + Style.RESET_ALL)

check_age(15)  # Red
check_age(25)  # Green
check_age(150) # Yellow
```

**Why this way**: Professional CLI output. Easy to read during debugging.

## 4️⃣ Practice Exercises (Simple)

**Exercise 1: Login Checker**
```python
# username = "admin", password = "1234"
# Check: sahi = Green "Login Success", galat = Red "Failed"
```

**Exercise 2: Grade System**
```python
marks = 85
# 90+ Green A+, 70-89 Yellow B, <70 Red Fail
```

**Exercise 3: File Checker**
```python
files = ["config.py", "missing.txt"]
# Existing: Green ✅, Missing: Red ❌
```

**Exercise 4: Progress Tracker**
```python
tasks_done = 7
total_tasks = 10
# Green: "70% Complete" with progress color
```

**🔥 Challenge**: Menu banaye jisme options different colors mein ho:
```
🔴 Exit
🟢 Add User  
🟡 View List
```

## All Colors List (Copy-Paste Ready)
```python
print("Colors:")
print(Fore.RED + "RED" + Style.RESET_ALL)
print(Fore.GREEN + "GREEN" + Style.RESET_ALL)
print(Fore.YELLOW + "YELLOW" + Style.RESET_ALL)
print(Fore.BLUE + "BLUE" + Style.RESET_ALL)
print(Fore.MAGENTA + "MAGENTA" + Style.RESET_ALL)
print(Fore.CYAN + "CYAN" + Style.RESET_ALL)
print(Fore.WHITE + "WHITE" + Style.RESET_ALL)
```

**Pro Tip**: IDE mein (VSCode, PyCharm) colors perfect dikhte hain. Terminal mein bhi kaam karega.

Test karo aur batao! Next kya sikhe? [stackoverflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)

# 1️⃣ Colorama Advanced Colors & Mixed Text

## 2️⃣ Complete Colorama Colors List

**Colorama mein 8 Basic Colors + Background + Styles**:

**Foreground (Text Colors)**:
```
Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW
Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
```

**Background Colors**:
```
Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW
Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE
```

**Styles** (Bold, Dim, etc.):
```
Style.DIM, Style.NORMAL, Style.BRIGHT, Style.RESET_ALL
```

**Total**: 8 Fore + 8 Back + 4 Styles = **20+ combinations**

## 3️⃣ Mixed Colors in Same Line (Word-by-Word)

**Different words different colors** - **Multiple times RESET karo**!

```python
from colorama import init, Fore, Back, Style
init()

# Mixed colors in ONE line
print(Fore.RED + "ERROR:" + Style.RESET_ALL + 
      Fore.GREEN + " Login " + Style.RESET_ALL + 
      Fore.YELLOW + "successful!" + Style.RESET_ALL)

# Background example
print(Fore.WHITE + Back.RED + " ALERT " + Style.RESET_ALL + 
      "High CPU usage!")

# Bold + Color
print(Style.BRIGHT + Fore.CYAN + "SUCCESS" + Style.RESET_ALL + 
      " User created")
```

**Output**:
```
ERROR: (Red) Login (Green) successful! (Yellow)
 ALERT (White on Red) High CPU usage!
SUCCESS (Bright Cyan) User created
```

**Rule**: Har color change ke baad `Style.RESET_ALL` lagao, warna next word bhi wahi color rahega!

## 4️⃣ Advanced Example: Professional Logger

```python
from colorama import init, Fore, Back, Style
init()

def colored_print(message_type, message):
    if message_type == "SUCCESS":
        print(Fore.GREEN + "✅ " + message + Style.RESET_ALL)
    elif message_type == "ERROR":
        print(Fore.RED + Back.WHITE + "❌ " + message + Style.RESET_ALL)
    elif message_type == "WARNING":
        print(Style.BRIGHT + Fore.YELLOW + "⚠️ " + message + Style.RESET_ALL)
    elif message_type == "INFO":
        print(Fore.CYAN + "ℹ️ " + message + Style.RESET_ALL)

# Usage
colored_print("SUCCESS", "Database connected")
colored_print("ERROR", "File not found")
colored_print("WARNING", "Low disk space")
colored_print("INFO", "Processing 50/100 files")
```

## 5️⃣ Other Packages (Simple Comparison)

| Package | Pros | Cons | Install |
|---------|------|------|---------|
| **Colorama** | ✅ Windows support, Simple, Fast | Basic 8 colors | `pip install colorama` |
| **Rich** | 🎨 256 colors, Tables, Progress bars | Heavy (slow startup) | `pip install rich` |
| **Termcolor** | Simple | No Windows | `pip install termcolor` |

**Rich Example** (Extra Fancy):
```python
from rich.console import Console
console = Console()

console.print("[bold green]Success![/bold green]")
console.print("[red]Error[/red] [blue]with[/blue] [yellow]colors[/yellow]")
```

## 6️⃣ Practice: Mixed Color Menu

```python
# Create colored menu
print(Fore.CYAN + "🎮 GAME MENU" + Style.RESET_ALL)
print(Fore.GREEN + " [stackoverflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)" + Style.RESET_ALL + " Play")
print(Fore.YELLOW + " [geeksforgeeks](https://www.geeksforgeeks.org/python/print-colors-python-terminal/)" + Style.RESET_ALL + " Score")
print(Fore.RED + "[3]" + Style.RESET_ALL + " Exit")
```

**Exercise**: Status bar banao:
```
CPU: [Green 45%] RAM: [Yellow 78%] Disk: [Red 95%]
```

## 7️⃣ Complete Colors Cheat Sheet

```python
from colorama import Fore, Back, Style

colors = {
    'red': Fore.RED, 'green': Fore.GREEN, 'yellow': Fore.YELLOW,
    'blue': Fore.BLUE, 'magenta': Fore.MAGENTA, 'cyan': Fore.CYAN,
    'white': Fore.WHITE, 'black': Fore.BLACK
}

for name, color in colors.items():
    print(color + f" {name.upper()} " + Style.RESET_ALL)
```

**Colorama hi best hai beginners ke liye** - simple aur powerful!

<!-- Koi doubt? Screenshot bhejo output ka! [stackoverflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal) -->