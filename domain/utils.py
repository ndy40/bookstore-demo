from typing import Any

from fastapi import Response
from fastapi import status
from returns.maybe import Maybe
from returns.result import Result, Success, Failure


def handle_response(response: Result[Any, Any]):
    match response:
        case Success(item):
            return item
        case Failure(msg):
            match msg:
                case Maybe.empty:
                    return Response(
                        status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
                    )
                case _:
                    return msg
