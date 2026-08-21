from django.conf import settings
from django.db import models


# =========================================================
# SAVED TOOLS
# =========================================================

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


# =========================================================
# RECENTLY VIEWED TOOLS
# =========================================================

class RecentViewedTool(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recent_viewed_tools",
    )

    tool_slug = models.CharField(
        max_length=120,
    )

    viewed_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "-viewed_at",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "user",
                    "tool_slug",
                ],
                name="unique_recent_tool_per_user",
            )
        ]

    def __str__(self):

        return (
            f"{self.user.username} - "
            f"{self.tool_slug}"
        )


# =========================================================
# WEBSITE VISITOR / ANALYTICS LOG
# =========================================================

class VisitorLog(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="visitor_logs",
    )

    session_key = models.CharField(
        max_length=100,
        blank=True,
        db_index=True,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    path = models.CharField(
        max_length=500,
        db_index=True,
    )

    request_method = models.CharField(
        max_length=10,
        default="GET",
    )

    response_status = models.PositiveIntegerField(
        default=200,
    )

    referrer = models.TextField(
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    device_type = models.CharField(
        max_length=40,
        blank=True,
    )

    browser = models.CharField(
        max_length=60,
        blank=True,
    )

    operating_system = models.CharField(
        max_length=60,
        blank=True,
    )

    is_authenticated_visit = models.BooleanField(
        default=False,
    )

    is_bot = models.BooleanField(
        default=False,
    )

    visited_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    class Meta:

        ordering = [
            "-visited_at",
        ]

        indexes = [
            models.Index(
                fields=[
                    "visited_at",
                    "path",
                ],
                name="visit_time_path_idx",
            ),

            models.Index(
                fields=[
                    "session_key",
                    "visited_at",
                ],
                name="visit_session_idx",
            ),
        ]

    def __str__(self):

        if self.user:

            visitor_name = (
                self.user.username
            )

        else:

            visitor_name = "Guest"

        return (
            f"{visitor_name} - "
            f"{self.path} - "
            f"{self.visited_at}"
        )


# =========================================================
# WEBSITE THEME SETTINGS
# =========================================================

class SiteTheme(models.Model):

    THEME_CHOICES = [

        (
            "midnight",
            "Midnight Purple",
        ),

        (
            "ocean",
            "Ocean Blue",
        ),

        (
            "emerald",
            "Emerald Green",
        ),

        (
            "sunset",
            "Sunset Orange",
        ),

        (
            "rose",
            "Rose Pink",
        ),

        (
            "light",
            "Clean Light",
        ),

        (
            "custom",
            "Custom Theme",
        ),

    ]

    site_name = models.CharField(
        max_length=100,
        default="Veylora AI",
    )

    theme_preset = models.CharField(
        max_length=30,
        choices=THEME_CHOICES,
        default="midnight",
    )

    primary_color = models.CharField(
        max_length=20,
        default="#7568ff",
    )

    secondary_color = models.CharField(
        max_length=20,
        default="#00d4ff",
    )

    accent_color = models.CharField(
        max_length=20,
        default="#d946ef",
    )

    background_color = models.CharField(
        max_length=20,
        default="#0b0f19",
    )

    card_color = models.CharField(
        max_length=20,
        default="#121827",
    )

    text_color = models.CharField(
        max_length=20,
        default="#ffffff",
    )

    muted_text_color = models.CharField(
        max_length=20,
        default="#9da6b8",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        verbose_name = (
            "Site Theme"
        )

        verbose_name_plural = (
            "Site Theme"
        )

    def __str__(self):

        return (
            f"{self.site_name} - "
            f"{self.get_theme_preset_display()}"
        )

    @classmethod
    def get_active_theme(cls):

        theme, created = (
            cls.objects.get_or_create(
                pk=1,
            )
        )

        return theme