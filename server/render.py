# -*- coding: utf-8 -*-
import os
import jinja2
from config import TEMPLATE_PATH, SOURCE


jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


def render_template(template, context):
    return jinja2_env.from_string(template).render(context)


def template_filter(func):
    " decorator to easily create jinja2 filters "
    jinja2_env.filters[func.__name__] = func


def render_url(url, context={}):
    with open(path_to(url), "rU") as f:
        template = f.read().decode('utf-8')
        html = render_template(template, {})
    return html


def path_to(url):
    if url[0] == '/':
        url = url[1:]
    path = os.path.join(SOURCE, url)
    return path


def is_index(url):
    return os.path.exists(path_to(url) + 'index.html')
