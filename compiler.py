# coding: utf8

# pylint: disable=W,C,R

from os import makedirs
from os.path import dirname, join

from wotw_blogger import Compiler
from wotw_blogger.generator.macro import ShellSession

CURRENT_DIR = dirname(__file__)
POSTS_DIR = join(CURRENT_DIR, 'posts')
BUILD_DIR = join(CURRENT_DIR, 'build')

try:
    makedirs(POSTS_DIR)
    macro = ShellSession()
    macro.install(POSTS_DIR)
except OSError:
    pass

try:
    makedirs(BUILD_DIR)
except OSError:
    pass


compiler = Compiler(
    POSTS_DIR,
    POSTS_DIR,
    BUILD_DIR
)
compiler.compile_everything()
