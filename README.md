
![](https://raw.githubusercontent.com/epykure/epyk-tornado/master/static/images/logo.ico)

# Epyk Tornado!


An easy way to use Epyk within a Tornado Web App

## Quickstart

Install Tornado

> pip install tornado

Install Epyk

> pip install epyk

Then create your first on demand report leveraging on Tornado
```py
import tornado.ioloop
import tornado.web

# Epyk is needed for the on demand report generation
from epyk.core.Page import Report

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
        (r"/dynamic", MainOnTheFlyHandler),
    ])
```

## Presentation

This repository is quite simple to show case the use of Epyk.

<div align="center" >
    <img src="https://github.com/marlyk/epyk-uvicorn/blob/master/static/images/details.PNG?raw=true">
</div>


This package will make a simple interface between the back and the front end generation.
For advanced use of Tornado please refer to the [official website](https://www.tornadoweb.org/en/stable/)

This repository will deal with common and simple example to demonstrate how to integrate Epyk to your Tornado static.

Epyk can be used in two different ways:

- Generating static or semi static (with Jinja) templates which will then be updated by Tornado
- Producing on the fly template within the views

This project will provide example on the different ways of using Epyk templates.

## Design Principle
The design is similar to any moder web server the different here is that the code is generated from Python.
Epyk is designed to generate a rich HTML and JavaScript code which can be used by any browser.

The code will rely by default on external JavaScript packages which will be retrieved from CDNJS directly.

It is possible to install the packages locally from the npm command and to use this directly.

The standatd design is as below. Namely Epyk pages are used to generate HTML artefact which will then be used directly by the 
server the render the page.

It is possible also to generate the page on the fly, it the structure of the page is quite different.
This can easily adapt the page to the data without having to create multiple static reports.

<div align="center" >
    <img src="https://github.com/epykure/epyk-tornado/blob/master/static/images/server_archi_1.PNG?raw=truee">
</div>

The concept is quite simple and it is based on components. Epyk is structure in simple components with some predefined styles and events.
Nearly all the CSS properties, ARIA information and JavaScript functions have been wrapped in this module to allow you to nearly to everything from Python.

No need to change code anymore or to maintain multiple static templates.
 
<div align="center" >
    <img src="https://github.com/epykure/epyk-tornado/blob/master/static/images/server_archi_2.PNG?raw=true">
</div>


On teh server side for complex component, the data module will provide you with simple function to convert the data to the right format.

<div align="center" >
    <img src="https://github.com/epykure/epyk-tornado/blob/master/static/images/server_archi_3.PNG?raw=true">
</div>

## Benefits

- No need anymore to maintain multiple folder with various styles and template. This can be managed by inheritance directly on the Python Layer.
- No need to install or import the right modules to your app. Components will build the page and add dynamically the necessary external packages.
- No need to reimplement / restructure your templates based on the target server (inddeed this will have multiple output to adpatd according to the target server)



Do not hesitate to propose new examples !