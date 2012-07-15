# -*- coding: utf-8 -*-
from nose import tools as t
from webtest import TestApp
from localhost_server import app


def test_should_render_index_page():
    server = TestApp(app)
    response = server.get(r'/')

def test_should_render_index_html_page():
    server = TestApp(app)
    response = server.get(r'/index.html')

def test_should_render_test_page():
    server = TestApp(app)
    response = server.get(r'/test.html')

def test_should_render_static():
    server = TestApp(app)
    response = server.get(r'/css/sona/sortcuts.less')
