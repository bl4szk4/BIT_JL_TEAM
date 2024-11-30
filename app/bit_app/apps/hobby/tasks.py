from celery import shared_task
from bit_app.apps.hobby.services import HobbySummaryService
from bit_app.apps.hobby.models import Hobby


@shared_task(bind=True)
def async_generate_hobby_summary(self, hobby_id: int) -> None:
    hobby = Hobby.objects.get(id=hobby_id)
    HobbySummaryService(hobby).generate_hobby_summary()
