from bit_app.apps.user_profile.models import UserProfile, ProfileEmbedding, Quiz, Question
from bit_app.apps.common.utils import generate_embedded_data
from bit_app.apps.common.utils import prompt_openai
from bit_app.apps.user_profile.gpt_schemas import USER_CHARACTER, USER_SUMMARY


class UserSummaryService:
    def __init__(self, profile: UserProfile):
        self.profile = profile
        self.quiz = Quiz.objects.filter(profile=profile).prefetch_related('questions').first()

    def generate_person_summary(self):
        quiz_data = [
            {question.name: question.response}
            for question in self.quiz.questions.all()
        ]
        context = USER_SUMMARY.prompt_preparing_function(quiz_data)
        gpt_response = prompt_openai(
            system_prompt=USER_SUMMARY.system_prompt,
            user_prompt=USER_SUMMARY.user_prompt,
            schema=USER_SUMMARY.schema,
            context=context
        )

        self.profile.summary = gpt_response.get("summary", None)
        self.profile.save(update_fields=['summary'])

    def generate_person_character(self):
        summary = self.profile.summary
        gpt_response = prompt_openai(
            system_prompt=USER_CHARACTER.system_prompt,
            user_prompt=USER_CHARACTER.user_prompt,
            schema=USER_CHARACTER.schema,
            context=summary
        )

        result = USER_CHARACTER.prompt_changing_function(gpt_response)
        self.profile.character = result
        self.profile.save(update_fields=['character'])

        return {"character": result}

    def generate_embedding(self):
        embedded_value = generate_embedded_data(self.profile.summary)

        ProfileEmbedding.objects.create(
            profile=self.profile,
            embedding=embedded_value
        )
