import unittest, string, random, pprint, re, operator, json, os, urllib2


class TestAdd(unittest.TestCase):
    def test_add(self):
        txt = "test"+str(random.randint(0,10))
        msg = 'add "'+txt+'"'

        bot_name= "path-reminder"
        urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote("remove all"))
        expected= urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(msg)).read()
        expected = re.sub(r'([0-9]){5,}.*', r'...', expected)

        bot_name = get_bot_name()
        urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote("remove all"))
        submitted = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(msg)).read()
        submitted = re.sub(r'([0-9]){5,}.*',r'...',submitted)

        self.assertEqual(expected, submitted, "\nWhen a new todo item is added to the datastore,...\n[Expected response]:\t"+ expected +"...\n[Actual response from your bot]:\t"+submitted)



def get_bot_name():
        yaml = open("hw12/app.yaml")
        settings = yaml.read()
        m_obj = re.match(r'application: (.+)', settings)
        bot_name = m_obj.group(1)
        return bot_name

unittest.main()
