from django.shortcuts import redirect, render

from .views import TOOLS


# =========================================================
# PROTECTED TOOL ACCESS
# User clicks a tool -> login first -> selected tool page
# =========================================================

def protected_tool_access(request, slug):

    tool = TOOLS.get(slug)

    if not tool:
        return redirect("home")

    # User is not logged in
    if not request.user.is_authenticated:

        request.session["pending_tool_slug"] = slug
        request.session["pending_tool_action"] = "detail"

        return redirect("login")

    # User already logged in
    return redirect(
        "tool_detail",
        slug=slug,
    )


# =========================================================
# PROTECTED OFFICIAL WEBSITE ACCESS
# Visit Official Website -> login first -> official website
# =========================================================

def protected_official_access(request, slug):

    tool = TOOLS.get(slug)

    if not tool:
        return redirect("home")

    # User is not logged in
    if not request.user.is_authenticated:

        request.session["pending_tool_slug"] = slug
        request.session["pending_tool_action"] = "official"

        return redirect("login")

    # User is logged in
    return redirect(
        tool["official_url"]
    )


# =========================================================
# AFTER LOGIN ROUTER
#
# Works with:
# - Normal username/password login
# - Google login
#
# Existing login system redirects users to /welcome/.
# This view checks whether the user originally clicked a tool.
# =========================================================

def welcome_router(request):

    if not request.user.is_authenticated:
        return redirect("login")

    pending_slug = request.session.pop(
        "pending_tool_slug",
        None,
    )

    pending_action = request.session.pop(
        "pending_tool_action",
        None,
    )

    # User originally clicked a tool
    if pending_slug and pending_slug in TOOLS:

        # User originally clicked Visit Official Website
        if pending_action == "official":

            return redirect(
                "protected_official_access",
                slug=pending_slug,
            )

        # User originally clicked a tool card
        return redirect(
            "tool_detail",
            slug=pending_slug,
        )

    # Normal login without clicking a tool first
    return render(
        request,
        "welcome.html",
    )