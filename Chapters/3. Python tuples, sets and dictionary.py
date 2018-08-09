'''

3. Python tuples, sets and dictionary

TUPLES

    Concept (immutable)

        - A tuple is a collection which is ordered and unchangeable. 
        
        - In Python tuples are written with round brackets. 

    Creating and Deleting Tuples

        - Create a Tuple:

        >>> thistuple = ("apple", "banana", "cherry")
        >>> print(thistuple)

        - Tuples are immutable and cannot be deleted, but deleting tuple entirely is possible by using the keyword "del."

    Accessing Values in a Tuple

        - Return the item in position 1:

        >>> thistuple = ("apple", "banana", "cherry")
        >>> print(thistuple[1])

    Updating Tuples

        - You cannot change values in a tuple:

        >>> thistuple = ("apple", "banana", "cherry")
        >>> thistuple[1] = "blackcurrant" # test changeability
        >>> print(thistuple)

    Basic Operations

        - Dictionary can return the list of tuples by calling items, where each tuple is a key value pair.

        >>> a = {'x' : 100, 'y' : 200}
        >>> b = list(a.items())
        >>> print(b)

    Delete items in a Tuple

        - You cannot remove items in a tuple.

        - However, you can take portions of existing tuples to make new tuples.

    Slicing and Matrices

        - To fetch specific sets of sub-elements from tuple or list, we use this unique function called slicing. Slicing is not only applicable to tuple but also for array and list.

        >>> x = ("a", "b","c", "d", "e")
        >>> print(x[2:4])

    Built-in tuple functions

        - To perform different task, tuple allows you to use many built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.

    Advantages

        - Iterating through tuple is faster than with list, since tuples are immutable.
        
        - Tuples that consist of immutable elements can be used as key for dictionary, which is not possible with list
        
        - If you have data that is immutable, implementing it as tuple will guarantee that it remains write-protected

Sets 

    Concept

        - A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
    
    Operations

        - Create a Set:

        >>> thisset = {"apple", "banana", "cherry"}
        >>> print(thisset)

        - The set is unordered, so the items will appear in a random order.

        - It is also possible to use the set() constructor to make a set.

        - Using the add() method to add an item:

        >>> thisset = set(("apple", "banana", "cherry"))
        >>> thisset.add("damson")
        >>> print(thisset)

Dictionary

    Concept (mutable)

        - A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

    Creating and Accessing Values in a Dictionary

        - Create and print a dictionary:

        >>> thisdict =	{
        ...     'apple': 'green',
        ...     'banana': 'yellow',
        ...     'cherry': 'red'
        ... }
        >>> print(thisdict['apple'])
        >>> print(thisdict)

        - Adding an item to the dictionary is done by using a new index key and assigning a value to it

        >>> thisdict =	dict(apple="green", banana="yellow", cherry="red")
        >>> thisdict["damson"] = "purple"
        >>> print(thisdict)
    
    Updating Dictionary

        - Change the apple color to "red":

        >>> thisdict =	{
        ...     "apple": "green",
        ...     "banana": "yellow",
        ...     "cherry": "red"
        ... }
        >>> thisdict["apple"] = "red"
        >>> print(thisdict)
    
    Delete Dictionary Elements

        - Removing a dictionary item must be done using the del.

        >>> thisdict =	dict(apple="green", banana="yellow", cherry="red")
        >>> del(thisdict["banana"])
        >>> print(thisdict)
    
    Looping over Dictionary

        - https://dev-notes.eu/2017/09/iterating-over-dictionary-in-python/

    Properties of Dictionary Keys 

        - https://en.wikibooks.org/wiki/Python_Programming/Dictionaries#Operations_on_Dictionaries
    
    Built-in Dictionary Functions

        - http://doc.pyschools.com/html/dictionary.html

'''