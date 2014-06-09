pycelex-phonology
=================

Python implementation of the celex2 dictionary. Only phonology is implemented.

##Usage:
```
from celex.factory import build_celex

path_to_celex = "YOUR PATH TO CELEX"
celex = build_celex(path_to_celex, 0, 0) # english language, version 0

word = "dean"
phoneme_translation = celex[word]
```

The above snippet shows a simple way to use pycelex-phonology.

Please read the documentation in celex/factory.py for more information on parameters.

test/ contains the implementation of the test cases for the code. It also includes
a fake celex directory "test_celex2/" used for testing only.

There are READMEs in the celex and test folders detailing the various options
and rationale behind features. Some features are customized for my own projects so
read the documentation well and decide if those features are useful to you.
