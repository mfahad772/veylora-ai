from datetime import timedelta

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import (
    RecentViewedTool,
    SavedTool,
    SiteTheme,
    VisitorLog,
)
from .views import TOOLS


User = get_user_model()


# =========================================================
# THEME PRESETS
# =========================================================

THEME_PRESETS = {

    "midnight": {
        "primary_color": "#7568ff",
        "secondary_color": "#00d4ff",
        "accent_color": "#d946ef",
        "background_color": "#070b14",
        "card_color": "#101725",
        "text_color": "#ffffff",
        "muted_text_color": "#8f9caf",
    },

    "ocean": {
        "primary_color": "#0ea5e9",
        "secondary_color": "#22d3ee",
        "accent_color": "#6366f1",
        "background_color": "#06111d",
        "card_color": "#0c1b2a",
        "text_color": "#ffffff",
        "muted_text_color": "#94a9bb",
    },

    "emerald": {
        "primary_color": "#10b981",
        "secondary_color": "#22c55e",
        "accent_color": "#06b6d4",
        "background_color": "#06140f",
        "card_color": "#0c2119",
        "text_color": "#ffffff",
        "muted_text_color": "#9ab9ac",
    },

    "sunset": {
        "primary_color": "#f97316",
        "secondary_color": "#f59e0b",
        "accent_color": "#ef4444",
        "background_color": "#160d08",
        "card_color": "#24150d",
        "text_color": "#ffffff",
        "muted_text_color": "#c2a89a",
    },

    "rose": {
        "primary_color": "#e11d48",
        "secondary_color": "#f43f5e",
        "accent_color": "#a855f7",
        "background_color": "#16090f",
        "card_color": "#25101a",
        "text_color": "#ffffff",
        "muted_text_color": "#c4a1ae",
    },

    "light": {
        "primary_color": "#4f46e5",
        "secondary_color": "#0284c7",
        "accent_color": "#9333ea",
        "background_color": "#f5f7fb",
        "card_color": "#ffffff",
        "text_color": "#111827",
        "muted_text_color": "#64748b",
    },
}


# =========================================================
# ADMIN DASHBOARD
# =========================================================

