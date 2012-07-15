#!/usr/bin/env python
import sys
from bottle import run, route, Bottle, static_file, debug, redirect
from bottle import request
from config import STATIC_URLS, ROOT
from render import render_url, is_index, render_dir, is_dir

app = Bottle()

def is_static_url(url):
    for static in STATIC_URLS:
        if url.startswith(static):
            return True


@route("<url:path>")
def server_css(url):
    if is_dir(url):
        if is_index(url):
            return redirect(url + 'index.html')
        else:
            return render_dir(url, ROOT)

    if is_static_url(url):
        return static_file(url, ROOT)

    if url.endswith('.html'):
        return render_url(request.path, {'dev': True})


    return static_file(url, ROOT)


if __name__ == '__main__':
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 80
    
    debug(True)
    run(host='0.0.0.0', port=port)
