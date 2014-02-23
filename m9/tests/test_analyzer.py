import unittest, pprint, re, operator
from hw9.event import Event
from hw9.collection import Collection
import hw9.analyzer as analyzer
import hw9.geoip as geoip


class TestAnalyzer(unittest.TestCase):

    def test_predicate_page_request(self):
        page_request_regex = r'(html|\/|pdf)$'
        events = [Event(log) for log in TestAnalyzer.log_string.split("\n")]
        for event in events:
            http_request = event.get('http_request')
            url = http_request.split(" ")[1]
            expected_output = len(re.findall(page_request_regex, url)) > 0
            submission_output = analyzer.predicate_page_request(event)
            self.assertEqual(expected_output, submission_output)

    def test_filter_page_request(self):
        collection = Collection([Event(log) for log in TestAnalyzer.log_string.split("\n")])
        submission_output = analyzer.filter_page_requests(collection)
        expected_output = Collection()
        expected_output.load_from_collection(collection)
        expected_output.filter(analyzer.predicate_page_request)
        self.assertEqual(str(expected_output), str(submission_output))

    def test_visitor_country(self):
        collection = Collection([Event(log) for log in TestAnalyzer.log_string.split("\n")])
        pages = analyzer.filter_page_requests(collection)
        country_pageview = {}
        dict_ip_collection = pages.group("ip")
        for ip, col in dict_ip_collection.items():
            country = geoip.country(ip)
            if country not in country_pageview.keys():
                country_pageview[country] = 0
            country_pageview[country] += analyzer.filter_page_requests(col).count()
        expected_output = sorted(country_pageview.items(), reverse=True, key=operator.itemgetter(1))
        submission_output = analyzer.visitor_country(collection)
        self.assertEqual(str(expected_output), str(submission_output))

    def test_popular_pages(self):
        collection = Collection([Event(log) for log in TestAnalyzer.log_string.split("\n")])
        pages = analyzer.filter_page_requests(collection)
        # canonical code
        url_pageview = {}
        dict_req_events = pages.group("http_request")
        for request, col in dict_req_events.items():
            url = request.split(" ")[1]
            if url not in url_pageview.keys():
                url_pageview[url] = 0
            url_pageview[url] += col.count()
        expected_output = sorted(url_pageview.items(), reverse=True, key=operator.itemgetter(1))
        submission_output = analyzer.popular_pages(collection)
        self.assertEqual(str(expected_output), str(submission_output))

    def test_referrers(self):
        collection = Collection([Event(log) for log in TestAnalyzer.log_string.split("\n")])
        pages = analyzer.filter_page_requests(collection)
        # canonical code
        ref_pageview = {}
        ref_groups = pages.group("referrer")
        for referrer in ref_groups.keys():
            if "www.cs.umd.edu/~bederson" in referrer: continue    # ignore referrers within the self domain
            if referrer not in ref_pageview.keys():
                ref_pageview[referrer] = 0
            ref_pageview[referrer] += ref_groups[referrer].count()

        def cmp_count(x, y):
            return x[1] - y[1]

        expected_output = sorted(ref_pageview.items(), reverse=True, cmp=cmp_count)
        submission_output = analyzer.referrers(collection)
        self.assertEqual(str(expected_output), str(submission_output))

    log_string = '''78.242.96.205 - - [29/Sep/2013:09:49:57 -0400] "GET /~bederson HTTP/1.1" 301 240 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.110 Safari/537.36 Squider/0.01"
192.35.35.35 - - [29/Sep/2013:09:50:42 -0400] "GET /~bederson/images/hcil-logo-small.gif HTTP/1.1" 304 - "-" "Mozilla/4.0 (compatible;)"
203.122.235.196 - - [29/Sep/2013:10:19:11 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
61.90.177.243 - - [29/Sep/2013:10:32:42 -0400] "GET /~bederson/js/utils.js HTTP/1.1" 304 - "-" "Mozilla/4.0 (compatible;)"
58.5.61.217 - - [29/Sep/2013:10:37:41 -0400] "GET /~bederson/js/constants.js HTTP/1.1" 200 1574 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:41 -0400] "GET /~bederson/js/utils.js HTTP/1.1" 200 1070 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:41 -0400] "GET /~bederson/jquery.min.js HTTP/1.1" 200 94840 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:41 -0400] "GET /~bederson/js/vis.js HTTP/1.1" 200 14612 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:41 -0400] "GET /~bederson/js/pubs.js HTTP/1.1" 200 11147 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:42 -0400] "GET /~bederson/papers/index.js HTTP/1.1" 200 1505 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:43 -0400] "GET /~bederson/images/hcil-logo-small.gif HTTP/1.1" 200 2060 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:43 -0400] "GET /~bederson/images/tr-curve-white.gif HTTP/1.1" 200 58 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
58.5.61.217 - - [29/Sep/2013:10:37:43 -0400] "GET /~bederson/images/bg-grad.jpg HTTP/1.1" 200 1907 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:10:49:08 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
89.176.226.191 - - [29/Sep/2013:10:57:07 -0400] "GET /~bederson/papers/index.html HTTP/1.1" 200 3549 "-" "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53"
89.176.226.191 - - [29/Sep/2013:10:57:07 -0400] "GET /~bederson/index.css HTTP/1.1" 200 4766 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53"
89.176.226.191 - - [29/Sep/2013:10:57:07 -0400] "GET /~bederson/js/pubs.js HTTP/1.1" 200 11147 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53"
89.176.226.191 - - [29/Sep/2013:10:57:07 -0400] "GET /~bederson/jquery.min.js HTTP/1.1" 200 94840 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53"
89.176.226.191 - - [29/Sep/2013:10:57:08 -0400] "GET /~bederson/papers/index.js HTTP/1.1" 200 1505 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53"
89.176.226.191 - - [29/Sep/2013:10:57:09 -0400] "GET /~bederson/images/tr-curve-white.gif HTTP/1.1" 200 58 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53"
78.52.146.148 - - [29/Sep/2013:11:08:56 -0400] "GET /~bederson/papers/index.html HTTP/1.1" 200 3549 "-" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
78.52.146.148 - - [29/Sep/2013:11:08:57 -0400] "GET /~bederson/index.css HTTP/1.1" 200 4766 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
78.52.146.148 - - [29/Sep/2013:11:08:57 -0400] "GET /~bederson/js/vis.js HTTP/1.1" 200 14612 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
78.52.146.148 - - [29/Sep/2013:11:08:57 -0400] "GET /~bederson/js/pubs.js HTTP/1.1" 200 11147 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
78.52.146.148 - - [29/Sep/2013:11:08:59 -0400] "GET /~bederson/images/hcil-logo-small.gif HTTP/1.1" 200 2060 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:11:19:10 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
200.23.91.154 - - [29/Sep/2013:11:34:04 -0400] "GET /~bederson/js/utils.js HTTP/1.1" 304 - "-" "Mozilla/4.0 (compatible;)"
81.52.143.15 - - [29/Sep/2013:11:37:18 -0400] "GET /~bederson/talks/ HTTP/1.1" 200 2716 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)"
203.122.235.196 - - [29/Sep/2013:11:49:03 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
217.224.140.242 - - [29/Sep/2013:11:51:33 -0400] "GET /~bederson/images/pubs_pdfs/p23-bederson.pdf HTTP/1.1" 200 332665 "http://www.google.de/url?sa=t&rct=j&q=&esrc=s&source=web&cd=166&cad=rja&ved=0CFoQFjAFOKAB&url=http%3A%2F%2Fwww.cs.umd.edu%2F~bederson%2Fimages%2Fpubs_pdfs%2Fp23-bederson.pdf&ei=80tIUtSgD4zDtAb01IGICA&usg=AFQjCNFkbZB_DsrlUOLFu1-t1tNDvcVNDQ&bvm=bv.53217764,d.Yms" "Mozilla/5.0 (X11; FreeBSD amd64; rv:17.0) Gecko/17.0 Firefox/17.0"
63.152.85.12 - - [29/Sep/2013:12:15:57 -0400] "GET /~bederson/js/vis.js HTTP/1.1" 200 14612 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
63.152.85.12 - - [29/Sep/2013:12:15:57 -0400] "GET /~bederson/js/pubs.js HTTP/1.1" 200 11147 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
63.152.85.12 - - [29/Sep/2013:12:15:58 -0400] "GET /~bederson/images/tr-curve-white.gif HTTP/1.1" 200 58 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
63.152.85.12 - - [29/Sep/2013:12:15:58 -0400] "GET /~bederson/images/hcil-logo-small.gif HTTP/1.1" 200 2060 "http://www.cs.umd.edu/~bederson/papers/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36"
203.122.235.196 - - [29/Sep/2013:12:19:03 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
116.64.12.66 - - [29/Sep/2013:12:36:42 -0400] "GET /~bederson/papers/index.html HTTP/1.1" 200 3549 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:43 -0400] "GET /~bederson/index.css HTTP/1.1" 200 4766 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:43 -0400] "GET /~bederson/js/vis.js HTTP/1.1" 200 14612 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:43 -0400] "GET /~bederson/js/utils.js HTTP/1.1" 200 1070 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:43 -0400] "GET /~bederson/papers/index.js HTTP/1.1" 200 1505 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:43 -0400] "GET /~bederson/jquery.min.js HTTP/1.1" 200 94840 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:43 -0400] "GET /~bederson/js/d3.v2.js HTTP/1.1" 200 255064 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:45 -0400] "GET /~bederson/images/tr-curve-white.gif HTTP/1.1" 200 58 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:45 -0400] "GET /~bederson/images/tl-curve-white.gif HTTP/1.1" 200 59 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:45 -0400] "GET /~bederson/images/bg-grad.jpg HTTP/1.1" 200 1907 "http://www.cs.umd.edu/~bederson/index.css" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
116.64.12.66 - - [29/Sep/2013:12:36:45 -0400] "GET /~bederson/images/hcil-logo-small.gif HTTP/1.1" 200 2060 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0"
203.122.235.196 - - [29/Sep/2013:12:49:21 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
93.137.1.52 - - [29/Sep/2013:12:57:02 -0400] "GET /~bederson/user-advocate/atom.xml HTTP/1.1" 404 230 "-" "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.15"
46.249.171.131 - - [29/Sep/2013:13:00:34 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 65536 "http://scholar.google.lt/scholar?q=Personal+information+management&hl=lt&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=31tIUtSIFKvQ4QTv-oD4Dg&ved=0CCwQgQMwAA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
46.249.171.131 - - [29/Sep/2013:13:00:37 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 52232 "http://scholar.google.lt/scholar?q=Personal+information+management&hl=lt&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=31tIUtSIFKvQ4QTv-oD4Dg&ved=0CCwQgQMwAA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
46.249.171.131 - - [29/Sep/2013:13:00:37 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 65536 "http://scholar.google.lt/scholar?q=Personal+information+management&hl=lt&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=31tIUtSIFKvQ4QTv-oD4Dg&ved=0CCwQgQMwAA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
46.249.171.131 - - [29/Sep/2013:13:00:37 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 65536 "http://scholar.google.lt/scholar?q=Personal+information+management&hl=lt&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=31tIUtSIFKvQ4QTv-oD4Dg&ved=0CCwQgQMwAA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
46.249.171.131 - - [29/Sep/2013:13:00:38 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 65536 "http://scholar.google.lt/scholar?q=Personal+information+management&hl=lt&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=31tIUtSIFKvQ4QTv-oD4Dg&ved=0CCwQgQMwAA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
46.249.171.131 - - [29/Sep/2013:13:00:38 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 65536 "http://scholar.google.lt/scholar?q=Personal+information+management&hl=lt&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=31tIUtSIFKvQ4QTv-oD4Dg&ved=0CCwQgQMwAA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
119.246.207.206 - - [29/Sep/2013:13:13:18 -0400] "GET /~bederson/images/pubs_pdfs/p40-teevan.pdf HTTP/1.1" 206 331173 "http://www.cs.umd.edu/~bederson/images/pubs_pdfs/p40-teevan.pdf" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22"
203.122.235.196 - - [29/Sep/2013:13:19:09 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
66.249.66.185 - - [29/Sep/2013:13:23:39 -0400] "GET /~bederson/press/dn-aug-99.shtml HTTP/1.1" 404 229 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
203.122.235.196 - - [29/Sep/2013:13:49:20 -0400] "GET /~bederson/user-advocate/rss.xml HTTP/1.1" 404 229 "-" "NetNewsWire/3.3.2 (Mac OS X; http://netnewswireapp.com/mac/; gzip-happy)"
66.249.66.185 - - [29/Sep/2013:13:51:17 -0400] "GET /~bederson/user-advocate/2007/01/in-defense-of-challenge-response-spam.html HTTP/1.1" 302 281 "-" "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
66.249.66.9 - - [29/Sep/2013:13:51:17 -0400] "GET /~bederson/user-advocate/2007/01/in-defense-of-challenge-response-spam.html HTTP/1.1" 404 272 "-" "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
216.200.93.185 - - [29/Sep/2013:13:55:49 -0400] "GET /~bederson/papers/index.html HTTP/1.1" 200 3549 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0"
216.200.93.185 - - [29/Sep/2013:13:55:49 -0400] "GET /~bederson/index.css HTTP/1.1" 200 4766 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0"
216.200.93.185 - - [29/Sep/2013:13:55:49 -0400] "GET /~bederson/js/constants.js HTTP/1.1" 200 1574 "http://www.cs.umd.edu/~bederson/papers/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0"'''


unittest.main()