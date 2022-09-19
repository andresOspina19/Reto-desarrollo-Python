from fastapi import APIRouter, Query

router = APIRouter()

@router.get('/math/lcm/')
async def get_least_common_multiple(numbers: list[int]):
    pass

@router.get('/math/numberPlusOne/')
async def get_number_plus_one(number: int):
    pass