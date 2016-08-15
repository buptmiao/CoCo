# -*- coding:utf-8 -*-

import codecs
import chardet
import argparse

__author__ = 'buptmiao'


def getargs():
    parse = argparse.ArgumentParser()
    parse.add_argument('-i', type=str, help="print the encoding of the input file")
    parse.add_argument('-o', type=str, help="specify the encoding of output file, utf-8 by defaul")
    parse.add_argument('src', help="input file")
    parse.add_argument('dst', help="output file")
    args = parse.parse_args()
    return vars(args)


def readfile(src, encoding):
    with codecs.open(src, "r", encoding) as f:
        return f.read()


def writefile(dst, u, encoding):
    with codecs.open(dst, "w", encoding) as f:
        f.write(u)


def detect(src):
    try:
        with open(src, 'rb') as f:
            data = f.read(1024)
            return chardet.detect(data)['encoding']
    except AttributeError as e:
        print(e)
        usage()


def convert(src, dst, dstco):
    try:
        srcco = detect(src)
        content = readfile(src, encoding=srcco)
        writefile(dst, content, encoding=dstco)
    except Exception as e:
        print(e)
        usage()


def usage():
    print("Usage: coco [OPTIONS] src dst")
    print("       coco [ --help | -v | --version ]")
    print("")
    print("A code convert tool\n")
    print("Options:\n")
    print("  -i input              print the encoding of the input file")
    print("  -o encoding           specify the encoding of output file, utf-8 by default")
    print("")
    print("Example:\n")
    print("  coco -i test.txt")
    print("  coco -o utf-8 foo.txt bar.txt")
    print("  coco foo.txt bar.txt")
    pass


def start():
    args = getargs()
    if args['i'] is not None:
        print(detect(args['i']))
        exit()
    src = args['src']
    dst = args['dst']
    outencoding = args['o']
    if outencoding is None:
        outencoding = 'utf-8'
    convert(src, dst, outencoding)
    exit()


if __name__ == '__main__':
    start()
