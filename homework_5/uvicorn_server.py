import uvicorn

if __name__ == '__main__':
    uvicorn.run('task:app', port=80, reload=True)