import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

class SonaHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwsrgs):
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

if __name__ == '__main__':
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 80
    server_address = ('', port)
    httpd = BaseHTTPServer.HTTPServer(server_address, SimpleHTTPRequestHandler)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()
