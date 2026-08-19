from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import RecentViewedTool
from .views import TOOLS


# =========================================================
# RECENTLY VIEWED TOOLS PAGE
# =========================================================

@login_required(login_url="login")
def recent_tools_view(request):

    records = RecentViewedTool.objects.filter(
        user=request.user,
    )

    recent_tools = []

    for record in records:

        tool = TOOLS.get(
            record.tool_slug
        )

        if tool:

            recent_tools.append(
                {
                    "slug": record.tool_slug,
                    "tool": tool,
                    "viewed_at": record.viewed_at,
                }
            )

    return render(
        request,
        "recent_tools.html",
        {
            "recent_tools": recent_tools,
            "recent_count": len(recent_tools),
        },
    )


# =========================================================
# CLEAR RECENT HISTORY
# =========================================================

@login_required(login_url="login")
@require_POST
def clear_recent_tools(request):

    RecentViewedTool.objects.filter(
        user=request.user,
    ).delete()

    return redirect(
        "recent_tools"
    )