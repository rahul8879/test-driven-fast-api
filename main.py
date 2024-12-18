from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def test():
    return {'hello':'How are you'}

