from django.contrib import admin
from django.urls import path, include

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


urlpatterns = [

    # Django Admin
    path("admin/", admin.site.urls),

    # Home
    path("", home, name="home"),

    # AI Tools
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

    # Information / Legal Pages
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

    # Normal Veylora AI Authentication
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

    # Welcome Screen
    path(
        "welcome/",
        welcome_view,
        name="welcome",
    ),

    # django-allauth
    # Google Social Login
    path(
        "accounts/",
        include("allauth.urls"),
    ),
]