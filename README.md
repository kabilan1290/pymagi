### pymagi 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 


# Description:
- ``pymagi`` is a python based client for <a href="https://github.com/gchq/CyberChef-server">CyberChef</a> API server.
- ``pymagi`` is used to bake cyberchef recipies in python program.

# Dependencies:

- You need to run CyberChef API server in the background for pymagi to work.
- https://github.com/gchq/CyberChef-server#installing - Visit here to know the installation of cyberchef server.

# Recepies:

- Currently ``pymagi`` can handle the following recepies.

```
- base64 encode/decode 
- morse encode/decode
- base85 encode/decode
- braillie encode/decode
- binary encode/decode
- octal encode/decode
- base32 encode/decode
- base58 encode/decode
- base62 encode/decode
- url encode/decode
- html encode/decode
```
# Usage:

- Make sure you have python installed on your system.
- Run the following command.

```
pip install pymagi
```
- Python3
```
>>> from pymagi import *
>>> a = morseencode("This_is_test")
>>> a
'- .... .. ... ..--.- .. ... ..--.- - . ... -'
>>> morsedecode(a)
'THIS_IS_TEST'
```

# Proof of work:

<a hre="https://youtu.be/PnwiZyUZ9bc">Watch here</a>
