import os

import tornado.ioloop
import tornado.web

# Epyk is needed for the on demand report generation
from epyk.core.Page import Report

cur_dir = os.path.dirname(os.path.abspath(__file__))


class MainStaticHandler(tornado.web.RequestHandler):
    def get(self):
     with open(os.path.join(cur_dir, "views", "chart.html")) as f:
       self.write(f.read())


class MainJinjaHandler(tornado.web.RequestHandler):
  def get(self):
    self.render(os.path.join(cur_dir, "views", "index.html"), name='Hello World')


class MainOnTheFlyHandler(tornado.web.RequestHandler):
  def get(self):
    page = Report()
    page.headers.dev()
    div = page.ui.div("Hellow World!")
    button = page.ui.button("Click Me")
    div.style.css.color = 'red'
    button.click([
      page.js.alert("Clicked")
    ])

    self.write(page.outs.html())


def make_app():
    return tornado.web.Application([
        (r"/jinja", MainJinjaHandler),
        (r"/chart", MainStaticHandler),
        (r"/dynamic", MainOnTheFlyHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
