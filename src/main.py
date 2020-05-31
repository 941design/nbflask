#!/usr/bin/env python3

import notebook

from flask import Flask
from flask import request
from flask import make_response
from flask_caching import Cache


app = Flask(__name__)
cache = Cache(config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300  # seconds
})
cache.init_app(app)


NOTEBOOK_PARAMETERS = {  # as defined in first cell of notebook
    'polynome': lambda s: list(map(float, s.split(',')))
}


@app.route('/pdf', methods=['GET'])
def pdf():
    kwargs = sanitize_parameters(request.args)
    response = make_response(create_pdf(**kwargs))
    response.headers['Content-Type'] = 'application/pdf'
    return response


def sanitize_parameters(params):
    # uncomment for ignoring case
    # params = { k.lower() : v for k,v in params.items() }
    return { k: NOTEBOOK_PARAMETERS[k](v)
             for k,v in params.items() if k in NOTEBOOK_PARAMETERS }


@cache.memoize()
def create_pdf(**kwargs):
    return notebook.create_pdf(**kwargs)


def main():
    app.run()


if __name__ == '__main__':
    main()
