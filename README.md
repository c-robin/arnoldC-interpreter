#ArnoldC interpreter

This is an interpreter of the [ArnoldC language](https://github.com/lhartikk/ArnoldC) written in Python, using [ANTLR](http://www.antlr.org/) v4.


##Quick Start

```
antlr -visitor -no-listener -Dlanguage=Python2 ArnoldC.g4
python main.py
```
