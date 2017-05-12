#!/usr/bin/python3
import sys

# safe_function - executes a function safely
# fct: function to be executed
# args: arguments to be passed to function
# Return: result of the function


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
