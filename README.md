[![Python Tests](https://github.com/RishitLaddha/session21/actions/workflows/python-tests.yml/badge.svg)](https://github.com/RishitLaddha/session21/actions/workflows/python-tests.yml)

<img width="1225" alt="Screenshot 2025-02-19 at 00 11 59" src="https://github.com/user-attachments/assets/102119de-2a84-4171-9b38-f2269a2671ae" />

# AdvancedNumber Class Documentation

The **AdvancedNumber** class is designed as a custom numerical type that exhibits a rich set of behaviors through operator overloading and special methods. The primary goal was to create a class that could seamlessly interact with standard numbers (integers and floats) while providing enhanced functionality. This document describes what was expected, the features that were implemented, and how these features work under the hood.

---

## Overview

The **AdvancedNumber** class encapsulates a numeric value and extends its functionality with advanced operator overloading, custom formatting, and additional behaviors such as being callable. The class is built to be robust, user-friendly, and integrate naturally with Python’s built-in operators and functions. Its design encourages code reuse and consistency in numeric operations while ensuring that instances behave as expected in a variety of contexts.

---

## Expected Functionality

Developers were tasked with implementing a class that meets the following requirements:

1. **Numeric Encapsulation and Representation:**
   - The class should store an integer or a float and provide access to the numeric value through a property.
   - Two string representations are required: one for developers (an unambiguous representation) and one for users (a human-friendly message).

2. **Arithmetic Operations:**
   - The class should support standard arithmetic operators such as addition, subtraction, multiplication, division, and modulo.
   - The implementation should allow operations with another instance of the class as well as with plain numbers.
   - Reverse operations should be supported so that the class can be used seamlessly even when the custom type is on the right-hand side of an arithmetic expression.

3. **Comparison Operators:**
   - The class must support equality, inequality, less-than, greater-than, and their corresponding or-equal-to variants.
   - Comparisons should work correctly when comparing an instance with another instance or a plain number.

4. **Hashing and Boolean Conversion:**
   - AdvancedNumber instances should be hashable, enabling their use in sets and as keys in dictionaries.
   - Boolean conversion must reflect the truthiness of the encapsulated value (zero should be considered `False` while any non-zero value is `True`).

5. **Callable Behavior:**
   - Instances should be callable, with the call operation returning the square of the stored numeric value.

6. **Custom Formatting:**
   - The class supports custom string formatting directives. For example, a format specifier for fixed-point notation or hexadecimal representation (if the stored value is an integer) should be implemented.
   - The implementation should intelligently choose the appropriate formatting behavior based on the type and format specifier.

7. **Destructor Behavior:**
   - When an instance of the class is about to be destroyed, it should output a message indicating that the instance is being removed from memory.

---

## Implementation Details

### Data Encapsulation and Property

The class stores the numeric value internally and exposes it through a property. This approach ensures that any future modifications to the internal storage (such as adding validation or logging) can be handled without affecting the external interface. The constructor verifies that the given value is of an acceptable numeric type (either an integer or a float). If an invalid type is provided, an exception is raised.

### String Representations

Two key methods, `__str__` and `__repr__`, provide the string representations:

- **Human-Readable Format (`__str__`):**  
  This method returns a simple string that identifies the stored value. It is intended for display purposes, such as printing to the console.

- **Developer-Friendly Format (`__repr__`):**  
  This method returns a more detailed string that can be used for debugging. It prints a message indicating when it is called and shows the value in a clear format that can be used to recreate the instance if necessary.

### Arithmetic Operations

The class implements standard arithmetic operations. Each arithmetic method follows a common pattern:
  
- A helper function extracts the numeric value from either an instance of **AdvancedNumber** or a plain numeric type.  
- Once the numeric value is determined, the corresponding arithmetic operation (addition, subtraction, etc.) is performed on the internal value.
- A new instance of **AdvancedNumber** is created with the result, ensuring that all operations return an instance of the same class.

Reverse operators (for example, when the custom type appears on the right-hand side of the expression) are also provided. This means that expressions like `2 + AdvancedNumber(3)` work as intended. Each reverse operator simply delegates to the corresponding standard operator by swapping the order of operands.

### Division and Modulo with Error Handling

Special care is taken in the division and modulo methods. These methods check for division by zero and raise the appropriate Python error if necessary. By doing so, the class mirrors the behavior of Python’s built-in numeric types, ensuring consistency and predictability.

### Comparison Methods

Comparison operators are overloaded so that **AdvancedNumber** can be compared not only with other instances but also with plain numbers. The methods implement equality (`==`), inequality (`!=`), less-than (`<`), less-than-or-equal-to (`<=`), greater-than (`>`), and greater-than-or-equal-to (`>=`). When an unsupported type is encountered during comparison, the methods return the special value `NotImplemented`, allowing Python to try alternative comparison methods or raise an appropriate error.

### Hashing and Boolean Conversion

To make the class hashable, the `__hash__` method is implemented to use the hash of the underlying numeric value. This allows instances to be used in sets or as dictionary keys, provided that their value does not change over their lifetime.

The boolean conversion method, `__bool__`, simply returns the truth value of the numeric value. This means that an instance with a value of zero is treated as `False`, and any non-zero value is treated as `True`.

### Callable Instances

The `__call__` method is defined so that instances of **AdvancedNumber** can be called as if they were functions. When an instance is invoked, it returns the square of the stored numeric value. This behavior adds another layer of functionality and demonstrates the flexibility provided by operator overloading.

### Custom Formatting

The **AdvancedNumber** class implements the `__format__` method to support custom formatting instructions. Depending on the format specifier passed:

- If the specifier requests a fixed-point format (e.g., using the `.2f` pattern), the numeric value is formatted accordingly.
- If the specifier indicates hexadecimal formatting (for instance, `#x`), the method converts the value to its hexadecimal representation, assuming the value is an integer.
- In other cases, the built-in formatting function is used as a fallback.

This flexibility allows users to convert instances to strings in various ways, depending on the context in which they are used.

### Destructor Behavior

The destructor method, `__del__`, prints a message when an instance is about to be destroyed. This behavior is useful for debugging purposes or for understanding the lifecycle of objects within a program. It provides insight into when resources are being freed and ensures that cleanup messages are displayed, though in production code, resource management is typically handled through context managers rather than relying on destructors.

---

## Conclusion

The **AdvancedNumber** class meets the design goals by providing a robust and flexible numerical type. It seamlessly integrates with Python’s arithmetic, comparison, and formatting functionalities while extending them to provide additional behaviors such as callable instances and a clear destructor message.

Each aspect of the class—from initialization and type-checking to operator overloading and custom formatting—was implemented with careful attention to detail. The design choices ensure that the class is both powerful and easy to use, making it a useful component in any system that requires enhanced numerical types.

This documentation should provide a clear understanding of what was expected, how each requirement is fulfilled, and the overall architecture of the **AdvancedNumber** class. The implementation is designed to be as intuitive as possible while demonstrating advanced features of Python’s object-oriented programming model.
