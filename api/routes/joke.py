from fastapi import APIRouter

router = APIRouter()

@router.get('/jokes/{value}')
async def get_joke(value: str):
    pass

@router.post('/jokes/')
async def save_joke():
    pass

@router.put('/jokes/')
async def update_joke():
    pass

@router.delete('/jokes/')
async def delete_joke():
    pass