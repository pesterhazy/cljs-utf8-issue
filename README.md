# Summary

Repo to repro

Code emitted by Google Closue (via ClojureScript) is considered invalid utf8 by Google Chrome (when it loads the file as a Chrome Extension Chrome checks content scripts for utf-8 conformance):

An older version of the [isutf8](https://joeyh.name/code/moreutils/) utility, version 0.59, agrees with Chrome.

The changelog for moreutils 0.60 mentions the UTF-8 problem (non-problem?): https://joeyh.name/code/moreutils/

> Noncharacters (ending with 0xFFFF and 0xFFFE) were considered invalid when encoded in utf8, according to the unicode standard they are valid: "However, they are not illegal in interchange, nor does their presence cause Unicode text to be ill-formed."

# Repro steps

```
bin/build-js
```

Output in [output.js](out/output.js).

# Output

Output on macOS 10.12

```
$ bin/build-js
+ curl -fsSLo compiler.zip http://dl.google.com/closure-compiler/compiler-20170910.zip
+ curl -fsSLo library.zip https://github.com/google/closure-library/archive/v20170910.zip
+ rm -rf closure-library-20170910 compiler
+ mkdir compiler
+ unzip -q compiler.zip -d compiler
+ unzip -q library.zip
+ java -jar compiler/closure-compiler-v20170910.jar --js 'closure-library-20170910/closure/goog/**.js' --js '*_test.js' --js js-src --closure_entry_point my.hello --manage_closure_dependencies --only_closure_dependencies --js_output_file out/output.js --charset utf-8
+ rm -rf moreutils
+ git clone git://git.joeyh.name/moreutils
Cloning into 'moreutils'...
remote: Counting objects: 1501, done.
remote: Compressing objects: 100% (527/527), done.
remote: Total 1501 (delta 950), reused 1491 (delta 944)
Receiving objects: 100% (1501/1501), 334.48 KiB | 321.00 KiB/s, done.
Resolving deltas: 100% (950/950), done.
+ pushd moreutils
~/prg/cljs-utf8-issue/moreutils ~/prg/cljs-utf8-issue
+ git checkout 0.59
Note: checking out '0.59'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at f891e8d... releasing package moreutils version 0.59
+ make isutf8
cc -O2 -g -Wall    isutf8.c   -o isutf8
+ popd
~/prg/cljs-utf8-issue
+ moreutils/isutf8 out/output.js
out/output.js: line 287, char 1, byte offset 217: invalid UTF-8 code
```
