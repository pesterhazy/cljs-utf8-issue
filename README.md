# Repro steps

```shell
$ curl -fsSLo cljs.jar https://github.com/clojure/clojurescript/releases/download/r1.9.946/cljs.jar

$ brew install moreutils # or apt-get install moreutils

$ bin/build

$ isutf8 out/main.js
out/main.js: line 272, char 1, byte offset 217: invalid UTF-8 code
```
