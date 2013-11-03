#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
from google.appengine.api import urlfetch

class MainHandler(webapp2.RequestHandler):
    def get(self):
        word = self.request.get("word")
        if word:
            url = "http://glosbe.com/gapi/translate?from=eng&dest=eng&phrase=" + word + "&format=json"
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                data_str = result.content
                data = json.loads(data_str)
                tuc = data["tuc"][0]
                meanings = tuc["meanings"]

                self.response.write("<html><body>\n")
                self.response.write("Definitions of <b>" + word + ":</b><br>\n")
                self.response.write("<ul>\n")
                for meaning in meanings:
                    self.response.write("<li>" + meaning["text"] + "<br>\n")
                self.response.write("</ul>\n")
                self.response.write("</body></html>")
        else:
            self.response.write("Usage: ?word=&lt;word&gt;")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
