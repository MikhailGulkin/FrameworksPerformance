from typing import Any

from fastapi import APIRouter
import Servers.test_data

router = APIRouter()


@router.get('/1_k_json')
async def one_k_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_1K


@router.get('/10_k_json')
async def ten_k_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_10K


@router.get('/100_k_json')
async def hundred_k_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_100K


@router.get('/1_kk_json')
async def one_kk_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_1M


@router.get('/5_kk_json')
async def five_kk_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_5M
