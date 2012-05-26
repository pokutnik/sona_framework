# -*- coding: utf-8 -*-
import os


def here(*x):
    return os.path.abspath(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), *x))

ROOT = here('..')
SOURCE = ROOT
DESTINATION = here('../export')
TEMPLATE_PATH = here("../templates")
CSS_DIR = here("../css")
IMAGES_DIR = here("../images")
SEVER_PATH = here('.')

SKIP_PATHS = [
        DESTINATION,
        TEMPLATE_PATH,
        SEVER_PATH,
        ROOT + '/.',
        here('../.git'),
        here('../doc'),
    ]

STATIC_URLS = [
        '/css/',
        '/images/',
        '/docs/',
        '/export/',
        '/js/',
    ]


if __name__ == '__main__':
    # Debug current config output
    from pprint import pprint
    pprint(locals())
