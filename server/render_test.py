# -*- coding: utf-8 -*-
import mock
from nose import tools as t
from render import render_dir


@mock.patch('render.os.listdir')
def test_should_render(listdir_mock):
    listdir_mock.return_value = ['test']
    page = render_dir('/', '')
    t.eq_(page, u'<a href="/test">test</a><br />')
