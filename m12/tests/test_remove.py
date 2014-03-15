import unittest, string, random, pprint, re, operator, json, os, urllib2


class TestRemove(unittest.TestCase):
    def test_remove(self):
        txt = "test"+str(random.randint(0,10))
        msg = 'add%20"'+txt+'"'

        bot_name= "path-reminder"
        urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg=remove%20all")
        response = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+msg).read()
        item_id = re.findall(r'your todo list at item ([0-9]+)\.', response)[0]
        expected = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg=remove%20"+item_id).read()
        expected = re.sub(r'[0-9]',r'...',expected)

        bot_name = get_bot_name()
        urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg=remove%20all")
        response = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+msg).read()
        item_id = re.findall(r'your todo list at item ([0-9]+)\.', response)[0]
        submitted = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg=remove%20"+item_id).read()
        submitted = re.sub(r'[0-9]',r'...',submitted)

        self.assertEqual(expected, submitted, "\nWhen a todo item is removed...\n[Expected response]:\t"+ expected +"...\n[Submitted response]:\t"+submitted)



def get_bot_name():
        yaml = open("hw12/app.yaml")
        settings = yaml.read()
        m_obj = re.match(r'application: (.+)', settings)
        bot_name = m_obj.group(1)
        return bot_name

unittest.main()
