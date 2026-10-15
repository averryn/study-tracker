from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Трекер дедлайнов работает"}


@app.get("/hello")
def hello():
    return {"message": "Эксперимент прошел успешно!"}
    