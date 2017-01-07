# CoCo

[![Build Status](https://travis-ci.org/buptmiao/CoCo.svg?branch=master)](https://travis-ci.org/buptmiao/CoCo)
![License](https://img.shields.io/dub/l/vibe-d.svg)

CoCo is a Code Convert tool which can transform file's encoding format.


## Install

#### install by pip
```
pip install cocov
```



#### install by source
```
> git clone git@github.com:buptmiao/CoCo.git  
> cd CoCo
> python setup.py install
```

## Usage
```
usage: CoCo [-h] [--version] [-i I [I ...]] [-o O] [src] [dst]

positional arguments:
  src            input file
  dst            output file

optional arguments:
  -h, --help     show this help message and exit
  --version, -v  show program's version number and exit
  -i I [I ...]   print the encoding of the input files
  -o O           specify the encoding of output file, utf-8 by default
```

## Examples

* check the encoding of files
```
> coco -i foo.csv
foo.csv utf-8

> coco -i foo.csv bar.csv
foo.csv utf-8
bar.csv gb2312
```
* convert encoding of files
```
> coco -i foo.csv
foo.csv utf-8

> coco -o gb2312 foo.csv bar.csv

> coco -i bar.csv
bar.csv gb2312

> coco -o utf-8 bar.csv utf.csv

> coco -i bar.csv utf.csv
bar.csv gb2312
utf.csv utf-8
```
* if -o option is not specified, utf-8 is used by default

```
> coco -o utf-8 bar.csv utf.csv
```
equals to
```
> coco bar.csv utf.csv
```
 
## More updates