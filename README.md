# Polygon Area Calculator

A Python project built as part of the **freeCodeCamp Python Certification**, demonstrating object-oriented programming (OOP) concepts through Rectangle and Square classes.

## Features

- Calculate the area, perimeter, and diagonal of rectangles and squares.
- Update the dimensions of shapes.
- Display shapes using `*` characters.
- Calculate how many smaller shapes fit inside a larger shape.
- Reuse code through inheritance.

## Technologies

- Python 3
- Object-Oriented Programming (OOP)

## OOP Concepts Practiced

- **Classes and Objects:** Creating Rectangle and Square objects.
- **Inheritance:** The Square class inherits from Rectangle.
- **Method Overriding:** Square customizes inherited methods.
- **`super()`:** Reuses the Rectangle constructor.
- **Magic Methods:** Uses `__init__()` and `__str__()`.

## Example Usage

```python
rect = Rectangle(10, 5)
print(rect.get_area())       # 50
print(rect.get_perimeter())  # 30

sq = Square(4)
print(sq.get_area())         # 16
print(sq)                    # Square(side=4)
```

## What I Learned

This project helped me practice Python classes, inheritance, method overriding, and using object-oriented programming to organize and reuse code.
