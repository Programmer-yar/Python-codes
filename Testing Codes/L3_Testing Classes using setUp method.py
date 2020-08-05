import unittest

from survey_class import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ Tests for class AnonymousSurvey """

    def setUp(self):
        """
        creates object/survey and set of responses which can be used
        in every method
        """
        question='What is your mother language?'
        self.my_survey=AnonymousSurvey(question)
        self.sample_responses=['urdu', 'saraiki', 'english']

    def test_store_single_response(self):
        """ test that a single response is stored properly """

        self.my_survey.get_response(self.sample_responses[1])

        self.assertIn('saraiki', self.my_survey.responses)

    def test_store_three_responses(self):
        """ Tests if 3 responses are stored correctly """
        
        for response in self.sample_responses:
            self.my_survey.get_response(response)

        for response in self.sample_responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
