from bit_app.apps.common.classes import PromptOpenAI
from bit_app.apps.common.utils import prompt_openai
from bit_app.apps.hobby.models import Hobby
from bit_app.apps.hobby.gpt_schemas import HOBBY_SUMMARY
from bit_app.apps.hobby.serializers import HobbySerializer

class HobbySummaryService:
    def __init__(self, hobby: Hobby):
        self.hobby = hobby

    def generate_hobby_summary(self):

        gpt_response = prompt_openai(
            system_prompt=HOBBY_SUMMARY.system_prompt,
            user_prompt=HOBBY_SUMMARY.user_prompt,
            schema=HOBBY_SUMMARY.schema,
        )