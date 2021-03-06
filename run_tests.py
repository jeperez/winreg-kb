#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to run the tests."""

import sys
import unittest

# Change PYTHONPATH to include winregrc.
sys.path.insert(0, u'.')

import winregrc.dependencies


if __name__ == '__main__':
  if not winregrc.dependencies.CheckDependencies():
    sys.exit(1)

  test_suite = unittest.TestLoader().discover('tests', pattern='*.py')
  test_results = unittest.TextTestRunner(verbosity=2).run(test_suite)
  if not test_results.wasSuccessful():
    sys.exit(1)
