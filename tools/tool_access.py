from django.shortcuts import redirect, render
from django.utils import timezone

from .models import RecentViewedTool
from .views import TOOLS


# =========================================================
# RECORD RECENTLY VIEWED TOOL
# =========================================================

def _record_recent_tool(user, slug):

    if not user.is_authenticated:
        return

    recent_tool, created = (
        RecentViewedTool.objects.get_or_create(
            user=user,
            tool_slug=slug,
        )
    )

    if not created:

        recent_tool.viewed_at = timezone.now()

        recent_tool.save(
            update_fields=[
                "viewed_at",
            ]
        )

    # Keep only latest 20 tools
    old_ids = list(
        RecentViewedTool.objects.filter(
            user=user,
        )
        .order_by("-viewed_at")
        .values_list(
            "id",
            flat=True,
        )[20:]
    )

    if old_ids:

        RecentViewedTool.objects.filter(
            id__in=old_ids,
        ).delete()


# =========================================================
# PROTECTED TOOL ACCESS
# User clicks tool -> login first -> selected tool
# =========================================================

def protected_tool_access(request, slug):

    tool = TOOLS.get(slug)

    if not tool:
        return redirect("home")

    if not request.user.is_authenticated:

        request.session[
            "pending_tool_slug"
        ] = slug

        request.session[
            "pending_tool_action"
        ] = "detail"

        return redirect("login")

    _record_recent_tool(
        request.user,
        slug,
    )

    return redirect(
        "tool_detail",
        slug=slug,
    )


# =========================================================
# PROTECTED OFFICIAL WEBSITE ACCESS
# =========================================================

def protected_official_access(request, slug):

    tool = TOOLS.get(slug)

    if not tool:
        return redirect("home")

    if not request.user.is_authenticated:

        request.session[
            "pending_tool_slug"
        ] = slug

        request.session[
            "pending_tool_action"
        ] = "official"

        return redirect("login")

    _record_recent_tool(
        request.user,
        slug,
    )

    return redirect(
        tool["official_url"]
    )


# =========================================================
# AFTER LOGIN ROUTER
# =========================================================

def welcome_router(request):

    if not request.user.is_authenticated:

        return redirect(
            "login"
        )

    pending_slug = request.session.pop(
        "pending_tool_slug",
        None,
    )

    pending_action = request.session.pop(
        "pending_tool_action",
        None,
    )

    if (
        pending_slug
        and pending_slug in TOOLS
    ):

        _record_recent_tool(
            request.user,
            pending_slug,
        )

        if pending_action == "official":

            return redirect(
                "protected_official_access",
                slug=pending_slug,
            )

        return redirect(
            "tool_detail",
            slug=pending_slug,
        )

    return render(
        request,
        "welcome.html",
    )