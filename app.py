import uvicorn

from infrastructure.http.rest import app


def main():
    return app


if __name__ == '__main__':
    uvicorn.run('app:main', port=5000, log_level='info', reload=True, host='0.0.0.0', factory=True)
