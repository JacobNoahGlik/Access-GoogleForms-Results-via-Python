from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
from GoogleStructures import SubmissionTable, GoogleFormsQuestion
from warn import deprecated
import os


@deprecated
def get_responses():
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

    # for resp in response.get("responses", []):
    #     print(resp)
    return response.get("responses", [])


@deprecated
def get_questions():
    SCOPES = [
        "https://www.googleapis.com/auth/forms.responses.readonly",
        "https://www.googleapis.com/auth/forms.body.readonly"
    ]
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

    form_info = form_service.forms().get(formId=FORM_ID).execute()
    questions = form_info.get('items', [])
    # {'itemId': '1c09dd1c', 'title': 'Enter your name', 'questionItem': {'question': {'questionId': '4ea269ef', 'required': True, 'textQuestion': {}}}}
    # for question in questions:
    #     print(question['itemId'])
    #     print(question['title'])
    #     print(question['questionItem']['question']['questionId'])
    #     print('_______________________\n')
    return questions


def single_request(FORM_ID: str = "1VaXClkkAF8F45vu60tvn8jGpKBZEDmN-MRDwur2B3CM"):
    SCOPES = [
        "https://www.googleapis.com/auth/forms.responses.readonly",
        "https://www.googleapis.com/auth/forms.body.readonly"
    ]
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage("token.json")
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        # webbrowser.get('default_browser').open(flow.auth_uri)
        os.system(f'start {flow.auth_uri}')
        creds = tools.run_flow(flow, store)

    form_service = discovery.build(
        "forms",
        "v1",
        http=creds.authorize(Http()),
        discoveryServiceUrl=DISCOVERY_DOC
    )

    form_info = form_service.forms().get(formId=FORM_ID).execute()
    questions = form_info.get('items', [])
    
    response = form_service.forms().responses().list(formId=FORM_ID).execute()
    submissions = response.get("responses", [])

    return (questions, submissions)


if __name__ == '__main__':
    raw_questions, raw_submissions = single_request()
    questions: list[GoogleFormsQuestion] = [GoogleFormsQuestion(question) for question in raw_questions]
    table = SubmissionTable(questions)
    for submission in raw_submissions:
        table.add_submission(submission)
    print('')
    table.to_csv('submissions.csv')