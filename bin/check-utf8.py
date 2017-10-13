#!/usr/bin/env python


def try_utf8(data):
    "Returns a Unicode object on success, or None on failure"
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return None


data = open("out/main.js").read()
udata = try_utf8(data)
if udata is None:
    print "not utf-8"
else:
    print "utf-8 ok"
