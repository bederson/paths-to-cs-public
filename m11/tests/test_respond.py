import unittest, pprint, re, operator, json, os, urllib2, random

class TestRespond(unittest.TestCase):
    def test_respond_add(self):
        bot_name = get_bot_name()
        urllib2.urlopen("http://"+bot_name+".appspot.com/remove_all")

        items_before = len(re.findall('<br>',urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()))
        msg_list = ['Bot! please add "test1"', 'add "test1" and tell me what you did.', 'Hi Bot! can add "test1"?']

        for msg in msg_list:
            response = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(msg)).read()
            expected = "Ok, I've added 'test1' to your todo list at item #"
            self.assertTrue(expected in response, "\n[Expected response to your add command]:\t"+ expected +"...\n[Actual response from your bot]:\t"+response)
        items_after = len(re.findall('<br>', urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()))
        self.assertEqual(items_before + len(msg_list), items_after)

    def test_respond_remove(self):
        bot_name = get_bot_name()
        urllib2.urlopen("http://"+bot_name+".appspot.com/remove_all")
        items_before = len(re.findall('<br>', urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()))
        msg_list = ['Bot! please remove #ID', 'remove #ID and tell me what you did.', 'Hi Bot! can you remove #ID?']
        for msg in msg_list:
            response = urllib2.urlopen("http://"+bot_name+".appspot.com/add?msg=test1").read()
            todo_id_match = re.match(r'(.*)#(.+)$', response)
            if todo_id_match is not None:
                todo_id = todo_id_match.group(2)
                response = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(msg.replace("ID",todo_id))).read()
                expected = "Ok, I've removed item #"+todo_id+" in your todo list"
                self.assertTrue(expected in response, "\n[Expected response to your remove command]:\t"+ expected +"...\n[Actual response from your bot]:\t"+response)
        items_after = len(re.findall('<br>',urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()))
        self.assertEqual(items_before, items_after)


    def test_respond_remove_all(self):
        bot_name = get_bot_name()
        urllib2.urlopen("http://"+bot_name+".appspot.com/remove_all")
        msg_list = ['Bot! please remove all todo items', 'remove all', 'Hi Bot! can you remove all?']
        for msg in msg_list:
            response = urllib2.urlopen("http://"+bot_name+".appspot.com/add?msg="+urllib2.quote(msg)).read()

        response = urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg=remove%20all").read()
        expected = "Ok, I've removed all the itmes in your todo list"
        self.assertEqual(expected, response)
        items_after = len(re.findall('<br>',urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()))
        self.assertEqual(2, items_after, "After 'http://"+bot_name+".appspot.com/remove_all request the list must be zero. However it still contains "+str(items_after-2)+".")

    def test_respond_complete(self):
        bot_name = get_bot_name()
        response = urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()
        completed_items_match = re.match(r'(.*)Completed:(.*)', response)
        completed_items_before = len(re.findall("<br>",completed_items_match.group(2)))
        msg_list = ['Bot! please complete #ID"', 'complete #ID and tell me what you did.', 'Hi Bot! can you complete #ID?']
        for msg in msg_list:
            response = urllib2.urlopen("http://"+bot_name+".appspot.com/add?msg=test1").read()
            todo_id_match = re.match(r'(.*)#(.+)$',response)
            self.assertNotEqual(todo_id_match,None,response+" <-- This response (to your add request) does not contain ID value.")
            if todo_id_match is not None:
                todo_id = todo_id_match.group(2)
                url = "http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(msg.replace("ID",todo_id))
                response = urllib2.urlopen(url).read()
                expected = "Ok, I've marked item #"+todo_id+" as completed in your todo list"
                self.assertTrue(expected in response, "\n[Expected response to your remove command]:\t"+ expected +"...\n[Actual response from your bot]:\t"+response)
        response = urllib2.urlopen("http://"+bot_name+".appspot.com/list").read()
        completed_items_match = re.match(r'(.*)Completed:(.*)',response)
        completed_items_after = len(re.findall("<br>",completed_items_match.group(2)))
        self.assertEqual(completed_items_before+len(msg_list), completed_items_after)

    def test_respond_list(self):
        bot_name = get_bot_name()
        urllib2.urlopen("http://"+bot_name+".appspot.com/remove_all").read()
        msg_list = ["test1", "test2", "test3"]
        id_list = []
        for msg in msg_list:
            response = urllib2.urlopen("http://"+bot_name+".appspot.com/add?msg="+msg).read()
            id_list.append(re.findall(r'#(.+)$', response)[0])
        id_list.reverse()
        msg_list = ['Bot! please show me the list of todo items"', 'list all.', 'todo list!']
        for msg in msg_list:
            list_after_addition= urllib2.urlopen("http://"+bot_name+".appspot.com/respond?msg="+urllib2.quote(msg)).read()
            expected = "To Do:<br>&nbsp;&nbsp;&nbsp;-test3 ["+id_list[0]+"]<br>&nbsp;&nbsp;&nbsp;-test2 ["+id_list[1]+"]<br>&nbsp;&nbsp;&nbsp;-test1 ["+id_list[2]+"]<br>Completed:<br>"
            self.assertEqual(expected, list_after_addition)


def get_bot_name():
        yaml = open("hw11/app.yaml")
        settings = yaml.read()
        m_obj = re.match(r'application: (.+)', settings)
        bot_name = m_obj.group(1)
        return bot_name

unittest.main()