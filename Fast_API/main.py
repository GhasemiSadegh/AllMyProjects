from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return 'zero.'


@app.get('/greeting')
def hello():
    return 'Hello Dear Customer, we are not available now.'


@app.get('/log_in')
def hello():
    return 'log in page'


@app.get('/main')
def hello():
    return 'home page.'


# @app.get('/hello/{name}')
# def hello_name(name):
#     return f'hello {name}'
#
