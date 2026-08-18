from django.contrib import admin
from django.urls import path, include, reverse
from django.http import HttpResponse
from xml.sax.saxutils import escape

from tools.views import (
    TOOLS,
    home,
    image_tools,
    video_tools,
    tool_detail,
    about,
    privacy,
    terms,
    disclaimer,
    contact,
    login_view,
    signup_view,
    logout_view,
    profile_view,
    welcome_view,
)


# =========================================================
# MAIN DOMAIN
# =========================================================

BASE_URL = "https://veyloraai.online"


# =========================================================
# FAVICON
# =========================================================

def favicon_view(request):
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <defs>
            <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#00d4ff"/>
                <stop offset="50%" stop-color="#6c5cff"/>
                <stop offset="100%" stop-color="#d946ef"/>
            </linearGradient>
        </defs>

        <rect width="100" height="100" rx="24" fill="#080b14"/>

        <path
            d="M22 25 L43 76 Q50 88 57 76 L79 25
               L65 25 L51 63 Q50 66 49 63
               L36 25 Z"
            fill="url(#g)"
        />

        <circle cx="76" cy="21" r="5" fill="#00eaff"/>
    </svg>
    """

    response = HttpResponse(
        svg,
        content_type="image/svg+xml"
    )

    response["Cache-Control"] = "public, max-age=86400"

    return response


# =========================================================
# ROBOTS.TXT
# =========================================================

def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /accounts/
Disallow: /profile/
Disallow: /welcome/

Sitemap: https://veyloraai.online/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )


# =========================================================
# SITEMAP.XML
# =========================================================

def sitemap_xml(request):

    urls = []

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

    for name in public_pages:
        urls.append(
            BASE_URL + reverse(name)
        )

    for slug in TOOLS.keys():

        urls.append(
            BASE_URL + reverse(
                "tool_detail",
                kwargs={"slug": slug}
            )
        )

    xml_urls = ""

    for url in urls:
        xml_urls += f"""
    <url>
        <loc>{escape(url)}</loc>
    </url>"""

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_urls}
</urlset>
"""

    return HttpResponse(
        sitemap,
        content_type="application/xml"
    )


# =========================================================
# URLS
# =========================================================

urlpatterns = [

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

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        home,
        name="home",
    ),

    path(
        "ai-image-tools/",
        image_tools,
        name="image_tools",
    ),

    path(
        "ai-video-tools/",
        video_tools,
        name="video_tools",
    ),

    path(
        "tool/<slug:slug>/",
        tool_detail,
        name="tool_detail",
    ),

    path(
        "about/",
        about,
        name="about",
    ),

    path(
        "privacy/",
        privacy,
        name="privacy",
    ),

    path(
        "terms/",
        terms,
        name="terms",
    ),

    path(
        "disclaimer/",
        disclaimer,
        name="disclaimer",
    ),

    path(
        "contact/",
        contact,
        name="contact",
    ),

    path(
        "login/",
        login_view,
        name="login",
    ),

    path(
        "signup/",
        signup_view,
        name="signup",
    ),

    path(
        "logout/",
        logout_view,
        name="logout",
    ),

    path(
        "profile/",
        profile_view,
        name="profile",
    ),

    path(
        "welcome/",
        welcome_view,
        name="welcome",
    ),

    path(
        "accounts/",
        include("allauth.urls"),
    ),
]