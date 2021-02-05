import os
from distutils.dir_util import copy_tree

# creating folders and project declarations/other files


def html(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('project created!')
    copy_tree('foldersHTML', path)


def py(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('project created!')
    file = open(path+'/app.py', 'w+')


def java(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('project created!')
    file = open(path+'/main.java', 'w+')


def c(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('project created!')
    file = open(path+'/app.c', 'w+')


def cpp(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('project created!')
    file = open(path+'/app.cpp', 'w+')
