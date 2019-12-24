# dexparser

Powerful DEX file format parser for Pythonist!

[![Build Status](https://travis-ci.com/bunseokbot/dexparser.svg?branch=master)](https://travis-ci.com/bunseokbot/dexparser)
[![PyPI version](https://badge.fury.io/py/dexparser.svg)](https://badge.fury.io/py/dexparser)
[![Documentation Status](https://readthedocs.org/projects/dexparser/badge/?version=latest)](https://dexparser.readthedocs.io/en/latest/?badge=latest)

## Usage

### Pre-requirements

* Python 3.x (Unofficially, dexparser support Python 2.x)
* DEX friendly mind

### Install
`pip install dexparser`

### Load DEX from file
```
from dexparser import Dexparser

filedir = '/path/to/classes.dex'
dex = Dexparser(filedir=filedir)
```

### Load DEX file from object
```
from dexparser import Dexparser

with open('classes.dex', 'rb') as fileobj:
    dex = Dexparser(fileobj=fileobj)
```

## License
This project is licensed under the MIT License
