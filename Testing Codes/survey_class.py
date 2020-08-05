class AnonymousSurvey():
    """ Collect anonymous answers to a survey question. """

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """ simply prints a question """
        print(self.question)

    def get_response(self, random_response):
        """ gets a response and stores it """
        self.responses.append(random_response)

    def show_results(self):
        """ displays all the responses """
        print("survey results: ")
            
        for response in self.responses:
            print("- ", response)

            
"""
e_survey=AnonymousSurvey('what do you like')
e_survey.get_response('rice')
"""
