from django.db import models
from pgvector.django import HnswIndex, VectorField

from bit_app.apps.user_profile.models.user_profile import UserProfile


class ProfileEmbedding(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="embeddings",
    )
    embedding = VectorField(
        dimensions=1536,
        null=True,
        blank=True,
        help_text="Embedding",
    )

    class Meta:
        indexes = (
            HnswIndex(
                name="profile_embedding",
                fields=("embedding",),
                m=16,
                ef_construction=64,
                opclasses=("vector_cosine_ops",),
            ),
        )
