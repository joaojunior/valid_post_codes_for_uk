import unittest

from post_code import (_valid_size, _valid_space_position,
                       _valid_last_3_positions, _verify_first_position,
                       _verify_second_position)


class TestPostCodeUK(unittest.TestCase):
    def setUp(self):
        self.post_code_size_6 = 'A9 9AA'
        self.post_code_size_7 = 'A9A 9AA'
        self.post_code_size_8 = 'AA9A 9AA'

    def test_verify_size_post_code_is_equal_6(self):
        post_code = self.post_code_size_6
        self.assertTrue(_valid_size(post_code))

    def test_verify_size_post_code_is_equal_7(self):
        post_code = self.post_code_size_7
        self.assertTrue(_valid_size(post_code))

    def test_verify_size_post_code_is_equal_8(self):
        post_code = self.post_code_size_8
        self.assertTrue(_valid_size(post_code))

    def test_verify_size_post_code_is_out_range(self):
        post_code = 'AA9A9 OUT'
        self.assertFalse(_valid_size(post_code))

    def test_verify_space_position_is_2(self):
        post_code = self.post_code_size_6
        self.assertTrue(_valid_space_position(post_code))

    def test_verify_space_position_is_3(self):
        post_code = self.post_code_size_7
        self.assertTrue(_valid_space_position(post_code))

    def test_verify_space_position_is_4(self):
        post_code = self.post_code_size_8
        self.assertTrue(_valid_space_position(post_code))

    def test_verify_space_position_is_out_of_range(self):
        post_code = 'AA9A9O U'
        self.assertFalse(_valid_space_position(post_code))

    def test_verify_last_3_positions_is_correct(self):
        post_code = self.post_code_size_6
        self.assertTrue(_valid_last_3_positions(post_code))

    def test_verify_have_number_in_last_position(self):
        post_code = 'A9 9A1'
        self.assertFalse(_valid_last_3_positions(post_code))

    def test_verify_have_number_in_penultimate_position(self):
        post_code = 'A9 91A'
        self.assertFalse(_valid_last_3_positions(post_code))

    def test_verify_have_letter_in_antepenultimate_position(self):
        post_code = 'A9 AAA'
        self.assertFalse(_valid_last_3_positions(post_code))

    def test_verify_first_position_is_letter(self):
        post_code = self.post_code_size_6
        self.assertTrue(_verify_first_position(post_code))

    def test_verify_first_position_is_not_letter(self):
        post_code = '99 9AA'
        self.assertFalse(_verify_first_position(post_code))

    def test_verify_first_position_is_not_Q(self):
        post_code = 'Q9 9AA'
        self.assertFalse(_verify_first_position(post_code))

    def test_verify_first_position_is_not_V(self):
        post_code = 'V9 9AA'
        self.assertFalse(_verify_first_position(post_code))

    def test_verify_first_position_is_not_X(self):
        post_code = 'X9 9AA'
        self.assertFalse(_verify_first_position(post_code))

    def test_verify_second_position_is_not_letter(self):
        post_code = self.post_code_size_6
        self.assertTrue(_verify_second_position(post_code))

    def test_verify_second_position_is_letter(self):
        post_code = self.post_code_size_7
        self.assertTrue(_verify_second_position(post_code))

    def test_verify_second_position_is_I(self):
        post_code = 'AI 9AA'
        self.assertFalse(_verify_second_position(post_code))

    def test_verify_second_position_is_J(self):
        post_code = 'AJ 9AA'
        self.assertFalse(_verify_second_position(post_code))

    def test_verify_second_position_is_Z(self):
        post_code = 'AZ 9AA'
        self.assertFalse(_verify_second_position(post_code))


if __name__ == '__main__':
    unittest.main()
