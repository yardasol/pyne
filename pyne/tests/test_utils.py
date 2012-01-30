"""PyNE utility tests"""
import os

import nose 

from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, assert_in, \
                       assert_true

from pyne import utils
import numpy as np


def test_to_sec():
    assert_equal(120.0, utils.to_sec(2, 'M'))


def test_to_barns():
    assert_equal(3E3, utils.to_barns(3, 'KB'))


def test_message():
    if os.name is 'posix':
        assert_equal('\033[1;32mHello\033[0m', utils.message('Hello'))
    else:
        assert_equal('*** MESSAGE ***: Hello', utils.message('Hello'))


def test_failure():
    if os.name is 'posix':
        assert_equal('\033[1;31mWorld\033[0m', utils.failure('World'))
    else:
        assert_equal('*** FAILURE ***: World', utils.failure('World'))

def test_remove():
    # test file removal
    assert_true('hello.txt' not in os.listdir('.'))
    with open('hello.txt', 'w') as f:
        f.write("Hello PyNE!")
    assert_true('hello.txt' in os.listdir('.'))

    utils.remove('hello.txt')
    assert_true('hello.txt' not in os.listdir('.'))

    # test recursive dir removal
    assert_true('rawr' not in os.listdir('.'))
    os.mkdir('rawr')

    assert_true('hello.txt' not in os.listdir('rawr'))
    with open('rawr/hello.txt', 'w') as f:
        f.write("Hello PyNE!")
    assert_true('hello.txt' in os.listdir('rawr'))

    utils.remove('rawr')
    assert_true('rawr' not in os.listdir('.'))

    # Test pass through on non-existant 
    assert_true('Medic!' not in os.listdir('.'))
    utils.remove('Medic!')


if __name__ == "__main__":
    nose.main()
