def _valid_size(post_code):
    result = True
    size = len(post_code)
    if size < 6 or size > 8:
        result = False
    return result


def _valid_space_position(post_code):
    size = len(post_code)
    result = True
    if post_code[size - 4] != ' ':
        result = False
    return result


def _valid_last_3_positions(post_code):
    """
    The last 3 positions have the format: 9AA, where
    9 represent one digit and A represent one letter
    """
    result = (post_code[-1].isalpha() and post_code[-2].isalpha()
              and post_code[-3].isdigit())
    return result


def _verify_first_position(post_code):
    """
    The first position is not a number
    The letters QVX are not used in the first position
    """
    not_allowed = ('Q', 'V', 'X')
    result = post_code[0].isalpha()
    if post_code[0] in not_allowed:
        result = False
    return result
