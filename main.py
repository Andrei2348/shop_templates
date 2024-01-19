'''Задание

Необходимо создать API для управления списком задач. 
Каждая задача должна содержать заголовок и описание. 
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.'''

from fastapi import FastAPI
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Task(BaseModel):
    title: str
    description: str


@app.get("/tasks")
async def get_all_tasks():
    logger.info('Отработал GET запрос на возврат списка всех задач.')
    return {"message": "Hello World"}


@app.get("/tasks/{task_id}")
async def get_selected_task(task_id: int):
    logger.info(f'Отработал GET запрос на возврат задачи с идентификатором: {task_id}')
    return {"task_id": task_id}


@app.post("/tasks/")
async def create_task(task: Task):
    logger.info('Отработал POST запрос. Добавлена новая задача')
    return task


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task:  Task):
    logger.info(f'Отработал PUT запрос. Обновлена задача с идентификатором: {task_id}.')
    return {"task_id": task_id, "task": task}


@app.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
    logger.info(f'Отработал DELETE запрос для идентификатора: {task_id}.')
    return {"task_id": task_id}
