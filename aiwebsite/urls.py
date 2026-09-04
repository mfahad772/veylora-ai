from django.contrib import admin
from django.urls import path, include, reverse
from django.http import HttpResponse

from tools import views
from tools.views import TOOLS

from tools.tool_access import (
    protected_tool_access,
    protected_official_access,
    welcome_router,
)

from tools.saved_tools import (
    toggle_saved_tool,
    saved_tools_view,
)

from tools.recent_tools import (
    recent_tools_view,
    clear_recent_tools,
)

from tools.admin_panel import (
    admin_dashboard,
)


BASE_URL = "https://veyloraai.online"


# =========================================================
# FAVICON
# =========================================================

def favicon_view(request):

    svg = """
    <svg xmlns="http://www.w3.org/2000/svg"
         width="64"
         height="64"
         viewBox="0 0 64 64">

        <defs>

            <linearGradient
                id="gradient"
                x1="0%"
                y1="0%"
                x2="100%"
                y2="100%"
            >

                <stop
                    offset="0%"
                    stop-color="#00d4ff"
                />

                <stop
                    offset="50%"
                    stop-color="#7b5cff"
                />

                <stop
                    offset="100%"
                    stop-color="#d946ef"
                />

            </linearGradient>

        </defs>

        <rect
            width="64"
            height="64"
            rx="14"
            fill="#070b14"
        />

        <path
            d="M14 16 L27 48 L37 48 L50 16 L40 16 L32 38 L24 16 Z"
            fill="url(#gradient)"
        />

    </svg>
    """

    return HttpResponse(
        svg,
        content_type="image/svg+xml",
    )


# =========================================================
# ROBOTS.TXT
# =========================================================

def robots_txt(request):

    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /control-panel/
Disallow: /accounts/
Disallow: /profile/
Disallow: /welcome/
Disallow: /saved-tools/
Disallow: /save-tool/
Disallow: /recent-tools/
Disallow: /clear-recent-tools/

Sitemap: https://veyloraai.online/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain",
    )


# =========================================================
# SITEMAP
# =========================================================

def sitemap_xml(request):

    public_pages = [
        "home",
        "image_tools",
        "video_tools",
        "about",
        "privacy",
        "terms",
        "disclaimer",
        "contact",
    ]

    urls = []

    for page_name in public_pages:

        urls.append(
            BASE_URL
            + reverse(
                page_name
            )
        )

    for slug in TOOLS.keys():

        urls.append(
            BASE_URL
            + reverse(
                "tool_detail",
                args=[slug],
            )
        )

    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    for url in urls:

        xml += f"""
    <url>
        <loc>{url}</loc>
    </url>
"""

    xml += """
</urlset>
"""

    return HttpResponse(
        xml,
        content_type="application/xml",
    )


# =========================================================
# URLS
# =========================================================


urlpatterns = [
    path("guides/", views.guides, name="guides"),
    path("guides/<slug:slug>/", views.guide_detail, name="guide_detail"),
    path(
        "ads.txt",
        lambda request: HttpResponse(
            "google.com, pub-9101955435716307, DIRECT, f08c47fec0942fa0\n",
            content_type="text/plain",
        ),
        name="ads_txt",
    ),


    # SEO
    path(
        "robots.txt",
        robots_txt,
        name="robots_txt",
    ),

    path(
        "sitemap.xml",
        sitemap_xml,
        name="sitemap_xml",
    ),

    path(
        "favicon.ico",
        favicon_view,
        name="favicon",
    ),


    # =====================================================
    # VEYLORA CONTROL PANEL
    # =====================================================

    path(
        "control-panel/",
        admin_dashboard,
        name="veylora_admin",
    ),


    # DJANGO ADMIN
    path(
        "admin/",
        admin.site.urls,
    ),


    # HOME
    path(
        "",
        views.home,
        name="home",
    ),


    # IMAGE TOOLS
    path(
        "ai-image-tools/",
        views.image_tools,
        name="image_tools",
    ),


    # VIDEO TOOLS
    path(
        "ai-video-tools/",
        views.video_tools,
        name="video_tools",
    ),


    # TOOL DETAIL
    path(
        "tool/<slug:slug>/",
        views.tool_detail,
        name="tool_detail",
    ),


    # PROTECTED TOOL ACCESS
    path(
        "access-tool/<slug:slug>/",
        protected_tool_access,
        name="protected_tool_access",
    ),


    # OFFICIAL WEBSITE
    path(
        "go/<slug:slug>/",
        protected_official_access,
        name="protected_official_access",
    ),


    # SAVED TOOLS
    path(
        "saved-tools/",
        saved_tools_view,
        name="saved_tools",
    ),

    path(
        "save-tool/<slug:slug>/",
        toggle_saved_tool,
        name="toggle_saved_tool",
    ),


    # RECENTLY VIEWED TOOLS
    path(
        "recent-tools/",
        recent_tools_view,
        name="recent_tools",
    ),

    path(
        "clear-recent-tools/",
        clear_recent_tools,
        name="clear_recent_tools",
    ),


    # ABOUT
    path(
        "about/",
        views.about,
        name="about",
    ),


    # PRIVACY
    path(
        "privacy/",
        views.privacy,
        name="privacy",
    ),


    # TERMS
    path(
        "terms/",
        views.terms,
        name="terms",
    ),


    # DISCLAIMER
    path(
        "disclaimer/",
        views.disclaimer,
        name="disclaimer",
    ),


    # CONTACT
    path(
        "contact/",
        views.contact,
        name="contact",
    ),


    # LOGIN
    path(
        "login/",
        views.login_view,
        name="login",
    ),


    # SIGNUP
    path(
        "signup/",
        views.signup_view,
        name="signup",
    ),


    # LOGOUT
    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),


    # PROFILE
    path(
        "profile/",
        views.profile_view,
        name="profile",
    ),


    # AFTER LOGIN
    path(
        "welcome/",
        welcome_router,
        name="welcome",
    ),


    # GOOGLE LOGIN
    path(
        "accounts/",
        include(
            "allauth.urls"
        ),
    ),

]