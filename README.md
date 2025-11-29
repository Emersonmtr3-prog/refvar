# refvar

`refvar` is a lightweight and reactive library for reference management in Python. It allows you to create mutable references to immutable types (such as `str`, `int`, `bool`) that can be shared across multiple modules and updated centrally.

The main goal is to solve the problem where importing simple variables into different files loses the link to the original value. Additionally, the library supports **callbacks**, allowing functions to be executed automatically whenever the value changes.

---

## 🚀 Features

- Reactive variable (`Ref`)
- Callbacks triggered automatically when the value changes
- Extremely lightweight (< 50 lines)
- Zero dependencies
- Simple and intuitive API:

- `ref(value)`

- `ref(new_value)` `.set()` to update

- `ref()` `.get()` to retrieve the content

- `.bind()` `.unbind()` to call a function

- Safe by design — supports **only simple types**

---

## ✨ Features

- **Single Source of Truth:** Pass variables between modules without losing the reference.

- **Reactivity:** "Bind" callbacks that trigger when the value is updated.

- **Pythonic Syntax:** Implements magic methods (`__call__`, `__eq__`, `__bool__`, `__str__`) for intuitive use.

- **Lightweight:** Uses `__slots__` for high memory efficiency.

---

## ✅ Recommended Types

`Ref` is recommended for **simple and immutable values**:

- `str`

- `int`

- `float`

- `bool`

- `None`

This avoids unexpected behavior with mutable objects.

## ⚠️ Not recommended for:

- `list`

- `dict`

- `set`

- custom classes
- functions
- anything mutable

If you need full reactive programming, use a framework —
`refvar` was specifically designed to be lightweight and simple.

---

## 📦 Installation

```bash
pip install refvar
```

---

## 🔧 Usage Example

### Basic Example

```python
from refvar import Ref

x = Ref(10)

def on_change(ref, new_value):

print("Value changed to:", new_value)

x.bind(on_change)

x(20) # Updates the value and triggers the callback

value = x()
print(value, type(value)) # 20 <class 'int'>

value = x.get()
print(value, type(value)) # 20 <class 'int'>

value = x
print(value, type(value)) # 20 <class 'ref.core.Ref'>