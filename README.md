## Version
0.0.1

## Python Version
Python 3.10.8 is supported. 

## Installation

[sudo] pip install tdil

## Quickstart
```python

from src.sep import Turkce

turkce = Turkce()

word = input("Enter A Word")

is_turkish = turkce.seperator(word)
print(is_turkish)
# If your word is turkish word return True.
# If your word isn't turkish word return False.