# Holberton School - 0x0A-python-inheritance

## Description

The focus of this project is to learn:
* what the differencea are  between a superclass, baseclass and parentclass
* what a subclass is
* how to list all attributes and methods of a class or instanec
* when an instance can have new attributes
* how to inherit one class from another
* how to define a class with multiple base classes
* what the default class every class inherits from
* how to override a method or attribute inherited from the base class
* which attributes or methods are available by heritage or subclasses
* what the purpose of inheritance is
* when and how to use what the `isinstance`, `isubsclass`, `type` and `super` built-ins functions

## Environment
* __Environment:__ Ubuntu 14.04 LTS
* __python3 version:__ 3.4.3
* __style:__ PEP 8

## Documentation
* module documentation: `print(__import__("my_module".__doc__)`
* class documentation: `print(__import__("my_module").MyClass.__doc__)`
* class function documentation: print(`__import__("my_module").MyClass.__doc__).my_functions.__doc__`
* global  function documentation: `print(__import__("my_module").my_function.__doc__)


## New concepts / functions / commands used:
``TODO``:

## Helpful Links
* https://docs.python.org/3.4/tutorial/classes.html#inheritance
* https://docs.python.org/3.4/tutorial/classes.html#multiple-inheritance
* https://www.packtpub.com/books/content/inheritance-python
* http://t3.gstatic.com/images?q=tbn:ANd9GcQUM0y6bxv-QJg-5SvHrf-HBUBTaid1QFxl_gJtGZisbziNydzn

## File Descriptions
`0-lookup.py`: returns a list of available attributes and methods of an object
`1-my_list.py`: class `MyList` that inherits from `list`
`2-is_same_class.py`: determines if an object is exactly an instance of the specified class
`3-is_kind_of_class.py`: determines if an object is an instance of a specified class or is a class instance that inherited from the specified class
`4-inherits_from.py`: determines if an object is an instance of a class that inherited (directl\
      y or indirectly) from the speciied class
`5-base_geometry.py`: empty class BaseGeometry
`6-base_geometry`: raises an `Exception` with the message "area() is not implemented"
`7-base_geometry.py`: function `integer_validator()`: raises `TypeError` execption "<name> must be greater than 0" if `value` is not an integer
`8-rectangle.py`: class `Rectangle` that inherits from `BaseGeometry`
`9-rectangle.py`: returns the rectangle description: [Rectangle] <`width`>/<`height`>
`10-square.py`: inherits from `Rectangle`
`11-square.py`: returns the square desciption: [`Square`] <`width`>/<`height`>

## Author
Stuart Kuredjian

twitter: @stueygk

linkdin: https://www.linkedin.com/in/stuart-kuredjian-8100a273/

## License
Public Domain, no copyright protection