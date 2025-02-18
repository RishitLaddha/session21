class AdvancedNumber:
    def __init__(self, value):
        """
        Initialize the AdvancedNumber instance.
        
        Args:
            value (int or float): The numerical value to store.
            
        Raises:
            ValueError: If the value is not an int or float.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("AdvancedNumber only accepts int or float values")
        self.value = value

    def __str__(self):
        """
        Return a human-readable string representation of the object.
        Called by str() and print().
        """
        return f"Value: {self.value}"

    def __repr__(self):
        """
        Return an unambiguous string representation of the object.
        Helpful for debugging. Also prints a message when called.
        """
        print('__repr__ called')
        return f"AdvancedNumber({self.value})"

    # ---------- Helper Method ----------
    def _get_value(self, other):
        """
        Extract the numerical value from the other operand.
        
        If 'other' is an instance of AdvancedNumber, returns its value.
        If 'other' is a plain int or float, returns it directly.
        Otherwise, returns NotImplemented.
        
        Args:
            other: Another AdvancedNumber or a numeric type.
            
        Returns:
            int or float or NotImplemented.
        """
        if isinstance(other, AdvancedNumber):
            return other.value
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    # ---------- Arithmetic Operators ----------
    def __add__(self, other):
        """
        Overload the addition operator.
        
        Supports AdvancedNumber + AdvancedNumber and AdvancedNumber + number.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return AdvancedNumber(self.value + other_val)

    def __radd__(self, other):
        """
        Right-hand addition supports number + AdvancedNumber.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Overload the subtraction operator.
        
        Supports AdvancedNumber - AdvancedNumber and AdvancedNumber - number.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return AdvancedNumber(self.value - other_val)

    def __rsub__(self, other):
        """
        Right-hand subtraction supports number - AdvancedNumber.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return AdvancedNumber(other_val - self.value)

    def __mul__(self, other):
        """
        Overload the multiplication operator.
        
        Supports AdvancedNumber * AdvancedNumber and AdvancedNumber * number.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return AdvancedNumber(self.value * other_val)

    def __rmul__(self, other):
        """
        Right-hand multiplication supports number * AdvancedNumber.
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Overload the division operator.
        
        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        if other_val == 0:
            raise ZeroDivisionError("division by zero")
        return AdvancedNumber(self.value / other_val)

    def __rtruediv__(self, other):
        """
        Right-hand division supports number / AdvancedNumber.
        
        Raises:
            ZeroDivisionError: If the AdvancedNumber's value is zero.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        if self.value == 0:
            raise ZeroDivisionError("division by zero")
        return AdvancedNumber(other_val / self.value)

    def __mod__(self, other):
        """
        Overload the modulo operator.
        
        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        if other_val == 0:
            raise ZeroDivisionError("Modulo by zero")
        return AdvancedNumber(self.value % other_val)

    def __rmod__(self, other):
        """
        Right-hand modulo supports number % AdvancedNumber.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        if self.value == 0:
            raise ZeroDivisionError("Modulo by zero")
        return AdvancedNumber(other_val % self.value)

    # ---------- Comparison Operators ----------
    def __eq__(self, other):
        """
        Overload equality operator.
        
        Returns True if the stored values are equal.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return self.value == other_val

    def __lt__(self, other):
        """
        Overload the less-than operator.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return self.value < other_val

    def __le__(self, other):
        """
        Overload the less-than-or-equal-to operator.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return self.value <= other_val

    def __gt__(self, other):
        """
        Overload the greater-than operator.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return self.value > other_val

    def __ge__(self, other):
        """
        Overload the greater-than-or-equal-to operator.
        """
        other_val = self._get_value(other)
        if other_val is NotImplemented:
            return NotImplemented
        return self.value >= other_val

    def __ne__(self, other):
        """
        Overload the not-equal-to operator.
        """
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq

    # ---------- Hashing and Boolean Conversion ----------
    def __hash__(self):
        """
        Make the AdvancedNumber hashable.
        Uses the hash of its stored numeric value.
        """
        return hash(self.value)

    def __bool__(self):
        """
        Define the truth value of the object.
        Returns True if the stored value is non-zero.
        """
        return bool(self.value)

    # ---------- Callable Behavior ----------
    def __call__(self):
        """
        Make the object callable.
        When called, it returns the square of the stored value.
        """
        return self.value ** 2

    # ---------- Custom Formatting ----------
    def __format__(self, format_spec):
        """
        Support custom string formatting.
        
        - If the format_spec ends with 'x' (or '#x') and the value is an integer,
          return the hexadecimal representation.
        - Otherwise, delegate to the built-in format for numbers.
        
        Args:
            format_spec (str): The format specification.
        
        Returns:
            str: The formatted string.
        """
        # Check for hexadecimal formatting: support both "x" and "#x"
        if format_spec.endswith('x'):
            # Remove '#' if present
            spec = format_spec.lstrip('#')
            if isinstance(self.value, int):
                return hex(self.value)
        # Fallback: use the standard format function.
        try:
            formatted = format(self.value, format_spec)
        except Exception:
            formatted = str(self.value)
        return formatted

    # ---------- Destructor ----------
    def __del__(self):
        """
        Destructor called when the object is about to be destroyed.
        Prints a message indicating the object's destruction.
        """
        print(f"AdvancedNumber with value {self.value} is being destroyed")
