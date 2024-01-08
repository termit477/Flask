from pydantic import BaseModel, Field


class Status(BaseModel):
    status: bool = False


class TaskIn2(Status):
    name: str
    description: str | None = None


class TaskOut2(TaskIn2):
    id: int


class TaskIn2(BaseModel):
    title: str = Field()
    description: str | None = Field(default=None)
    done: bool = Field(default=False)


class TaskOut2(TaskIn2):
    id: int

    