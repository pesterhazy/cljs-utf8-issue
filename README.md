# Summary

Repo to repro

Code emitted by Google Closue (via ClojureScript) is considered invalid utf8 by Google Chrome (when it loads the file as a Chrome Extension Chrome checks content scripts for utf-8 conformance):

The [isutf8](https://joeyh.name/code/moreutils/) utility agrees with Chrome.

# Repro steps

```shell
$ curl -fsSLo cljs.jar https://github.com/clojure/clojurescript/releases/download/r1.9.946/cljs.jar

$ brew install moreutils # or apt-get install moreutils

$ bin/build
```

isutf8 considers this file invalid:

```

$ isutf8 out/main.js
out/main.js: line 272, char 1, byte offset 217: invalid UTF-8 code
```

iconv thinks it's ok

```
$ iconv -f UTF-8 out/main.js > /dev/null; echo $?
0
```

and so does python

```
$ bin/check-utf8.py
utf-8 ok
```
