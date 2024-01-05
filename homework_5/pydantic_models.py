from pydantic import BaseModel


class Music(BaseModel):
    id: int
    name: str
    author: str
    description: str | None = None
    genre: str


