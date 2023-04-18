from typing import Any

from fastapi import APIRouter
from Servers.Python.utils.path import JsonResponse
import Servers.test_data

router = APIRouter()


@router.get(JsonResponse.one_k_json)
async def one_k_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_1K


@router.get(JsonResponse.ten_k_json)
async def ten_k_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_10K


@router.get(JsonResponse.hundred_k_json)
async def hundred_k_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_100K


@router.get(JsonResponse.one_kk_json)
async def one_kk_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_1M


@router.get(JsonResponse.five_kk_json)
async def five_kk_json() -> list[dict[str, Any]]:
    return Servers.test_data.JSON_5M
