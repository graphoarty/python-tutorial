'''

1. INTRODUCTION TO PYTHON (https://docs.python.org/3/tutorial/)

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

STANDARD DATA TYPES

    BASIC - Numbers, Booleans and Strings
    
    Numbers
    
        - Python has integers and floats. Integers are simply whole numbers, like 314, 500, and -716.

        - Floats, meanwhile, are fractional numbers like 3.14, 2.867, 76.88887. 
        
        - You can use the type method to check the value of an object.

        >>> type(3)
        <class 'int'>
        >>> type(3.14)
        <class 'float'>
        >>> pi = 3.14
        >>> type(pi)
        <class 'float'>

    Booleans

        - Boolean values are simply True or False.

    Strings

        - Strings are basically a sequence of characters like a letter, a number, or a backslash.

        - Python recognizes single and double quotes as the same thing, the beginning and end of the strings.

        >>> "This is a string with double quotes."
        'This is a string with double quotes.'
        >>> 'This is a string with single quotes.'
        'This is a string with single quotes.'

        - Use escape sequences to make the quotes inside the string to not be confused by Python as the end of the string.

        >>> "He said \"no\" to me"
        'He said "no" to me'

        - You can concatenate strings with the + operator.

        - The string is an object so you can use the built-in functions like upper(), lower(), replace(), and count().

        - You can also format strings with the format() method.

        >>> "{0} is a lot of {1}".format("Python", "fun!")
        'Python is a lot of fun!'
    
    DATA TYPE CONVERSION

        - Python defines type conversion functions to directly convert one data type to another.

        - int(x, base=10) : Return an integer object constructed from a number or string x with the base, or return 0 if no arguments are given.

        - float([x]) : Return a floating point number constructed from a number or string x.

        - Other conversions: 
            
            - ord() : character to integer
            - hex() : integer to hexadecimal string
            - oct() : integer to octal string
    
    OPERATORS

        - Operators are the constructs which can manipulate the value of operands.
        
        Arithmetic Operators

            - Addition (+)
            - Subtraction (-)
            - Multiplication (*)
            - Division (/)
            - Modulus (%)
            - Exponent (**)
            - Floor Division (//)
    
        Comparision Operators

            - Equals to (==)
            - Not Equals to (!=, <>)
            - Greater than (>)
            - Less than (<)
            - Greater than or equal to (>=)
            - Less than or equal to (<=)
        
        Assignment Operators

            - Right to Left Assignment (=)
            - Addition and Right to Left Assignment (+=)
            - Subtraction and Right to Left Assignment (-=)
            - Division and Right to Left Assignment (/=)
            - Modulus and Right to Left Assignment (%=)
            - Exponent and Right to Left Assignment (**=)
            - Floor Division and Right to Left Assignment (//=)
        
        Bitwise Operators

            - Binary AND (&)
            - Binary OR (|)
            - Binary XOR (^)
            - Binary Ones (~)
            - Binary Left Shift (<<)
            - Binary Right Shift (>>)
        
        Logical Operators

            - and Logical AND	
            - or Logical OR
            - not Logical NOT
        
        Python Membership Operators (in & not in)
        
            - Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.

            - Evaluates to true if it finds a variable in the specified sequence and false otherwise. (in)

            - Evaluates to true if it does not finds a variable in the specified sequence and false otherwise. (not in)

        Python Identity Operators (is & is not)
        
            - Identity operators compare the memory locations of two objects.

            - Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. (is)

            - Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. (is not)

        Operator Precedence

            - Python interpreter evaluates operators with higher precedence first.

            - Associativity is the rule which denotes what direction the expression gets evaluated in if all the operators are of the same precedence.

            - Except the exponent operator (**) all other operators get evaluated from left to right associative.

            - Parentheses () overriding the precedence of the operators.
    
            - Assignment Operators and Comparison Operators which don’t support associativity.

    If...elif...else...

        - The control flow evaluates the condition and will execute the if block is it is True or execute the else block if it is False.

        if condition:
            statement
        
        if condition:
            statement1
        else:
            statement2

        - The control flow check the elif condition and executes its code block is it is True.

        if condition:
            statement1
        elif condition:
            statement2
        elif condition:
            statement3
        else:
            statement4

        - We can also form nested if else blocks.

Loops

    - For Loop

        - A for loop is used for iterating over a sequence (that is either a list, a tuple or a string).

        >>> fruits = ["apple", "banana", "cherry"]
        ... for x in fruits:
        ...     print(x)
    
        - The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

        >>> for x in range(0, 6):
        ...     print(x)

    - While Loop

        - The while loop we can execute a set of statements as long as a condition is True.

        while condition:
            code block

        >>> i = 1
        ... while i < 6:
        ...     print(i)
        ...     i += 1

    LOOP CONTROL STATEMENTS 
        
        break
        
            - With the break statement we can stop the loop even if the while condition is true:

                >>> i = 1
                ... while i < 6:
                ... print(i)
                ... if i == 3:
                ...     break
                ... i += 1

        continue

            - With the continue statement we can stop the current iteration, and continue with the next:

            >>> i = 0
            ... while i < 6:
            ...   i += 1 
            ...   if i == 3:
            ...     continue
            ...   print(i)
            
        pass

            - It is used when a statement is required syntactically but you do not want any command or code to execute.

            - The pass statement is a null operation; nothing happens when it executes.
    
MATHEMATICAL FUNCTION AND CONSTANTS FROM IMPORT MATH
    
    - This module is always available. It provides access to the mathematical functions defined by the C standard.

    - https://docs.python.org/3/library/math.html

RANDOM NUMBER FUNCTIONS

    - This module implements pseudo-random number generators for various distributions.

    - https://docs.python.org/3/library/random.html

    - pseudo-random : satisfying one or more statistical tests for randomness but produced by a definite mathematical procedure.


'''