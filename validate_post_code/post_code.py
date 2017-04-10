class PostCodeUK():
    def validate_post_code_for_uk(self, post_code):
        self.post_code = post_code
        return (self._valid_size() and
                self._valid_space_position() and
                self._valid_last_3_positions() and
                self._verify_first_position() and
                self._verify_second_position() and
                self._verify_third_position() and
                self._verify_fourth_position())

    def _valid_size(self):
        result = True
        size = len(self.post_code)
        if size < 6 or size > 8:
            result = False
        return result

    def _valid_space_position(self):
        size = len(self.post_code)
        result = True
        if self.post_code[size - 4] != ' ':
            result = False
        return result

    def _valid_last_3_positions(self):
        """
        The last 3 positions have the format: 9AA, where
        9 represent one digit and A represent one letter.
        The final two letters do not use the letters CIKMOV
        """
        not_allowed = ['C', 'I', 'K', 'M', 'O', 'V']
        post_code = self.post_code
        result = (post_code[-1].isalpha() and
                  post_code[-1] not in not_allowed and
                  post_code[-2].isalpha() and
                  post_code[-2] not in not_allowed and
                  post_code[-3].isdigit())
        return result

    def _verify_first_position(self):
        """
        The first position is not a number
        The letters QVX are not used in the first position
        """
        not_allowed = ('Q', 'V', 'X')
        result = self.post_code[0].isalpha()
        if self.post_code[0] in not_allowed:
            result = False
        return result

    def _verify_second_position(self):
        """
        The second position is a number or a letter
        The letters IJZ are not used in the second position
        """
        not_allowed = ('I', 'J', 'Z')
        result = self.post_code[1].isalpha() or self.post_code[1].isdigit()
        if self.post_code[1] in not_allowed:
            result = False
        return result

    def _verify_third_position(self):
        """
        The only letters to appear in the third position are
        ABCDEFGHJKPSTUW when the structure starts with A9A.
        """
        allowed = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'P', 'S',
                   'T', 'U', 'W']
        result = True
        if self.post_code[2].isalpha():
            result = self.post_code[2] in allowed
        return result

    def _verify_fourth_position(self):
        """
        The only letters to appear in the fourth position are
        ABEHMNPRVWXY when the structure starts with AA9A.
        """
        allowed = ['A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y']
        result = True
        if self.post_code[3].isalpha():
            result = self.post_code[3] in allowed
        return result
