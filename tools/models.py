from django.conf import settings
from django.db import models


class SavedTool(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="saved_tools",
    )

    tool_slug = models.CharField(
        max_length=120,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "user",
                    "tool_slug",
                ],
                name="unique_saved_tool_per_user",
            )
        ]

    def __str__(self):

        return (
            f"{self.user.username} - "
            f"{self.tool_slug}"
        )