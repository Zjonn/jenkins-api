import unittest

from lib.json_requests import build_url


class TestBuildUrl(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(build_url(''), (''))

    def test_list_no_backslash(self):
        self.assertEqual(build_url(['', '']), '/')

    def test_list_one_backslash(self):
        self.assertEqual(build_url(['/', '']), '/')

    def test_list_two_backslash(self):
        self.assertEqual(build_url(['/', '/']), '/')

    def test_both_backslash(self):
        self.assertEqual(build_url('/', '/'), '/')

    def test_one_backslash(self):
        self.assertEqual(build_url('/', ''), '/')
        self.assertEqual(build_url('', '/'), '/')

    def test_no_backslash(self):
        self.assertEqual(build_url('', ''), '/')


if __name__ == '__main__':
    unittest.main()
