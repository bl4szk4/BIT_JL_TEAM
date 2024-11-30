from django.db import models
from pgvector.django import HnswIndex, VectorField

from bit_app.apps.hobby.models.hobby import Hobby


class HobbyEmbedding(models.Model):
    hobby = models.ForeignKey(
        Hobby,
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
                name="hobby_embedding",
                fields=("embedding",),
                m=16,
                ef_construction=64,
                opclasses=("vector_cosine_ops",),
            ),
        )
