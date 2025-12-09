from fastapi import FastAPI

app = FastAPI()

@app.get("/test/{endpoint}", status_code=201)
def test_endpoint(endpoint: str):
    return endpoint