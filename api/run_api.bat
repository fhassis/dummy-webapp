@ECHO OFF

@REM poetry config virtualenvs.in-project true

@REM poetry install

poetry run uvicorn app:app --port 8001
