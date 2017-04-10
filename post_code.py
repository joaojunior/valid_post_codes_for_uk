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
