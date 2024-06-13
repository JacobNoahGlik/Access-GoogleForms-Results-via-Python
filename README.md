# Acess GoogleForms Results via Python
Access Google Forms results via Python using GoogleFormsAPI

To use the GoogleFormsAPI you will need an OAuth token. Read the [get_an_OAuth_token.md](get_an_OAuth_token.md) for more info.

Once you've created an OAuth 2.0 token, google will give you access to a `client-ID` and `client-secret`. Download the [credentials.json](credentials.json) file and replace the `client-ID` and `client-secret` with your own.

Run `python3 main.py` to download the Google Forms data and display it locally as a CSV file. Note: this will require you to whitelist your email account and sign in when prompted so that the script can pull the submissions on your behalf.
