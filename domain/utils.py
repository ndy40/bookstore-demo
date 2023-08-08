from typing import Any

from fastapi import HTTPException
from fastapi import status
from returns.result import Result, Success, Failure
from returns.maybe import Nothing


def handle_response(response: Result[Any, Any]):
    match response:
        case Success(item):
            return item
        case Failure(msg):
            print(msg)
            match msg:
                case Nothing(_):
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
                case _:
                    return msg

