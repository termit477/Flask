# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с
# задачами.


from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import create_engine, select, insert, update, delete
import databases

from pydantic_models import TaskIn2, TaskOut2
from sqlalchemy_models import Base, Task2


DATABASE_URL = 'sqlite:///task_3.sqlite'

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


@app.get('/done/', response_model=list[TaskOut2])
async def get_done():
    tasks = select(Task2).where(Task2.status == True)

    return await database.fetch_all(tasks)


@app.get('/notdone/', response_model=list[TaskOut2])
async def get_not_done():
    tasks = select(Task2).where(Task2.status == False)

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


@app.post('/tasks/{task_id}/done/', response_model=TaskOut2)
async def done_task(task_id: int):
    task_done = update(Task2).where(Task2.id == task_id).values(status=True)

    await database.execute(task_done)

    return await database.fetch_one(select(Task2).where(Task2.id == task_id))


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
