from fastapi import FastAPI
from databases import engine, Base

import uvicorn

app = FastAPI()

# Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {'message': 'Hello, World!'}


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
    