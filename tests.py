import unittest

from post_code import _valid_size


class TestPostCodeUK(unittest.TestCase):
    def test_verify_size_post_code_is_equal_6(self):
        post_code = 'A9 9AA'
        self.assertTrue(_valid_size(post_code))

    def test_verify_size_post_code_is_equal_7(self):
        post_code = 'A9A 9AA'
        self.assertTrue(_valid_size(post_code))

    def test_verify_size_post_code_is_equal_8(self):
        post_code = 'AA9A 9AA'
        self.assertTrue(_valid_size(post_code))

    def test_verify_size_post_code_is_out_range(self):
        post_code = 'AA9A 9OUT'
        self.assertFalse(_valid_size(post_code))


if __name__ == '__main__':
    unittest.main()
