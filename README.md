# Study Tracker

Веб-трекер дедлайнов по учёбе. Учебный проект, который я делаю для себя, чтобы освоить backend-разработку.

## Стек

- Python
- FastAPI

## Как запустить

Команды для Windows (PowerShell).

1. Склонируй репозиторий и перейди в папку проекта:
```
   git clone https://github.com/averryn/study-tracker.git
   cd study-tracker
```
2. Создай и активируй виртуальное окружение:
```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
```
   Если PowerShell запрещает запуск скриптов, один раз выполни `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` и повтори активацию.
3. Установи зависимости:
```
   pip install "fastapi[standard]"
```
4. Запусти сервер:
```
   fastapi dev main.py
```
5. Открой в браузере:
   - `http://127.0.0.1:8000` — главная страница API
   - `http://127.0.0.1:8000/docs` — автоматическая документация

## Статус

В разработке. Сейчас готов минимальный сервер с одним маршрутом.

В планах: база данных SQLite, API для задач (создать, показать, отметить, удалить), веб-интерфейс, запуск в Docker.