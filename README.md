# nbflask

Serves pdf from underlying jupyter notebook via http.

Create good looking, dynamic reports from jupyter notebooks.


## features

+ executes notebook with given request parameters
+ caches resulting pdf
+ execute notebook locally
+ develop notebook as usual


## requirements

+ pandoc
+ latex


## usage

+ `make install` for installing requirements
+ `make install-kernel` install custom jupyter kernel
+ `make to-pdf` to create a pdf from notebook
+ `make to-md` to convert notebook to markdown
+ `make from-md` to create notebook from markdown
+ `make notebook` to start notebook as jupyter notebook in browser
+ `make start` for running flask webservice on `http://localhost:5000`
+ [link](http://localhost:5000/pdf?polynome=1,2,3) for opening in browser
+ `curl http://localhost:5000/pdf?polynome=1,2,3 -o out.pdf` for download


## examples

see [examples/test.md](./examples/test.md)


## TODO

+ dockerize
+ nicer plots (resolution?, svg?)
+ error handling
+ health checks
+ extend example to use an sqliteDB
+ build package
+ consider pinning requirements
+ check vulnerabilities
+ create actual command line interface, using argparse or click
+ add license
+ create kernel via Makefile
