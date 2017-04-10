from flask import Flask
from flask import abort

from validate_post_code.post_code import PostCodeUK

app = Flask(__name__)
post_code_validator = PostCodeUK()


@app.route('/validate/<post_code>')
def show_user_profile(post_code):
    result = post_code_validator.validate_post_code_for_uk(post_code)
    if result:
        return 'The Post code: {0} is valid!'.format(post_code)
    else:
        abort(422, {'errors': dict(post_code="This post code isn't valid")})
