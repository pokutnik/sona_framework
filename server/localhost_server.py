#!/usr/bin/env python
import sys
import posixpath
import urllib
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
from chisel import is_html

class SonaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super(SonaHandler, self).__init__(*args, **kwargs)
        self.extensions_map.update({
            '.css': 'text/css',
            '.less': 'text/css',
            '.xml': 'text/xml',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.jpeg': 'image/jpeg',
            '.jpg': 'image/jpeg',
            '.js': 'application/x-javascript',
            '.htc': 'text/x-component',
            '.ico': 'image/x-icon',
            '.svg': 'image/svg+xml',
            '.swf': 'application/x-shockwave-flash',
            '.zip': 'application/zip',
            '.mp3': 'audio/mpeg',
            })

    def translate_path(self, serve_path):
        """
        The default behavior of SimpleHTTPRequestHandler.translate_path
        is to serve files from the current directory and all of the
        directories below it. This class overrides the method and
        looks for a `rootpath` attribute, which will be used instead
        of the current directory.
        """
        # abandon query parameters
        path = serve_path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = posixpath.normpath(urllib.unquote(path))
        print serve_path, path
        if is_html(path):
            print ">>>> YAY", path
        return super(SonaHandler, self).translate_path(serve_path)

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
