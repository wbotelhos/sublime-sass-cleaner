import mock
import os.path
import sys
import unittest

sys.path.insert(0, os.path.abspath('.'))

import sass_cleaner

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

class Test(unittest.TestCase):
  def test__should_process__when_file_is_sass_and_view_size_is_more_than_zero__it_return_true(view):
    view = mock.Mock()

    view.file_name.return_value = 'name.sass'
    view.size.return_value      = 1

    assert sass_cleaner.should_process(view) == True

  def test__should_process__when_file_is_sass_and_view_size_is_less_or_equal_zero__it_return_false(view):
      view = mock.Mock()

      view.file_name.return_value = 'name.sass'
      view.size.return_value      = 0

      assert sass_cleaner.should_process(view) == False

  def test__should_process__when_file_is_not_sass_and_view_size_is_more_than_zero__it_return_false(view):
    view = mock.Mock()

    view.file_name.return_value = 'name.css'
    view.size.return_value      = 1

    assert sass_cleaner.should_process(view) == False

  def test__should_process__when_file_is_not_sass_and_view_size_is_less_or_equal_zero__it_return_false(view):
    view = mock.Mock()

    view.file_name.return_value = 'name.css'
    view.size.return_value      = 0

    assert sass_cleaner.should_process(view) == False

if __name__ == '__main__':
  unittest.main()
