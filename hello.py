
#calling of main function

"""

When Python interpreter reads a source file, it will execute all the code found in it.
When Python runs the "source file" as the main program, it sets the special variable (__name__) to have a value ("__main__").
When you execute the main function, it will then read the "if" statement and checks whether __name__ does equal to __main__.
In Python "if__name__== "__main__" allows you to run the Python files either as reusable modules or standalone programs.


  Command line args are in sys.argv[1], sys.argv[2] ...
     sys.argv[0] is the script name itself and can be ignored
  because we are giving script name as a input
"""
#!/usr/bin/env python
# import modules used here -- sys is a very standard one
import sys
def main():
    print ('hello there', sys.argv[0])


if __name__== "__main__":
  main()


 # In a standard Python program, the list sys.argv contains the command-line arguments in the standard way with sys.argv[0] being the program itself, sys.argv[1] the first argument, and so on. If you know about argc, or the number of arguments, you can simply request this value from Python with len(sys.argv), just like we did in the interactive interpreter code above when requesting the length of a string. In general, len() can tell you how long a string is, the number of elements in lists and tuples (another array-like data structure), and the number of key-value pairs in a dictionary.