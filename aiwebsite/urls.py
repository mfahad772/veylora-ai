from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from tools.views import (
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
# VEYLORA AI FAVICON
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
# URLS
# =========================================================

urlpatterns = [

    # Favicon
    path(
        "favicon.ico",
        favicon_view,
        name="favicon",
    ),

    # Django Admin
    path(
        "admin/",
        admin.site.urls,
    ),

    # Home
    path(
        "",
        home,
        name="home",
    ),

    # AI Image Tools
    path(
        "ai-image-tools/",
        image_tools,
        name="image_tools",
    ),

    # AI Video Tools
    path(
        "ai-video-tools/",
        video_tools,
        name="video_tools",
    ),

    # Tool Detail
    path(
        "tool/<slug:slug>/",
        tool_detail,
        name="tool_detail",
    ),

    # About
    path(
        "about/",
        about,
        name="about",
    ),

    # Privacy
    path(
        "privacy/",
        privacy,
        name="privacy",
    ),

    # Terms
    path(
        "terms/",
        terms,
        name="terms",
    ),

    # Disclaimer
    path(
        "disclaimer/",
        disclaimer,
        name="disclaimer",
    ),

    # Contact
    path(
        "contact/",
        contact,
        name="contact",
    ),

    # Login
    path(
        "login/",
        login_view,
        name="login",
    ),

    # Signup
    path(
        "signup/",
        signup_view,
        name="signup",
    ),

    # Logout
    path(
        "logout/",
        logout_view,
        name="logout",
    ),

    # Profile
    path(
        "profile/",
        profile_view,
        name="profile",
    ),

    # Welcome
    path(
        "welcome/",
        welcome_view,
        name="welcome",
    ),

    # Google Social Login / django-allauth
    path(
        "accounts/",
        include("allauth.urls"),
    ),
]