from flask import abort
from flask import Flask

from post_code import PostCodeUK

app = Flask(__name__)
post_code_validator = PostCodeUK()


@app.route('/<post_code>')
def validate_post_code(post_code):
    post_code = post_code.strip()
    result = post_code_validator.validate_post_code_for_uk(post_code)
    if result:
        return 'The Post code: {0} is valid!'.format(post_code)
    else:
        abort(422, {'errors': dict(post_code="This post code isn't valid")})


if __name__ == "__main__":
    app.run()
