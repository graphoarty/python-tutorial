'''

1. INTRODUCTION TO PYTHON


IDENTIFIERS

    - Identifiers are names given to entities like variable, functions, classes etc.

    - Python is case-sensitive.

    - Python is a dynamically-typed and weakly or duck-typed language

        - In dynamically-typed languages, it is possible to bind a name to objects of different types during the execution of the program.

        - A weakly-typed language has looser typing rules.

    - Rules to define an Identifier.

        - Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). Ex. jackieChan, super_man_123, 

        - An identifier cannot start with a digit. 1Love is not a valid identifier.

        - The Keywords or Reserved Word below cannot be used as identifiers.

            - and, as, assert, async, await, break, class, continue, def, del, elif, else, except, exec, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, print, raise, return, True, try, while, with, yield

    Things to Rememeber: 

    - When defining an Identifier, do you fellow programmers a favour and use descriptive names. Don't use c where you can write count and don't use a where you can write num1. 

    - Use either camel-casing or underscore seperation.

    - identifiers, keywords, literals, operators, and delimiters

LINES AND INDENTATION

    - Python uses whitespace indentation, rather than curly brackets or keywords, to indicate blocks.

    - Both space characters and tab characters are currently accepted as forms of indentation, but do not mix them.

    >>> def foo(x):
    ... if x == 0:
    ...     bar()
    ...     baz()
    ... else:
    ...     qux(x)
    ...     foo(x - 1)

    VS

    >>> def foo(x):
    ... if x == 0:
    ...    bar()
    ...     baz()
    ... else:
    ...     qux(x)
    ... foo(x - 1)

MULTI-LINE STATEMENTS

    - Usually, every Python statement ends with a newline character. However, we can extend it over to multiple lines using the line continuation character (\).

    - Explicit Line Continuation
        
        - Using the Continuation character (\) to split a statement into multiple lines.

        >>> eval ( \
        ... " 2.5 \
        ... + \
        ... 3.5")
        6.0

    - Implicit Line Continuation

        - Spliting a statement using either of parentheses ( ), brackets [ ] and braces { }. You need to enclose the target statement using the mentioned construct.

        >>> subjects = [
        ... 'Maths',
        ... 'English',
        ... 'Science'
        ... ]
        >>> print(subjects)
        ['Maths', 'English', 'Science']

COMMENTS

    - A comment is a programmer-readable explanation or annotation in the source code of a computer program. 

    - They are added with the purpose of making the source code easier for humans to understand, and are generally ignored by compilers and interpreters.

    - Single-line comments are created simply by beginning a line with the hash (#) character, and they are automatically terminated by the end of line. Ex. 

    >>> # This would be a comment in Python
 
    - Comments that span multiple lines – used to explain things in more detail – are created by adding a delimiter (""") on each end of the comment.

    >>> """ This would be a multiline comment
    ... in Python that spans several lines and
    ... describes your code, your day, or anything you want it to
    ... …
    ... """ 

PRINTING TO THE CONSOLE WITH print()

    - The print function prints objects to the console by defualt but you can also change it's functionality to do other things.

    >>> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

    - Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.

GETTING INPUT FROM THE USER WITH raw_input() / input

    - Python provides the function input() and raw_input() to take input from the user by stopping the programs control flow. 
    
    -In Python 3, input() is now eval(input()) and raw_input() is now input().

COMMAND LINE ARGUMENTS

    - sys.argv contains the list of command-line arguments passed to the Python program.

    - To use it, we first have to import the sys module (import sys).

    - The first argument, sys.argv[0], is always the name of the program as it was invoked. sys.argv[1] is the first argument you pass to the program and so on and so forth.

    >>> import sys
    ... program_name = sys.argv[0]
    ... arguments = sys.argv[1:]
    ... count = len(arguments)

standard data types

    basic
    
    none
    
    boolean (true & False)
    
    numbers
    
    Python strings
    
    data type conversion
    
    Python basic operators (Arithmetic
    
        comparision
        
        assignment
        
        bitwise logical)
        
        Python membership operators (in & not in)
        
        Python identity operators (is & is not)
        
        Operator precedence
    
    Control Statements

Python loops

    Iterating by subsequence index
    
    loop control statements (break
    
    continue
    
    pass
    
Mathematical functions and constants (import math)
    
Random number functions


'''