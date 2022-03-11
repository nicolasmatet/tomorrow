from botocore.exceptions import ClientError
from fastapi import APIRouter

from ..models import Question

router = APIRouter()


@router.get("/")
async def get_question(n):
    return Question.read({'id': int(n)})
