from django.db.models import Case, F, Sum, When
from pgvector.django import CosineDistance

from bit_app.apps.hobby.consts import SEMANTIC_SEARCH_THRESHOLD
from bit_app.apps.hobby.models import Hobby, HobbyEmbedding
from bit_app.apps.user_profile.models import UserProfile


class HobbyMatchingService:
    def __init__(self, profile: UserProfile):
        self.profile = profile

    def get_best_matching_hobbies(self):
        profile_embeddings = list(self.profile.embeddings.all().values_list("embedding", flat=True))
        if not profile_embeddings:
            return Hobby.objects.none()

        hobby_embeddings = HobbyEmbedding.objects.select_related("hobby").exclude(hobby__id__in=self.profile.rejected_hobbies).exclude(hobby__id__in=self.profile.accepted_hobbies)

        for embedding in profile_embeddings:
            hobby_embeddings = hobby_embeddings.annotate(
                hobby_distance=CosineDistance("embedding", embedding)
            ).filter(
                hobby_distance__lte=SEMANTIC_SEARCH_THRESHOLD,
            )

        if not hobby_embeddings.exists():
            return Hobby.objects.none()

        hobby_distances = (
            hobby_embeddings.values("hobby")
            .annotate(total_distance=Sum("hobby_distance"))
            .order_by("total_distance")
        )

        best_results_ids = [entry["hobby"] for entry in hobby_distances]
        preserved_order = Case(
            *[
                When(id=hobby_id, then=position)
                for position, hobby_id in enumerate(best_results_ids)
            ]
        )

        return (
            Hobby.objects.filter(id__in=best_results_ids)
            .annotate(order=preserved_order)
            .order_by("order")
        )
