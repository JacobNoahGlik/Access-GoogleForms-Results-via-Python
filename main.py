from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = ["https://www.googleapis.com/auth/forms.responses.readonly"]
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("token.json")
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC
)

FORM_ID = "1VaXClkkAF8F45vu60tvn8jGpKBZEDmN-MRDwur2B3CM"

response = form_service.forms().responses().list(formId=FORM_ID).execute()

# Print form responses
for resp in response.get("responses", []):
    print(resp)