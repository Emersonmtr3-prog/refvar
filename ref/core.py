class Ref:
    """
    A lightweight reactive variable for simple immutable types.
    Supports automatic callback execution whenever its value changes.
    Ideal for state tracking in Python applications.
    """

    __slots__ = ("value", "callbacks")

    SIMPLE_TYPES = (str, int, float, bool, type(None))

    def __init__(self, value=None):
        if not isinstance(value, self.SIMPLE_TYPES):
            raise TypeError("Ref supports only: str, int, float, bool, or None.")
        self.value = value
        self.callbacks = set()

    def __call__(self, new_value):
        """Updates the value like a function call: ref(new_value)."""
        self.set(new_value)
        return self

    def set(self, new_value):
        if not isinstance(new_value, self.SIMPLE_TYPES):
            raise TypeError("Ref supports only: str, int, float, bool, or None.")

        for callback in self.callbacks:
            callback(self, new_value)

        self.value = new_value
        return self

    def get(self):
        """Returns the current stored value."""
        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Ref({self.value!r})"

    def __eq__(self, other):
        return self.value == other

    def __bool__(self):
        return bool(self.value)

    def bind(self, callback):
        """
        Registers a callback.
        Callback signature: callback(ref, old_value, new_value)
        """
        self.callbacks.add(callback)
        return callback

    def unbind(self, callback):
        self.callbacks.discard(callback)
        return callback
