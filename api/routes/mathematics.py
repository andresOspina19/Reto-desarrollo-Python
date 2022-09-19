from fastapi import APIRouter, Query, HTTPException
from math import lcm
from api.schemas.mathematics import lcmEntity, numberPlusOneEntity

router = APIRouter()

@router.get('/math/lcm/')
def get_least_common_multiple(numbers: list[int] = Query() ):
    return lcmEntity(lcm(*numbers))

@router.get('/math/numberPlusOne/')
def get_number_plus_one(number: float):
    return numberPlusOneEntity(number + 1)