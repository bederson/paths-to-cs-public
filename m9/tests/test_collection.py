import unittest, pprint
from hw9.event import Event
from hw9.collection import Collection
import hw9.analyzer as analyzer


class TestCollection(unittest.TestCase):
    log_string = '''157.55.32.98 - - [29/Sep/2013:03:37:38 -0400] "GET /~bederson/images/pubs_pdfs/p203-parhi.pdf HTTP/1.1" 200 497931 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
218.104.71.166 - - [29/Sep/2013:04:28:31 -0400] "GET /~bederson/images/bederson.jpg HTTP/1.1" 200 32133 "http://arnetminer.org/" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:04:48:09 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
203.122.235.196 - - [29/Sep/2013:05:18:16 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
88.191.122.6 - - [29/Sep/2013:05:25:39 -0400] "GET /~bederson/user-advocate/atom.xml HTTP/1.0" 302 239 "-" "Feedshow/2.0 (http://www.feedshow.com; 1 subscriber)"
93.197.125.158 - - [29/Sep/2013:05:32:40 -0400] "GET /~bederson/js/utils.js HTTP/1.1" 200 1070 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
93.197.125.158 - - [29/Sep/2013:05:32:40 -0400] "GET /~bederson/js/constants.js HTTP/1.1" 200 1574 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
93.197.125.158 - - [29/Sep/2013:05:32:40 -0400] "GET /~bederson/js/vis.js HTTP/1.1" 200 14612 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
93.197.125.158 - - [29/Sep/2013:05:32:40 -0400] "GET /~bederson/papers/index.js HTTP/1.1" 200 1505 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
93.197.125.158 - - [29/Sep/2013:05:32:40 -0400] "GET /~bederson/js/d3.v2.js HTTP/1.1" 200 255064 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
93.197.125.158 - - [29/Sep/2013:05:32:41 -0400] "GET /~bederson/images/bg-grad.jpg HTTP/1.1" 200 1907 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
93.197.125.158 - - [29/Sep/2013:05:32:41 -0400] "GET /~bederson/images/hcil-logo-small.gif HTTP/1.1" 200 2060 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"
123.125.71.88 - - [29/Sep/2013:05:44:18 -0400] "GET /~bederson/classes/dui-spring-2002/lecture-notes/intro/hello-world-applet.cs HTTP/1.1" 404 273 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
203.122.235.196 - - [29/Sep/2013:05:49:13 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
65.55.24.239 - - [29/Sep/2013:05:57:48 -0400] "GET /~bederson/user-advocate/2009/06/why-gmail-doesnt-let-you-sort-by-size.html HTTP/1.1" 404 272 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
203.122.235.196 - - [29/Sep/2013:06:19:10 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
116.202.24.126 - - [29/Sep/2013:06:24:24 -0400] "GET /~bederson/js/constants.js HTTP/1.1" 200 1574 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0"
116.202.24.126 - - [29/Sep/2013:06:24:24 -0400] "GET /~bederson/js/utils.js HTTP/1.1" 200 1070 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0"
116.202.24.126 - - [29/Sep/2013:06:24:24 -0400] "GET /~bederson/js/pubs.js HTTP/1.1" 200 11147 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0"'''

    def test_filter_basic(self):
        log_string = '''157.55.32.98 - - [29/Sep/2013:03:37:38 -0400] "GET /~bederson/images/pubs_pdfs/p203-parhi.pdf HTTP/1.1" 200 497931 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
218.104.71.166 - - [29/Sep/2013:04:28:31 -0400] "GET /~bederson/images/bederson.jpg HTTP/1.1" 200 32133 "http://arnetminer.org/" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:04:48:09 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"'''
        collection = Collection([Event(log) for log in log_string.split("\n")])

        def predicate_ip_contains_196(event):
            return "196" in event.get("ip")

        collection.filter(predicate_ip_contains_196)
        expected_collection = Collection([Event(
            '203.122.235.196 - - [29/Sep/2013:04:48:09 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"')])
        self.assertEqual(str(expected_collection), str(collection))

    def test_filter_block_everything(self):
        log_string = '''157.55.32.98 - - [29/Sep/2013:03:37:38 -0400] "GET /~bederson/images/pubs_pdfs/p203-parhi.pdf HTTP/1.1" 200 497931 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
218.104.71.166 - - [29/Sep/2013:04:28:31 -0400] "GET /~bederson/images/bederson.jpg HTTP/1.1" 200 32133 "http://arnetminer.org/" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:04:48:09 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"'''
        collection = Collection([Event(log) for log in log_string.split("\n")])

        def predicate_block_everything(event):
            return False

        collection.filter(predicate_block_everything)
        expected_collection = Collection()
        self.assertEqual(str(expected_collection), str(collection))

    def test_group_ip(self):
        collection = Collection([Event(log) for log in TestCollection.log_string.split("\n")])
        group_dict = collection.group("ip")
        expected_output = ['116.202.24.126', '123.125.71.88', '157.55.32.98', '203.122.235.196', '218.104.71.166',
                           '65.55.24.239', '88.191.122.6', '93.197.125.158']
        self.assertEqual(expected_output, sorted(group_dict.keys()))

    def test_group_http_request(self):
        collection = Collection([Event(log) for log in TestCollection.log_string.split("\n")])
        group_dict = collection.group("http_request")
        expected_output = ['GET /~bederson/classes/dui-spring-2002/lecture-notes/intro/hello-world-applet.cs HTTP/1.1',
                           'GET /~bederson/images/bederson.jpg HTTP/1.1', 'GET /~bederson/images/bg-grad.jpg HTTP/1.1',
                           'GET /~bederson/images/hcil-logo-small.gif HTTP/1.1',
                           'GET /~bederson/images/pubs_pdfs/p203-parhi.pdf HTTP/1.1',
                           'GET /~bederson/js/constants.js HTTP/1.1', 'GET /~bederson/js/d3.v2.js HTTP/1.1',
                           'GET /~bederson/js/pubs.js HTTP/1.1', 'GET /~bederson/js/utils.js HTTP/1.1',
                           'GET /~bederson/js/vis.js HTTP/1.1', 'GET /~bederson/papers/index.js HTTP/1.1',
                           'GET /~bederson/user-advocate/2009/06/why-gmail-doesnt-let-you-sort-by-size.html HTTP/1.1',
                           'GET /~bederson/user-advocate/atom.xml HTTP/1.0',
                           'GET /~bederson/user-advocate/rss.xml HTTP/1.1']
        self.assertEqual(expected_output, sorted(group_dict.keys()))

    def test_comparator_ip(self):
        event1 = Event(
            '157.55.32.98 - - [29/Sep/2013:03:37:38 -0400] "GET /~bederson/images/pubs_pdfs/p203-parhi.pdf HTTP/1.1" 200 497931 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"')
        event2 = Event(
            '93.197.125.158 - - [29/Sep/2013:05:32:40 -0400] "GET /~bederson/js/constants.js HTTP/1.1" 200 1574 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.81 Safari/537.1"')
        self.assertTrue(analyzer.comparator_ip(event1, event2) < 0)

    def test_sort_ip(self):
        log_string = '''157.55.32.98 - - [29/Sep/2013:03:37:38 -0400] "GET /~bederson/images/pubs_pdfs/p203-parhi.pdf HTTP/1.1" 200 497931 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
218.104.71.166 - - [29/Sep/2013:04:28:31 -0400] "GET /~bederson/images/bederson.jpg HTTP/1.1" 200 32133 "http://arnetminer.org/" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:04:48:09 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"'''
        collection = Collection([Event(log) for log in log_string.split("\n")])
        collection.sort(analyzer.comparator_ip)
        submission_output = [e.get("ip") for e in collection.get_events()]
        expected_output = ['218.104.71.166','203.122.235.196','157.55.32.98']
        self.assertEqual(expected_output, submission_output)


unittest.main()