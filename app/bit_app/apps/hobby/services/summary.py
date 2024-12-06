from bit_app.apps.common.utils import generate_embedded_data, prompt_openai
from bit_app.apps.hobby.gpt_schemas import HOBBY_SUMMARY
from bit_app.apps.hobby.models import Hobby, HobbyEmbedding
from bit_app.apps.hobby.serializers import HobbySerializer


class HobbySummaryService:
    def __init__(self, hobby: Hobby):
        self.hobby = hobby

    def generate_hobby_summary(self):
        hobby_data = HobbySerializer(self.hobby).data
        context = HOBBY_SUMMARY.prompt_preparing_function(hobby_data)
        gpt_response = prompt_openai(
            system_prompt=HOBBY_SUMMARY.system_prompt,
            user_prompt=HOBBY_SUMMARY.user_prompt,
            schema=HOBBY_SUMMARY.schema,
            context=context,
        )

        self.hobby.summary = gpt_response.get("summary", None)
        self.hobby.save(update_fields=["summary"])

    def generate_embedding(self):
        embedded_value = generate_embedded_data(self.hobby.summary)

        HobbyEmbedding.objects.create(hobby=self.hobby, embedding=embedded_value)
