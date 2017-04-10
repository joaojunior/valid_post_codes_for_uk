[![Build Status](https://travis-ci.org/joaojunior/valid_post_codes_for_uk.svg?branch=master)](https://travis-ci.org/joaojunior/valid_post_codes_for_uk)

# Valid post codes for UK
This api supports validating and formatting post codes for UK. You can see the rules in https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

# Install
After clone this project, you can run this with two commands below:
```
pip install -r requirements.txt
python validate_post_code/api.py
```
# Response
You can make a get in url '/post_code', where 'post_code' is the post code that you would like to verify if is valid.
When the post_code is valid, the api return a status code equal 200 and when the post_code isn't valid, the api
return the status_code 422.

# Heroku
You can access this api in heroku: https://validatepostcodeuk.herokuapp.com/
