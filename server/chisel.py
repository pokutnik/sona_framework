#!/usr/bin/python

# Based on Chisel by David Zhou
#
import sys
import os
import shutil

# Settings


_STEPS = []

from config import SOURCE, DESTINATION, SKIP_PATHS
from render import render_url, path_to


def step(func):
    def wrapper(*args, **kwargs):
        print
        print "Starting " + func.__name__ + "...",
        func(*args, **kwargs)
        print "Done."
    _STEPS.append(wrapper)
    return wrapper


def is_dot(filename):
    return filename and filename[0] == '.'


def is_sub(parent, subfolder):
    return os.path.abspath(subfolder).startswith(
                os.path.abspath(parent))


def can_skip(filename):
    for skip in SKIP_PATHS:
        if filename.startswith(skip):
            return True


def ensure_destination():
    if not os.path.exists(DESTINATION):
        os.makedirs(DESTINATION)


def get_tree(source):
    files = []
    rel = lambda fname: fname[len(source):]

    for root, ds, fs in os.walk(source):
        if is_dot(rel(root)) or can_skip(root):
            continue
        for name in fs:
            print '>', root, name
            if is_dot(name):
                continue
            path = os.path.join(root, name)
            rel_path = rel(path)
            print "+", rel_path
            mtime = os.path.getmtime(path)
            with open(path, "rU") as f:
                files.append({
                    'content': ''.join(f.readlines()),
                    'filename': name,
                    'url': rel_path,
                    'path': path,
                    'name': name,
                    'mtime': mtime,
                })
    return files


def compare_entries(x, y):
    result = cmp(-x['mtime'], -y['mtime'])
    if result == 0:
        return -cmp(x['filename'], y['filename'])
    return result


def write_file(url, data):
    path = DESTINATION + url
    dirs = os.path.dirname(path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    file = open(path, "w")
    file.write(data.encode('UTF-8'))
    file.close()
    print '   =>', url


def copy_file(url):
    dest_path = DESTINATION + url
    dirs = os.path.dirname(dest_path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    path = path_to(url)
    shutil.copy2(path, dest_path)
    print '   =>', url


def is_html(name):
    if name.endswith('.html') or name.endswith('.htm'):
        return True


@step
def render_htmls(f):
    for file in f:
        if is_html(file['name']):
            print '\n#', file['url']
            context = compile_context()
            rendered = render_url(file['url'], context)
            write_file(file['url'], rendered)


def compile_context(**extra):
    context = {
            'dev': False,
            'compile': True,
        }
    context.update(extra)
    return context

def update_url(url):
    rendered = render_url(url)
    write_file(url, rendered)


@step
def copy_static(f):
    css_dir = os.path.join(SOURCE, 'css')
    js_dir = os.path.join(SOURCE, 'js')
    for file in f:
        name = file['path']
        if is_sub(css_dir, name) or is_sub(js_dir, name):
            copy_file(file['url'])


def main():
    print "Chiseling..."
    ensure_destination()
    print "\tReading files...",
    files = sorted(get_tree(SOURCE), cmp=compare_entries)
    print "Done."
    print "\tRunning steps..."
    for step in _STEPS:
        print "\t\t",
        step(files)
    print "\tDone."
    print "Done."


if __name__ == "__main__":
    sys.exit(main())
