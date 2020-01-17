#! /usr/bin/env python
# -*- coding: utf-8 -*_
# Author: Skyfalldechjx<skyfalldec@outlook.com>
from distutils.core import setup
import setuptools

setup(
    name='FeonGui', # 包的名字
    version='0.0.1',  # 版本号
    description='project describe',  # 描述
    author='HuangJiaxu', # 作者
    author_email='skyfalldec@outlook.com',  # 你的邮箱**
    url='',  # 可以写github上的地址，或者其他地址
    
    # 依赖包
    install_requires=[
        'numpy',
        'Feon',
        'pyqt5',
        'easygui',
        'meshio',

    ],
    classifiers=[
        'Operating System :: Microsoft'  # 你的操作系统
        'Intended Audience :: Developers',
        'Programming Language :: Python',   # 支持的语言
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)
