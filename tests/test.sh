#!/bin/bash

coco -i foo.csv
coco -o gb2312 foo.csv bar.csv
coco -i bar.csv
coco -o utf-8 bar.csv utf.csv
coco -i utf.csv
