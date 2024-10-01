from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "Estou viva, mulher!"}

@app.get("/data")
def randon_return():
    return {"message": "Diamante Negro nem é chocolate!"}

@app.get("/kill")
def erro_app():
    sys.exit(1)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
