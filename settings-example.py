# The Slack webhook URL
webhook = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'

# The Slack channel to post in
channel = '#api-status'

# The endpoints to be checked by the script
# The format is a tuple of:
# 1) a URL
# 2) a lambda function checking the content or "False" if no checking is wanted
# 3) a boolean if the value is considered JSON (defaults to True)
endpoints = [

    # Just check if an endpoint is available
    ('https://test.com/just-json.json'),

    # Check if an endpoint that does not return json is available
    ('https://test.com/image.png', False, False),

    # Check if an endpoint is available and returns an array with 10 entries
    ('https://test.com/array-ten.json', lambda x: len(x) == 10),

]