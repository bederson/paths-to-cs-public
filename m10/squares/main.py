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

class MainHandler(webapp2.RequestHandler):
    """
    Simple GAE app to return a list of squares in JSON
    Usage: localhost:8080/?start=###&num_squares=###
    """
    def squares(self, start, num_squares):
        squares_dict = {}
        for i in range(start, start+num_squares):
            squares_dict[i] = i*i
        return squares_dict

    def get(self):
        start = 0
        start_str = self.request.get("start")
        if start_str:
            start = int(start_str)
        num_squares = 10
        num_squares_str = self.request.get("num_squares")
        if num_squares_str:
            num_squares = int(num_squares_str)
        self.response.write(json.dumps(self.squares(start, num_squares)))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
