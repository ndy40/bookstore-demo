import uvicorn
from dotenv import load_dotenv

from infrastructure.http.rest import app

load_dotenv()


def main():
    return app


if __name__ == '__main__':
    uvicorn.run('app:main', port=5000, log_level='info', reload=True)
