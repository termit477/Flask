# Необходимо создать API для управления музыкальными композициями. 
# Каждая музыкальная композиция должна содержать id, название, автора, описание, жанр. 

# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех музыкальных композиций.
# — GET /tasks/{id} — возвращает музыкальную композицию с указанным идентификатором.
# — POST /tasks — добавляет новую музыкальную композицию.
# — PUT /tasks/{id} — обновляет музыкальную композицию с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет музыкальную композицию с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. 
# Для этого использовать библиотеку Pydantic.

from fastapi import FastAPI
from pydantic_models import Music


app = FastAPI()
musics: list[Music] = []


@app.get('/')
async def index():
    return musics


@app.get('/musics/{music_id}')
async def get_music(music_id: int):
    filtered_musics = [music for music in musics if music.id == music_id]
    music = filtered_musics[0]

    return music


@app.post('/musics/')
async def create_music(music: Music):
    musics.append(music)
    return musics


@app.put('/musics/{music_id}')
async def update_music(music_id: int, new_music: Music):
    filtered_musics = [music for music in musics if music.id == music_id]
    if not filtered_musics:
        return {'updated': False}
    
    music = filtered_musics[0]

    music.id = new_music.id
    music.name = new_music.name
    music.author = new_music.author
    music.description = new_music.description
    music.genre = new_music.genre

    return {'updated': True, 'music': new_music}


@app.delete('/musics/{music_id}')
async def delete_music(music_id: int):
    filtered_musics = [music for music in musics if music.id == music_id]
    if not filtered_musics:
        return {'updated': False}
    
    music = filtered_musics[0]
    
    musics.remove(music)

    return {'deleted': True, 'music': music}