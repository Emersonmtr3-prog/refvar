# refvar

A lightweight and dependency-free reactive variable system for Python.  
`refvar` allows you to store simple values and automatically execute callbacks whenever the value changes.

Ideal for small applications, state control, or simple reactive patterns — without requiring any frameworks.

---

## 🚀 Features

- Reactive reference variable (`Ref`)
- Callbacks automatically triggered on value change
- Extremely lightweight (< 50 lines)
- Zero dependencies
- Clean and intuitive API:
  - `ref(value)`
  - `ref(new_value)` to update
  - `.get()`, `.set()`, `.bind()`, `.unbind()`
- Safe by design — supports **only simple types**

---

## ⚠ Supported Types

`Ref` is intentionally limited to **immutable simple values**:

- `str`
- `int`
- `float`
- `bool`
- `None`

This prevents unexpected behavior with mutable objects.

### ❌ Not recommended for:

- `list`
- `dict`
- `set`
- custom classes
- functions
- anything mutable

If you need full reactive programming, use a framework —  
`refvar` is specifically designed for lightweight use.

---

## 📦 Installation

```bash
pip install refvar
```

---

## 🔧 Usage

### Basic Example

```python
from refvar import Ref

x = Ref(10)

def on_change(ref, new_value):
    print("Value changed to:", new_value)

x.bind(on_change)

x(20)   # Updates the value and triggers the callback
print(x.value)  # 20