@staff_member_required(login_url="login")
def admin_dashboard(request):

    now = timezone.now()
    today = now.date()

    seven_days_ago = (
        today - timedelta(days=6)
    )

    active_tab = request.GET.get(
        "tab",
        "dashboard",
    )

    allowed_tabs = [
        "dashboard",
        "analytics",
        "visitors",
        "users",
        "tools",
        "theme",
    ]

    if active_tab not in allowed_tabs:
        active_tab = "dashboard"


    theme = SiteTheme.get_active_theme()


    # =====================================================
    # FORM ACTIONS
    # =====================================================

    if request.method == "POST":

        action = request.POST.get(
            "action",
            "",
        )


        # -------------------------------------------------
        # SAVE THEME
        # -------------------------------------------------

        if action == "save_theme":

            selected_theme = request.POST.get(
                "theme_preset",
                "midnight",
            )

            theme.theme_preset = selected_theme


            if selected_theme in THEME_PRESETS:

                preset = THEME_PRESETS[
                    selected_theme
                ]

                for field, value in preset.items():

                    setattr(
                        theme,
                        field,
                        value,
                    )


            elif selected_theme == "custom":

                fields = [
                    "primary_color",
                    "secondary_color",
                    "accent_color",
                    "background_color",
                    "card_color",
                    "text_color",
                    "muted_text_color",
                ]

                for field in fields:

                    value = request.POST.get(
                        field
                    )

                    if value:
                        setattr(
                            theme,
                            field,
                            value,
                        )


            theme.save()

            return redirect(
                "/control-panel/?tab=theme"
            )


        # -------------------------------------------------
        # CLEAR ANALYTICS
        # -------------------------------------------------

        if action == "clear_analytics":

            VisitorLog.objects.all().delete()

            return redirect(
                "/control-panel/?tab=analytics"
            )


    # =====================================================
    # ANALYTICS
    # =====================================================

    real_visits = VisitorLog.objects.filter(
        is_bot=False,
    )

    today_visits = real_visits.filter(
        visited_at__date=today,
    )


    total_users = User.objects.count()

    total_page_views = real_visits.count()

    total_unique_visitors = (
        real_visits
        .exclude(session_key="")
        .values("session_key")
        .distinct()
        .count()
    )

    today_page_views = (
        today_visits.count()
    )

    today_unique_visitors = (
        today_visits
        .exclude(session_key="")
        .values("session_key")
        .distinct()
        .count()
    )

    logged_in_views = (
        real_visits
        .filter(
            is_authenticated_visit=True
        )
        .count()
    )

    guest_views = (
        real_visits
        .filter(
            is_authenticated_visit=False
        )
        .count()
    )

    bot_views = (
        VisitorLog.objects
        .filter(is_bot=True)
        .count()
    )

    saved_tools_count = (
        SavedTool.objects.count()
    )

    recent_tools_count = (
        RecentViewedTool.objects.count()
    )


    # =====================================================
    # POPULAR PAGES
    # =====================================================

    popular_pages = list(

        real_visits
        .values("path")
        .annotate(
            views=Count("id")
        )
        .order_by("-views")[:15]

    )


    # =====================================================
    # TOOL STATISTICS
    # =====================================================

    tool_stats = []

    for slug, tool in TOOLS.items():

        saved_count = (
            SavedTool.objects
            .filter(tool_slug=slug)
            .count()
        )

        recent_count = (
            RecentViewedTool.objects
            .filter(tool_slug=slug)
            .count()
        )

        tool_stats.append(
            {
                "slug": slug,
                "name": tool.get(
                    "name",
                    slug,
                ),
                "icon": tool.get(
                    "icon",
                    "✦",
                ),
                "category": tool.get(
                    "category",
                    "AI Tool",
                ),
                "saved_count": saved_count,
                "recent_count": recent_count,
                "official_url": tool.get(
                    "official_url",
                    "#",
                ),
            }
        )


    tool_stats.sort(
        key=lambda item: (
            item["saved_count"]
            + item["recent_count"]
        ),
        reverse=True,
    )


    # =====================================================
    # DEVICE / BROWSER / OS
    # =====================================================

    browser_stats = list(

        real_visits
        .exclude(browser="")
        .values("browser")
        .annotate(
            total=Count("id")
        )
        .order_by("-total")[:10]

    )


    device_stats = list(

        real_visits
        .exclude(device_type="")
        .values("device_type")
        .annotate(
            total=Count("id")
        )
        .order_by("-total")[:10]

    )


    os_stats = list(

        real_visits
        .exclude(operating_system="")
        .values("operating_system")
        .annotate(
            total=Count("id")
        )
        .order_by("-total")[:10]

    )


    # =====================================================
    # 7 DAY TRAFFIC
    # =====================================================

    traffic_query = (

        real_visits
        .filter(
            visited_at__date__gte=seven_days_ago
        )
        .annotate(
            day=TruncDate(
                "visited_at"
            )
        )
        .values("day")
        .annotate(
            views=Count("id")
        )
        .order_by("day")

    )


    traffic_map = {

        item["day"]: item["views"]

        for item in traffic_query

    }


    traffic_labels = []
    traffic_values = []


    for offset in range(7):

        day = (
            seven_days_ago
            + timedelta(days=offset)
        )

        traffic_labels.append(
            day.strftime("%d %b")
        )

        traffic_values.append(
            traffic_map.get(
                day,
                0,
            )
        )


    # =====================================================
    # RECENT VISITORS
    # =====================================================

    visitor_filter = request.GET.get(
        "visitor_type",
        "all",
    )

    recent_visits_query = (
        real_visits
        .select_related("user")
    )


    if visitor_filter == "users":

        recent_visits_query = (
            recent_visits_query.filter(
                is_authenticated_visit=True
            )
        )


    elif visitor_filter == "guests":

        recent_visits_query = (
            recent_visits_query.filter(
                is_authenticated_visit=False
            )
        )


    recent_visits = (
        recent_visits_query
        .order_by("-visited_at")[:100]
    )


    # =====================================================
    # USERS
    # =====================================================

    users = (
        User.objects
        .order_by("-date_joined")
    )

    newest_users = users[:12]

    staff_users = (
        User.objects
        .filter(is_staff=True)
        .count()
    )

    active_users = (
        User.objects
        .filter(is_active=True)
        .count()
    )


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "active_tab":
            active_tab,

        "theme":
            theme,

        "total_users":
            total_users,

        "active_users":
            active_users,

        "staff_users":
            staff_users,

        "total_page_views":
            total_page_views,

        "total_unique_visitors":
            total_unique_visitors,

        "today_page_views":
            today_page_views,

        "today_unique_visitors":
            today_unique_visitors,

        "logged_in_views":
            logged_in_views,

        "guest_views":
            guest_views,

        "bot_views":
            bot_views,

        "saved_tools_count":
            saved_tools_count,

        "recent_tools_count":
            recent_tools_count,

        "popular_pages":
            popular_pages,

        "tool_stats":
            tool_stats,

        "browser_stats":
            browser_stats,

        "device_stats":
            device_stats,

        "os_stats":
            os_stats,

        "traffic_labels":
            traffic_labels,

        "traffic_values":
            traffic_values,

        "recent_visits":
            recent_visits,

        "visitor_filter":
            visitor_filter,

        "newest_users":
            newest_users,

        "users":
            users,

        "total_tools":
            len(TOOLS),

    }


    return render(
        request,
        "admin_dashboard.html",
        context,
    )