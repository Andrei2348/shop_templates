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
import json


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

task_list = []

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    


@app.get("/tasks")
async def get_all_tasks():
    print(task_list)
    logger.info('Отработал GET запрос на возврат списка всех задач.')
    return task_list


@app.get("/tasks/{task_id}")
async def get_selected_task(task_id: int):
    for elem in task_list:
        if elem.id == task_id:
            logger.info(f'Отработал GET запрос на возврат задачи с идентификатором: {task_id}')
            return elem 
    logger.info('GET запрос на возврат задачи с идентификатором отработал с ошибкой')
    return {"Alarm_message":"В списке задач нет такой задачи"}


@app.post("/tasks/")
async def create_task(task: Task):
    task_list.append(task)
    logger.info('Отработал POST запрос. Добавлена новая задача')
    return task


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task:  Task):
    for index, elem in enumerate(task_list):
        if elem.id == task_id:
            task_list[index] = task
            logger.info(f'Отработал PUT запрос. Обновлена задача с идентификатором: {task_id}.')
            return {"task_id": task_id, "task": task}
    logger.info('PUT запрос отработал с ошибкой')
    return {"Alarm_message":"В списке задач нет такой задачи"}
   
    
@app.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
    for index, elem in enumerate(task_list):
        if elem.id == task_id:
            task_list.pop(index)
            logger.info(f'Отработал DELETE запрос для идентификатора: {task_id}.')
            return {"task_id": task_id}
    logger.info('DELETE запрос отработал с ошибкой')
    return {"Alarm_message":"В списке задач нет такой задачи"}
