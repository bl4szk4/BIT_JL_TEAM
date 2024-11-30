from django.db.models import Case, When
from pgvector.django import CosineDistance

from bit_app.apps.hobby.consts import SEMANTIC_SEARCH_THRESHOLD
from bit_app.apps.hobby.models import Hobby, HobbyEmbedding
from bit_app.apps.user_profile.models import UserProfile


class HobbyMatchingService:
    def __init__(self, profile: UserProfile):
        self.profile = profile

    def get_best_matching_hobbies(self):
        # Pobierz profile embeddings
        print(self.profile.id)
        profile_embedding_instance = self.profile.embeddings.first()
        if not profile_embedding_instance:
            return Hobby.objects.none()

        profile_embedding = profile_embedding_instance.embedding

        hobby_embeddings = HobbyEmbedding.objects.select_related("hobby").all()

        best_hobbies = hobby_embeddings.annotate(
            hobby_distance=CosineDistance("embedding", profile_embedding),
        ).filter(
            hobby_distance__lte=SEMANTIC_SEARCH_THRESHOLD,
        )

        if not best_hobbies.exists():
            return Hobby.objects.none()

        best_hobbies = best_hobbies.order_by("hobby_distance")

        best_results_ids = best_hobbies.values_list("hobby__id", flat=True)
        preserved_order = Case(
            *[
                When(id=result_id, then=position)
                for position, result_id in enumerate(best_results_ids)
            ]
        )

        return (
            Hobby.objects.filter(id__in=best_results_ids)
            .annotate(order=preserved_order)
            .order_by("order")
        )
