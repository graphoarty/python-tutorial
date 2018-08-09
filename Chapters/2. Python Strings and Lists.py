'''

Strings

    - Use escape sequences to make the quotes inside the string to not be confused by Python as the end of the string.

    >>> "He said \"no\" to me"
    'He said "no" to me'

    - You can concatenate strings with the + operator.

    - The string is an object so you can use the built-in functions like upper(), lower(), replace(), and count().

    - Strings are immuatable.

    - You can also format strings with the format() method.

    >>> "{0} is a lot of {1}".format("Python", "fun!")
    'Python is a lot of fun!'

    CONCEPT 

        - Strings are basically a sequence of characters like a letter, a number, or a backslash.

        - Python recognizes single and double quotes as the same thing, the beginning and end of the strings.

        >>> "This is a string with double quotes."
        'This is a string with double quotes.'
        >>> 'This is a string with single quotes.'
        'This is a string with single quotes.'

    SLICING

        - Like the list data type that has items that correspond to an index number, each of a string’s characters also correspond to an index number, starting with the index number 0.

        - By referencing index numbers, we can isolate one of the characters in a string.

        - If we have a long string and we want to pinpoint an item towards the end, we can also count backwards from the end of the string, starting at the index number -1.

        - We can call multiple character values by creating a range of index numbers separated by a colon [x:y] (substring)

        - A third parameter ([x:y:z]) specifies the stride, which refers to how many characters to move forward after the first character is retrieved from the string.

    ESCAPE CHARACTERS

        - An escape character gets interpreted; in a single quoted as well as double quoted strings.

        - http://2.bp.blogspot.com/-kJ7klu4Mm3I/TydMU62aH8I/AAAAAAAAFeY/G3OLkYJeSE0/s1600/table6-1.JPG

    STRING SPECIAL OPERATOR

        - https://www.tutorialspoint.com/python3/python_strings.htm

    STRING FORMATTING OPERATOR

        - https://www.tutorialspoint.com/python3/python_strings.htm

    TRIPLE QUOTES

        - https://www.tutorialspoint.com/python3/python_strings.htm

    Raw String

        - https://www.tutorialspoint.com/python3/python_strings.htm

    Unicode strings

        - https://www.tutorialspoint.com/python3/python_strings.htm

    Built-in String methods

        - https://www.tutorialspoint.com/python3/python_strings.htm

Lists

    CONCEPT

        - A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. 
        
        - Each element or value that is inside of a list is called an item. 

    CREATING AND ACCESSING LISTS

        - Just as strings are defined as characters between quotes, lists are defined by having comma-seperated values between square brackets [ ].

        - To access values in lists, use the square brackets along with the index to obtain value available at that index.
    
    UPDATING AND DELETING LISTS

        - You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator.

        - You can add to elements in a list with the append() method.

        - You can use either the del statement if you know exactly which element(s) you are deleting or you can use the remove() method if you do not know exactly which items to delete.
    
    BASIC LIST OPERATORS

        - https://www.tutorialspoint.com/python3/python_lists.htm
    
    REVERSE

        - https://www.tutorialspoint.com/python3/list_reverse.htm
    
    INDEXING, SLICING, MATRICES

        - https://www.tutorialspoint.com/python3/python_lists.htm

    BUILT-IN LIST FUNCTIONS

        - Lambda Functions: The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created.

        >>> sum = lambda x, y : x + y
        >>> sum(3,4)
        7

        map()

            - map() is a function which takes two arguments: 

                r = map(func, seq)

            - The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq.

            >>> def fahrenheit(T):
            ...     return ((float(9)/5)*T + 32)
            ...
            >>> def celsius(T):
            ...     return (float(5)/9)*(T-32)
            ...
            >>> temperatures = (36.5, 37, 37.5, 38, 39)
            >>> F = map(fahrenheit, temperatures)
            >>> C = map(celsius, temperatures)

            - map() used to return a list, where each element of the result list was the result of the function func applied on the corresponding element of the list or tuple "seq".

            or we can use the Lamba Version of this function...

            >>> C = [39.2, 36.5, 37.3, 38, 37.8] 
            >>> F = list(map(lambda x: (float(9)/5)*x + 32, C))
            >>> print(F)
            [102.56, 97.7, 99.14, 100.4, 100.03999999999999]
            >>> C = list(map(lambda x: (float(5)/9)*(x-32), F))
            >>> print(C)
            [39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]

        filter()
        
            - The function offers an elegant way to filter out all the elements of a sequence "sequence", for which the function function returns True.
        
            filter(function, sequence)

            - The function filter(f,l) needs a function f as its first argument. f has to return a Boolean value, i.e. either True or False. 

            - This function will be applied to every element of the list l.

            - Only if f returns True will the element be produced by the iterator, which is the return value of filter(function, sequence).

            >>> fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
            >>> odd_numbers = list(filter(lambda x: x % 2, fibonacci))
            >>> print(odd_numbers)
            [1, 1, 3, 5, 13, 21, 55]

        reduce()
        
        Using Lists as stacks and
        Queues

            - https://www.geeksforgeeks.org/using-list-stack-queues-python/

'''