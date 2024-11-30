from bit_app.apps.user_profile.models import Question, Quiz, UserProfile


class QuizService:
    def __init__(self, profile: UserProfile):
        self.profile = profile

    def create_quiz(self, quiz_data: dict):
        questions_data = quiz_data.pop('questions')
        quiz = Quiz.objects.create(profile=self.profile, **quiz_data)
        questions = [Question(quiz=quiz, **question_data) for question_data in questions_data]
        Question.objects.bulk_create(questions)
        return quiz

