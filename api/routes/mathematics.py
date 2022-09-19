from fastapi import APIRouter, Query, HTTPException
from math import lcm
from schemas.mathematics import lcmEntity, numberPlusOneEntity

router = APIRouter()

@router.get('/math/lcm/', tags=["Mathematics Methods"])
def get_least_common_multiple(numbers: list[int] = Query() ):
    return lcmEntity(lcm(*numbers))

@router.get('/math/numberPlusOne/', tags=["Mathematics Methods"])
def get_number_plus_one(number: float):
    return numberPlusOneEntity(number + 1)