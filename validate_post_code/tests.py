import unittest

from .post_code import PostCodeUK


class TestPostCodeUK(unittest.TestCase):
    def setUp(self):
        self.post_code_size_6 = 'A9 9AA'
        self.post_code_size_7 = 'A9A 9AA'
        self.post_code_size_8 = 'AA9A 9AA'
        self.post_code_uk = PostCodeUK()

    def test_verify_size_post_code_is_equal_6(self):
        self.post_code_uk.post_code = self.post_code_size_6
        self.assertTrue(self.post_code_uk._valid_size())

    def test_verify_size_post_code_is_equal_7(self):
        self.post_code_uk.post_code = self.post_code_size_7
        self.assertTrue(self.post_code_uk._valid_size())

    def test_verify_size_post_code_is_equal_8(self):
        self.post_code_uk.post_code = self.post_code_size_8
        self.assertTrue(self.post_code_uk._valid_size())

    def test_verify_size_post_code_is_out_range(self):
        self.post_code_uk.post_code = 'AA9A9 OUT'
        self.assertFalse(self.post_code_uk._valid_size())

    def test_verify_space_position_is_2(self):
        self.post_code_uk.post_code = self.post_code_size_6
        self.assertTrue(self.post_code_uk._valid_space_position())

    def test_verify_space_position_is_3(self):
        self.post_code_uk.post_code = self.post_code_size_7
        self.assertTrue(self.post_code_uk._valid_space_position())

    def test_verify_space_position_is_4(self):
        self.post_code_uk.post_code = self.post_code_size_8
        self.assertTrue(self.post_code_uk._valid_space_position())

    def test_verify_space_position_is_out_of_range(self):
        self.post_code_uk.post_code = 'AA9A9O U'
        self.assertFalse(self.post_code_uk._valid_space_position())

    def test_verify_last_3_positions_is_correct(self):
        self.post_code_uk.post_code = self.post_code_size_6
        self.assertTrue(self.post_code_uk._valid_last_3_positions())

    def test_verify_have_number_in_last_position(self):
        self.post_code_uk.post_code = 'A9 9A1'
        self.assertFalse(self.post_code_uk._valid_last_3_positions())

    def test_verify_not_allowed_letters_in_last_position(self):
        for letter in ['C', 'I', 'K', 'M', 'O', 'V']:
            self.post_code_uk.post_code = "AA9A 9A{0}".format(letter)
            self.assertFalse(self.post_code_uk._valid_last_3_positions())

    def test_verify_have_number_in_penultimate_position(self):
        self.post_code_uk.post_code = 'A9 91A'
        self.assertFalse(self.post_code_uk._valid_last_3_positions())

    def test_verify_not_allowed_letters_in_penultimate_position(self):
        for letter in ['C', 'I', 'K', 'M', 'O', 'V']:
            self.post_code_uk.post_code = "AA9A 9{0}A".format(letter)
            self.assertFalse(self.post_code_uk._valid_last_3_positions())

    def test_verify_have_letter_in_antepenultimate_position(self):
        self.post_code_uk.post_code = 'A9 AAA'
        self.assertFalse(self.post_code_uk._valid_last_3_positions())

    def test_verify_first_position_is_letter(self):
        self.post_code_uk.post_code = self.post_code_size_6
        self.assertTrue(self.post_code_uk._verify_first_position())

    def test_verify_first_position_is_not_letter(self):
        self.post_code_uk.post_code = '99 9AA'
        self.assertFalse(self.post_code_uk._verify_first_position())

    def test_verify_first_position_is_not_Q(self):
        self.post_code_uk.post_code = 'Q9 9AA'
        self.assertFalse(self.post_code_uk._verify_first_position())

    def test_verify_first_position_is_not_V(self):
        self.post_code_uk.post_code = 'V9 9AA'
        self.assertFalse(self.post_code_uk._verify_first_position())

    def test_verify_first_position_is_not_X(self):
        self.post_code_uk.post_code = 'X9 9AA'
        self.assertFalse(self.post_code_uk._verify_first_position())

    def test_verify_second_position_is_not_letter(self):
        self.post_code_uk.post_code = self.post_code_size_6
        self.assertTrue(self.post_code_uk._verify_second_position())

    def test_verify_second_position_is_letter(self):
        self.post_code_uk.post_code = self.post_code_size_7
        self.assertTrue(self.post_code_uk._verify_second_position())

    def test_verify_second_position_is_I(self):
        self.post_code_uk.post_code = 'AI 9AA'
        self.assertFalse(self.post_code_uk._verify_second_position())

    def test_verify_second_position_is_J(self):
        self.post_code_uk.post_code = 'AJ 9AA'
        self.assertFalse(self.post_code_uk._verify_second_position())

    def test_verify_second_position_is_Z(self):
        self.post_code_uk.post_code = 'AZ 9AA'
        self.assertFalse(self.post_code_uk._verify_second_position())

    def test_verify_third_position_is_space(self):
        self.post_code_uk.post_code = 'A9 9AA'
        self.assertTrue(self.post_code_uk._verify_third_position())

    def test_verify_third_position_is_digit(self):
        self.post_code_uk.post_code = 'A99 9AA'
        self.assertTrue(self.post_code_uk._verify_third_position())

    def test_verify_third_position_is_letter_and_incorrect(self):
        self.post_code_uk.post_code = 'A9Z 9AA'
        self.assertFalse(self.post_code_uk._verify_third_position())

    def test_verify_third_position_is_letter_and_correct(self):
        allowed = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'P', 'S',
                   'T', 'U', 'W']
        for letter in allowed:
            self.post_code_uk.post_code = 'A9{0} 9AA'.format(letter)
            self.assertTrue(self.post_code_uk._verify_third_position())

    def test_verify_fourth_position_is_space(self):
        self.post_code_uk.post_code = 'A9A 9AA'
        self.assertTrue(self.post_code_uk._verify_fourth_position())

    def test_verify_fourth_position_is_number(self):
        self.post_code_uk.post_code = 'AA99 9AA'
        self.assertTrue(self.post_code_uk._verify_fourth_position())

    def test_verify_fourth_position_is_letter_and_incorrect(self):
        self.post_code_uk.post_code = 'AA9Z 9AA'
        self.assertFalse(self.post_code_uk._verify_fourth_position())

    def test_verify_fourth_position_is_letter_and_correct(self):
        allowed = ['A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y']
        for letter in allowed:
            self.post_code_uk.post_code = 'AA9{0} 9AA'.format(letter)
            self.assertTrue(self.post_code_uk._verify_fourth_position())

    def test_verify_post_code_with_size_6_is_correct(self):
        post_code = self.post_code_size_6
        self.assertTrue(self.post_code_uk.validate_post_code_for_uk(post_code))

    def test_verify_post_code_with_size_7_is_correct(self):
        post_code = self.post_code_size_7
        self.assertTrue(self.post_code_uk.validate_post_code_for_uk(post_code))

    def test_verify_post_code_with_size_8_is_correct(self):
        post_code = self.post_code_size_8
        self.assertTrue(self.post_code_uk.validate_post_code_for_uk(post_code))

    def test_verify_post_code_is_incorrect(self):
        post_cod = 'AAAA AAA'
        self.assertFalse(self.post_code_uk.validate_post_code_for_uk(post_cod))


if __name__ == '__main__':
    unittest.main()
