# Hangman Game

* What is the use of if __name__ == '__main__' ?
In Python, `if __name__ == '__main__':` is used to check whether the script is being run directly or it's being imported as a module. 

When a Python file is run directly, the special variable `__name__` is set to `'__main__'`. So, `if __name__ == '__main__':` allows the code under this if-statement to run only when the file is executed directly, not when it is imported as a module in another script.

Here's an example:

```python
# This is my_script.py

def function():
    print("This is a function inside my_script.")

if __name__ == '__main__':
    print("my_script.py is being run directly.")
    function()
```

If you run `my_script.py`, it will print:

```
my_script.py is being run directly.
This is a function inside my_script.
```

But if you import `my_script` in another Python file and run that file, it won't print anything because `my_script.py` is not being run directly in this case.

```python
# This is another_script.py

import my_script

my_script.function()
```

If you run `another_script.py`, it will only print:

```
This is a function inside my_script.
```

I hope this helps! Let me know if you have any other questions. 😊

* word.count("char") counts number of times the char occurs in the word

## collection.Counter()
returns how many times each char is repeated 
example - i/p:print(Counter('apple'))
          o/p:Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})