'''

5. Working with Files and Directories

Creating files
Operations on files (open, close, read, write)
file object attributes
filepositions

    - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

Listing Files in a Directory

    >>> import os
    >>> print(os.listdir("C:/Users/Quark/Documents/shuffler"))  

https://docs.python.org/3/library/os.html

Testing File Types

    - We can use endswith to test this out.

Removing Files and Directories

    - os.remove() or os.unlink()

    - os.rmdir(): Removes the specified directory. The directory must be empty or Python will display an exception message.

    - shutil.rmtree(): Removes the specified directory, all subdirectories, and all files. This function is especially dangerous because it removes everything without checking (Python assumes that you know what you’re doing). As a result, you can easily lose data using this function.

Copying and Renaming Files

    - https://docs.python.org/3/library/shutil.html

    - https://docs.python.org/3/library/os.html

Splitting Pathnames

    - https://docs.python.org/3/library/stdtypes.html#str.split

    - https://docs.python.org/3/library/os.path.html

Creating and Moving to Directories

    - https://stackabuse.com/creating-and-deleting-directories-with-python/

Traversing Directory Trees

    - https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/

'''