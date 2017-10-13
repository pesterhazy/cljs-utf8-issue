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

isutf8 1.1 considers this file invalid:

```
$ isutf8 --help
Usage: /usr/local/Cellar/moreutils/0.57/libexec/bin/isutf8 [-hq] [--help] [--quiet] [file ...]
Check whether input files are valid UTF-8.
This is version 1.1.

$ isutf8 out/main.js
out/main.js: line 272, char 1, byte offset 217: invalid UTF-8 code
```

You can easily compile moreutils 0.59 from git.

However, isutf8 1.2 from moreutils 0.61 think it's ok:

```
$ isutf8 out/main.js
```

From the moreutils 0.60 changelog:

> moreutils 0.60 released with these changes
> 
> New implementation of isutf8 by Julien Palard.
> Noncharacters (ending with 0xFFFF and 0xFFFE) were considered invalid when encoded in utf8, according to the unicode standard they are valid: "However, they are not illegal in interchange, nor does their presence cause Unicode text to be ill-formed."
> \xf4\xbf\xbf\xbf was considered valid UTF8, which is not: after 0xF4 the following byte should be between 80 and 8F.

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
