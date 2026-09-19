from fastapi import FastAPI


app = FastAPI()


@app.get("/say_hello")
def say_hello():
    return {"message":"Hey"}



