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

    # gw2api endpoints
    ('https://gw2-api.com/item/36273', lambda x: x),
    ('https://gw2-api.com/items/12434,26186,47690,13970,28151,45945,37255,28677,32689,67044', lambda x: len([y for y in x if y is not False]) == len(x) and len(x) == 10),
    ('https://gw2-api.com/items/all', lambda x: len([y for y in x if y is not False]) == len(x) and len(x) > 10000),
    ('https://gw2-api.com/items/all-prices', lambda x: len([y for y in x if y is not False]) == len(x) and len(x) > 10000),
    ('https://gw2-api.com/items/categories', lambda x: len(x) > 0),
    ('https://gw2-api.com/items/autocomplete?q=Twilight', lambda x: len(x) > 0),
    ('https://gw2-api.com/items/by-name?name=Twilight', lambda x: len(x) > 0),
    ('https://gw2-api.com/items/by-skin?skin_id=12', lambda x: len(x) > 0),
    ('https://gw2-api.com/items/query?include_name=Recipe&craftable=1', lambda x: len(x) > 0),
    ('https://gw2-api.com/skins/resolve', lambda x: len(x) > 3500),
    ('https://gw2-api.com/recipe/nested/31083', lambda x: len(x) > 0),
    ('https://gw2-api.com/gems/history', lambda x: len(x) == 2 and len(x['gold_to_gem']) > 1000),
    ('https://gw2-api.com/leaderboard/pvp', lambda x: len(x) == 2 and len(x['eu']) == 1000),
    ('https://gw2-api.com/leaderboard/pvp/queicherius.2568', False),
    ('https://gw2-api.com/image/4ad5963baebf58383f75f13a2a70a22c/64', False, False),

    # gw2efficiency endpoints
    ('https://gw2efficiency.com/api/account/dyes', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/account/miniatures', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/account/wardrobe', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/account/achievements', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/account/statistics/account_value', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/account/materials', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/dungeon-tokens', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/spirit-shards', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/karma', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/badges-of-honor', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/laurels', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/guild-commendations', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/currencies/claim-tickets', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/tradingpost/custom-item-prices', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/average-times.json', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/dungeons/fractals', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/worldbosses', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/gathering', lambda x: len(x) > 0),
    ('https://gw2efficiency.com/api/community/lottery', lambda x: len(x) > 0)

]