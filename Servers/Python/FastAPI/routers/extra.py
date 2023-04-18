from typing import Any

from fastapi import APIRouter
from Servers.Python.utils.path import ExtraTests

router = APIRouter()


@router.get(ExtraTests.hello_world)
async def hello_world() -> dict[str, str]:
    return {'Hello': 'World'}
