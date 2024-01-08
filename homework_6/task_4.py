# Напишите API для управления списком задач. Для этого создайте модель Task
# со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)

# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.



from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import create_engine, select, insert, update, delete
import databases

from pydantic_models import TaskIn2, TaskOut2
from sqlalchemy_models import Base, Task2


DATABASE_URL = 'sqlite:///task_4.sqlite'

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()

    yield

    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/tasks/', response_model=list[TaskOut2])
async def index():
    tasks = select(Task2)

    return await database.fetch_all(tasks)


@app.get('/tasks/{task_id}/', response_model=TaskOut2)
async def get_task(task_id: int):
    task = select(Task2).where(Task2.id == task_id)

    return await database.fetch_one(task)


@app.post('/tasks/', response_model=TaskIn2)
async def create_task(task: TaskIn2):
    new_task = insert(Task2).values(**task.model_dump())
    await database.execute(new_task)

    return task


@app.put('/tasks/{task_id}/', response_model=TaskOut2)
async def update_task(task_id: int, task: TaskIn2):
    task_update = update(Task2).where(Task2.id == task_id).values(**task.model_dump())

    await database.execute(task_update)

    return await database.fetch_one(select(Task2).where(Task2.id == task_id))


@app.delete('/tasks/{task_id}/')
async def delete_task(task_id: int):
    task_delete = delete(Task2).where(Task2.id == task_id)
    await database.execute(task_delete)

    return {'deleted': True, 'task': task_id}
