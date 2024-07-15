from fastapi import FastAPI

app = FastAPI()


@app.get('/index')
def hello1():
    return {
        'message': 'hello1 is working.'
    }

