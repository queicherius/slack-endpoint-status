# -*- coding: utf-8 -*-
import json, requests
import time
import slackweb
import settings


# Go through all endpoint and check them one by one
def check_endpoints():
    failed_endpoints = []
    for entity in settings.endpoints:
        failure = check_endpoint(*entity)
        if not failure:
            continue
        failed_endpoints.append(failure)
    return failed_endpoints


# Check if a url is reachable and matches the content checking function
def check_endpoint(url, check_function, json_response=True):

    try:
        response = requests.get(url=url)
    except Exception as e:
        return {'url': url, 'status': str(e)}

    if response.status_code != 200:
        return {'url': url, 'status': 'Status code ' + str(response.status_code)}

    data = json.loads(response.text) if json_response else response.text

    if check_function and not check_function(data):
        return {'url': url, 'status': 'Content check failure'}

    return False


# Format failed endpoints into a markdown list
def format_failed_endpoints(endpoints):
    messages = []
    for i, endpoint in enumerate(failed_endpoints):
        messages.append(u'' + str(i + 1) + '. ' + endpoint['status'] + ': ' + endpoint['url'] + '\n')
    return ''.join(messages)


# Post a message to the slack channel
def post_slack_message(title, color, text=False):
    attachment = {"title": title, "fallback": title, "color": color, "mrkdwn_in": ["text"]}
    if text:
        attachment['text'] = text
    slack.notify(attachments=[attachment], channel=settings.channel, username="status-bot", icon_emoji=":bell:")


# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Startup Slack client
slack = slackweb.Slack(url=settings.webhook)

# Save the current status
current = False

# Every 30 seconds check the status and write a Slack message if the status changed
while 1:
    try:
        print "Checking... ",
        failed_endpoints = check_endpoints()

        if current == failed_endpoints:
            print "No change"
            time.sleep(30)
            continue

        current = failed_endpoints

        if len(failed_endpoints) == 0:
            print "Working"
            post_slack_message('Status change: Working', 'good')
        else:
            print "Failing", failed_endpoints
            post_slack_message('Status change: Failing', 'danger', format_failed_endpoints(failed_endpoints))

        time.sleep(30)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print "Error"