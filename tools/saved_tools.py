from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .models import SavedTool
from .views import TOOLS


# =========================================================
# SAFE REDIRECT HELPER
# =========================================================

def _safe_next_url(request, default_url):

    next_url = request.POST.get("next", "").strip()

    if next_url and url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return next_url

    return default_url


# =========================================================
# SAVE / UNSAVE TOOL
# =========================================================

@login_required(login_url="login")
@require_POST
def toggle_saved_tool(request, slug):

    tool = TOOLS.get(slug)

    if not tool:
        return redirect("home")

    saved_tool = SavedTool.objects.filter(
        user=request.user,
        tool_slug=slug,
    ).first()

    # Already saved -> remove it
    if saved_tool:

        saved_tool.delete()

    # Not saved -> save it
    else:

        SavedTool.objects.create(
            user=request.user,
            tool_slug=slug,
        )

    default_url = reverse(
        "tool_detail",
        args=[slug],
    )

    return redirect(
        _safe_next_url(
            request,
            default_url,
        )
    )


# =========================================================
# SAVED TOOLS PAGE
# =========================================================

@login_required(login_url="login")
def saved_tools_view(request):

    saved_records = SavedTool.objects.filter(
        user=request.user,
    )

    saved_tools = []

    for record in saved_records:

        tool = TOOLS.get(
            record.tool_slug
        )

        if tool:

            saved_tools.append(
                {
                    "slug": record.tool_slug,
                    "tool": tool,
                    "saved_at": record.created_at,
                }
            )

    return render(
        request,
        "saved_tools.html",
        {
            "saved_tools": saved_tools,
            "saved_count": len(saved_tools),
        },
    )


# =========================================================
# CHECK WHETHER CURRENT TOOL IS SAVED
# Used later on tool detail page
# =========================================================

def is_tool_saved(user, slug):

    if not user.is_authenticated:
        return False

    return SavedTool.objects.filter(
        user=user,
        tool_slug=slug,
    ).exists()