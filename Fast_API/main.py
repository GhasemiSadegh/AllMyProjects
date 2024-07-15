from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return 'Hello World'


@app.get('/hello/{name}')
def hello_name(name):
    return f'hello {name}'

