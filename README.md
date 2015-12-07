# Slack Endpoint Status

Get status messages of your endpoints in Slack.

## Install

First clone the repository and install the required dependencies:

```bash
git clone https://github.com/queicherius/slack-endpoint-status.git
pip install slackweb
```

After this update `settings.py` with your webhook, channel and endpoints.

Now you can run `check.py` to monitor your endpoints:

```bash
python check.py
```

If you want the script to run permanently in the background, you can run

```bash
# TODO
```