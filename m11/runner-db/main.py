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
import datetime
import webapp2
from google.appengine.ext import db


class Activity(db.Model):
    runner_id = db.StringProperty()
    distance = db.FloatProperty()
    duration = db.FloatProperty()
    date = db.DateProperty()

    def __str__(self):
        return str(self.date) + ": " + str(self.distance) + " miles in " + str(self.duration) + " minutes"


class Runner(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()

    def __str__(self):
        return str(self.key().id()) + ": " + self.name + " (" + self.email + ")"


class AddRunnerHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        email = self.request.get("email")
        runner = Runner()
        runner.name = name
        runner.email = email
        runner.put()


class AddActivityHandler(webapp2.RequestHandler):
    def get(self):
        runner_id = self.request.get("runner_id")
        distance = float(self.request.get("distance"))
        duration = float(self.request.get("duration"))
        run = Activity()
        run.runner_id = runner_id
        run.date = datetime.datetime.now().date()
        run.distance = distance
        run.duration = duration
        run.put()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<b>Runners:</b><br>')
        runner_query = Runner.all()
        runner_query.order("name")
        for runner in runner_query.run():
            self.response.write(runner)
            activity_query = Activity.all()
            activity_query.filter("runner_id = ", str(runner.key().id()))
            activity_query.order("date")
            self.response.write("<ul>")
            for activity in activity_query.run():
                self.response.write("<li>")
                self.response.write(activity)
            self.response.write("</ul>")
            self.response.write("<br>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddRunnerHandler),
    ('/addactivity', AddActivityHandler)
], debug=True)