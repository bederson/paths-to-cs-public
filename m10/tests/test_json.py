import unittest, pprint, re, operator, json, os, urllib2

class TestJSON(unittest.TestCase):

    def test_city_not_found(self):
        questions = ["Current weather at Washington d.c. Tell me."]
        bot_name = get_bot_name()
        for q in questions:
            url = "http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(q, '')
            result = urllib2.urlopen(url)
            response = result.read()
            self.assertTrue("Washington d.c. Tell me. is not found." in response, "Your bot responded '"+response+"' to the query '" + q + "'. Instead, your bot should have responded 'Washington d.c. Tell me. is not found.'.")


def get_bot_name():
        yaml = open("hw10/app.yaml")
        settings = yaml.read()
        #print settings
        m_obj = re.match(r'application: (.+)', settings)
        bot_name = m_obj.group(1)
        return bot_name

unittest.main()
