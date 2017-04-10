def _valid_size(post_code):
    result = True
    size = len(post_code)
    if size < 6 or size > 8:
        result = False
    return result
