# dexparser

Powerful DEX file format parser for Pythonist!

[![Build Status](https://travis-ci.com/bunseokbot/dexparser.svg?branch=master)](https://travis-ci.com/bunseokbot/dexparser)
[![PyPI version](https://badge.fury.io/py/dexparser.svg)](https://badge.fury.io/py/dexparser)
[![Documentation Status](https://readthedocs.org/projects/dexparser/badge/?version=latest)](https://dexparser.readthedocs.io/en/latest/?badge=latest)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fbunseokbot%2Fdexparser&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Usage

See the [docs](https://dexparser.readthedocs.io/en/latest/) for detail descriptions.

### Pre-requirements

* Python 3.x (Unofficially, dexparser support Python 2.x)
* DEX friendly mind

### Install
`pip install dexparser`

### Load DEX from filename
```
from dexparser import DEXParser

filedir = '/path/to/classes.dex'
dex = DEXParser(filedir=filedir)
```

### Load DEX file from object
```
from dexparser import DEXParser

with open('classes.dex', 'rb') as fileobj:
    dex = DEXParser(fileobj=fileobj.read())
```

### Load APK file from object and filename
```
from dexparser import APKParser

filedir = '/path/to/test.apk'
apk = APKParser(filedir=filedir)

with open('/path/to/test.apk', 'rb') as fileobj:
    apk = APKParser(fileobj=fileobj.read())
```

### Load AAB file from object and filename
```
from dexparser import AABParser

filedir = '/path/to/test.apk'
aab = AABParser(filedir=filedir)

with open('/path/to/test.apk', 'rb') as fileobj:
    aab = AABParser(fileobj=fileobj.read())
```


## License
This project is licensed under the MIT License

## Reference
* [Dalvik Executable Format](https://source.android.com/devices/tech/dalvik/dex-format)
* [dexparser released! (Korean)](https://iam.namjun.kim/opensource/2019/12/25/dexparser-released/)

