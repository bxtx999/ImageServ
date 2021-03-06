from fastapi import APIRouter, HTTPException

from serv.models.images import Images
from serv.models.views import Image_Info_Pydantic

router = APIRouter()


@router.get("/{image_hash}", response_model=Image_Info_Pydantic)
async def get_image(image_hash: str):
    try:
        img = await Image_Info_Pydantic.from_queryset_single(Images.get(hash=image_hash))
    except Exception as e:
        raise HTTPException(status_code=404, detail="image not found.")
    return img
