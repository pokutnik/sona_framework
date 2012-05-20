#!/usr/bin/env python
import sys
import os
import posixpath
import urllib
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
from chisel import is_html, update_url
from chisel import DESTINATION


class SonaHandler(SimpleHTTPRequestHandler):
    def translate_path(self, serve_path):
        """
        Trigger rerender for html files.
        Serve file form destination folder.
        """
        path = serve_path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = posixpath.normpath(urllib.unquote(path))
        path = SimpleHTTPRequestHandler.translate_path(self, path)
        url = path
        if is_html(path):
            update_url(url)
            d, f = os.path.split(path)
            path = os.path.join(d, DESTINATION, f)
            path = posixpath.normpath(path)
            print ">>>> YAY", path

        return path


if __name__ == '__main__':
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 80
    server_address = ('', port)
    httpd = BaseHTTPServer.HTTPServer(server_address, SonaHandler)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    print "Open  http://%s:%s/" % (sa[0], sa[1])
    httpd.serve_forever()
