# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='cocov',
    version='0.0.1',
    packages=['coco'],  # 代码所在包
    url='https://github.com/buptmiao/CoCo',
    license='MIT License',
    author='buptmiao',
    author_email='buptmiao@163.com',
    description="CoCo is a Code Convert tool which can transform file's encoding format.",
    zip_safe=False,
    install_requires=[
        'chardet',
    ],
    entry_points={
        'console_scripts': [
            'coco = coco.coco:start'
        ]
    },
)
