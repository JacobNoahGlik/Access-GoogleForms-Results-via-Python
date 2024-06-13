# Getting an OAuth Token

Go to [Google Cloud Consol](https://console.cloud.google.com/)s website and select the `APIs & Services` button.

Navigate to the `credentials` tab and select the `+ CREATE CREDENTIALS` button to reveal a drop-down of 4 items. 

Select the second item (`OAuth client ID`, sub-text: "Requests user consent so your app can access the user's data")

This will bring you to the "Create OAuth client ID" page. **However**, in order to be able to continue you need to fill out the `OAuth consent screen` and pass the screening process. The step-by-step process is in the [OAuthConcent.md](OAuthConcent.md) file.

Finally, click the application type dropdown, select `Desktop app`, and name it whatever you'd like.

Click the blue `CREATE` button at the bottom of the page.

A pop-up window will appear with your `client-ID` and `client-secret`. Save both somewhere secure.

