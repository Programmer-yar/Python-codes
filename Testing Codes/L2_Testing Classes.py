import unittest

from survey_class import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ Tests for class AnonymousSurvey """

    def test_store_single_response(self):
        """ test that a single response is stored properly """

        question='What is your mother language?'
        my_survey = AnonymousSurvey(question)
        my_survey.get_response('Saraiki')

        self.assertIn('Saraiki', my_survey.responses)

    def test_store_three_responses(self):
        """ Tests if 3 responses are stored correctly """
        my_survey=AnonymousSurvey('What is your mother language?')
        ch_resp=['urdu', 'saraiki', 'english']
        for response in ch_resp:
            my_survey.get_response(response)

        for response in ch_resp:
            self.assertIn(response, my_survey.responses)

unittest.main()

"""
question='What is your mother language?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()

print("Enter 'q' to exit at any time")

while True:
    response=input("Language: ")
    if response=='q':
        break
    my_survey.get_response(response)

my_survey.show_results()
"""
