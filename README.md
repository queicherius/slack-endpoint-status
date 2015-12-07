# Slack Endpoint Status

Get status messages of your endpoints in Slack.

## Features

- Checks if the endpoints are reachable
- Checks if the endpoints have the correct content based on custom functions
- Writes Slack status messages

## Install

```bash
# Clone the repository and install dependencies
git clone https://github.com/queicherius/slack-endpoint-status.git
cd slack-endpoint-status/
pip install slackweb

# Copy the example settings
cp settings-example.py settings.py

# Update settings.py with your webhook, channel and endpoints
nano settings.py

# Run the status checking script
python check.py
```

If you want the script to run permanently in the background, you can run

```bash
# TODO
```