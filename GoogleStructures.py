class SubmissionTable:
    def __init__(self, questions: list['GoogleFormsQuestion']):
        self.header = [
            'responseId',
            'createTime',
            'lastSubmittedTime'
        ]
        for question in questions:
            self.header.append(question.text)
        self.questions = questions
        self._id_to_q = {q.id: q.text for q in questions}
        self.submissions = {}

    def add_submission(self, submission):
        temp: list = [submission['responseId'], submission['createTime'], submission['lastSubmittedTime']]
        counter: int = 3
        for question_id, answer in submission['answers'].items():
            while self.header[counter] != self._id_to_q[question_id]:
                counter += 1
                if counter >= len(self.header):
                    raise Exception(f'Question {answer["questionId"]} not found')
                temp.append('')
            temp.append(answer['textAnswers']['answers'][0]['value'])
            counter += 1
        self.submissions[submission['responseId']] = temp
        
    def to_csv(self, path, display_outcome: bool = True) -> bool:
        try_again: bool = True
        while try_again:
            try:
                with open(path, 'w') as csv:
                    csv.write(','.join(self.header))
                    for submission in self.submissions.values():
                        csv.write('\n')
                        csv.write(','.join(submission))
                if display_outcome: print(f'✔️ Updated "{path}" successfully')
                return True
            except PermissionError as e:
                print(f"Encountered permission error while triing to write to '{path}'.")
                print("Some process may be using this file... please close the process before trying again.")
                if input("  > try again? (y/n) ") not in ['y', 'yes', 'ye', 'yeah']:
                    try_again = False
        if display_outcome: print(f'❌ Failed to update "{path}"!')
        return False


                
class GoogleFormsQuestion:
    def __init__(self, question_json):
        self.id = question_json['questionItem']['question']['questionId']
        self.text = question_json['title']
        self.itemID = question_json['itemId']