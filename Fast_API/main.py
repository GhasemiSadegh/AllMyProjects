from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return 'the code is working.'
