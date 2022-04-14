from fastapi import APIRouter
from ..dynamodb.fixtures import FixtureQuestions
from ..models import Question
import datetime
router = APIRouter()

NQUESTIONS = len(FixtureQuestions().values)
SEED = 59863
def get_day_in_year():
    return datetime.datetime.now().timetuple().tm_yday

def get_question_id(question_order:int):
    initial = get_day_in_year()
    return (initial + SEED ** question_order) % NQUESTIONS

@router.get("/")
async def get_question(n):
    question_id = get_question_id(int(n))
    return Question.read({'id': question_id})

