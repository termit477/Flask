import uvicorn

if __name__ == '__main__':
    uvicorn.run('task_4:app', port=80, reload=True)