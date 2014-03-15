import unittest, pprint, re, operator, json, os, urllib2

class TestRegex(unittest.TestCase):

    def test_valid_weather_question(self):
        questions = ["Hi, bot! What's the weather at Washington d.c.? Tell me.", "WEATHER IN Washington d.c.", "WEATHER of Washington D.C.", "How's the weather in washington d.c.?"]
        bot_name = get_bot_name()
        for q in questions:
            url = "http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(q, '')
            result = urllib2.urlopen(url)
            response = result.read()
            self.assertTrue("The current weather at Washington is" in response, "Your bot responded '"+response+"' to the query '" + q + "'. Instead, your bot should have responded 'The current weather at Washington is...'.")


    def test_non_weather_questions(self):
        invalid_questions = ["WEATHER from Washington D.C.?", "Is is clear in Washington D.C.?"]
        bot_name = get_bot_name()
        for q in invalid_questions:
            url = "http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(q, '')
            result = urllib2.urlopen(url)
            response = result.read()
            self.assertTrue("Thanks for saying" in response, "Your bot responded '"+response+"' to the query '" + q + "'. Instead, your bot should have responded 'Thanks for saying...'.")


def get_bot_name():
        yaml = open("hw10/app.yaml")
        settings = yaml.read()
        #print settings
        m_obj = re.match(r'application: (.+)', settings)
        bot_name = m_obj.group(1)
        return bot_name

unittest.main()
