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
import os
import jinja2
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.api import taskqueue


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

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

        self.response.write("Runner added: " + runner.name)
        taskqueue.add(method="GET", url="/sendsummary", params={"msg": "Runner added"})


class AddActivityHandler(webapp2.RequestHandler):
    def get(self):
        runner_id = self.request.get("runner_id")
        distance = float(self.request.get("distance"))
        duration = float(self.request.get("duration"))
        activity = Activity()
        activity.runner_id = runner_id
        activity.date = datetime.datetime.now().date()
        activity.distance = distance
        activity.duration = duration
        activity.put()

        self.response.write("Activity added: " + str(distance) + " miles")
        taskqueue.add(method="GET", url="/sendsummary", params={"msg": "Activity added"})


class MailSummaryHandler(webapp2.RequestHandler):
    def get(self):
        runner_query = Runner.all()
        runner_query.order("name")
        for runner in runner_query.run():
            body = "<b>Running summary for " + runner.name + ":</b><br>"
            body += str(runner)
            activity_query = Activity.all()
            activity_query.filter("runner_id = ", str(runner.key().id()))
            activity_query.order("date")
            body += "<ul>"
            for activity in activity_query.run():
                body += "<li>"
                body += str(activity)
            body += "</ul>"
            msg = self.request.get("msg")
            if msg:
                body += "<br><br>"
                body += "This message sent because: " + msg

            runner_to = runner.name + " <" + runner.email + ">"
            message = mail.EmailMessage(sender="Ben Bederson <bederson@gmail.com>",
                                        subject="Your running summary")
            message.to = runner_to
            message.html = body   # Or could use ".body"
            message.send()

            self.response.write("Message sent successfully to " + runner_to + "<br>")


class MainHandler(webapp2.RequestHandler):
    def get(self):
        runner_query = Runner.all()
        runner_query.order("name")
        runners = []
        for runner in runner_query.run():
            activity_query = Activity.all()
            activity_query.filter("runner_id = ", str(runner.key().id()))
            activity_query.order("date")
            runner.activities = []
            for activity in activity_query.run():
                runner.activities.append(activity)
            runners.append(runner)

        template_values = {
            "runners": runners
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/addrunner', AddRunnerHandler),
    ('/addactivity', AddActivityHandler),
    ('/sendsummary', MailSummaryHandler)
], debug=True)