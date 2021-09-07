# tf-status

Share your Terraform stats in Mattermost!

### Setup

- Create a Mattermost personal access token and assign it to the `MM_TOKEN` environment variable.
- Set the `MM_URL` environment variable to your Mattermost server URL.
- Add the `bin/` folder to the front of your path so that it gets picked up before the real Terraform executable.

### Notes

- Assumes Terraform is intalled at `/usr/local/bin/terraform`.
