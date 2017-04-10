from flask import Flask, abort

from post_code import PostCodeUK

app = Flask(__name__)
post_code_validator = PostCodeUK()


@app.route('/')
def main():
    result = """This app validate the post code for uk. Access /code, where
              code is the post_code that you want to validate.\n
              For example /EC1A 1BB to verify is the post code EC1A 1BB
              is valid.\n
              You can get more details about post code in uk here:
              https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom"""
    return result


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
