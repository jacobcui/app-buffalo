"""Helper module."""

import jinja2
import webapp2

import settings

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_template(html_name):
  return JINJA_ENVIRONMENT.get_template(html_name)

def render_template(html_name, template_values):
  template = get_template(html_name)
  return template.render(template_values)
