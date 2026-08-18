from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# =========================================================
# AI TOOLS DATA
# =========================================================

TOOLS = {

    # =====================================================
    # VIDEO TOOLS
    # =====================================================

    "flow-ai": {
        "name": "Flow AI",
        "icon": "🎬",
        "category": "AI Video Generator",
        "description": (
            "Create cinematic AI videos using Google's advanced "
            "Flow AI video creation platform."
        ),
        "tags": [
            "AI Video",
            "Text to Video",
            "Google AI",
            "Cinematic Video",
        ],
        "official_url": "https://labs.google/fx/tools/flow",
        "type": "video",
    },

    "ai-video-generator": {
        "name": "AI Video Generator",
        "icon": "🎥",
        "category": "AI Video Generator",
        "description": (
            "Generate creative AI videos from text prompts and "
            "ideas using artificial intelligence."
        ),
        "tags": [
            "Video Generator",
            "Text to Video",
            "AI Creation",
        ],
        "official_url": "https://www.canva.com/ai-video-generator/",
        "type": "video",
    },

    "image-to-video-ai": {
        "name": "Image to Video AI",
        "icon": "🖼️",
        "category": "Image to Video",
        "description": (
            "Turn static images into animated AI videos with "
            "motion and creative visual effects."
        ),
        "tags": [
            "Image to Video",
            "Animation",
            "AI Video",
        ],
        "official_url": "https://pika.art/",
        "type": "video",
    },

    "ai-video-editor": {
        "name": "AI Video Editor",
        "icon": "✂️",
        "category": "AI Video Editing",
        "description": (
            "Edit and enhance videos faster using AI-powered "
            "video editing features."
        ),
        "tags": [
            "Video Editing",
            "AI Editor",
            "Creative Tools",
        ],
        "official_url": "https://www.capcut.com/",
        "type": "video",
    },

    "ai-avatar-video": {
        "name": "AI Avatar Video",
        "icon": "👤",
        "category": "AI Avatar",
        "description": (
            "Create professional talking avatar videos using "
            "AI-generated presenters and voices."
        ),
        "tags": [
            "AI Avatar",
            "Talking Avatar",
            "Presentation",
        ],
        "official_url": "https://www.heygen.com/",
        "type": "video",
    },

    "ai-voice-video": {
        "name": "AI Voice Video",
        "icon": "🎙️",
        "category": "AI Voice & Video",
        "description": (
            "Create videos with artificial intelligence voices, "
            "narration and automated content."
        ),
        "tags": [
            "AI Voice",
            "Voiceover",
            "Video",
        ],
        "official_url": "https://www.synthesia.io/",
        "type": "video",
    },

    "ai-animation-generator": {
        "name": "AI Animation Generator",
        "icon": "✨",
        "category": "AI Animation",
        "description": (
            "Generate animated videos and creative visual scenes "
            "with artificial intelligence."
        ),
        "tags": [
            "Animation",
            "AI Video",
            "Creative",
        ],
        "official_url": "https://runwayml.com/",
        "type": "video",
    },

    "runway": {
        "name": "Runway",
        "icon": "🚀",
        "category": "AI Video Generator",
        "description": (
            "Runway provides powerful AI tools for generating, "
            "editing and transforming videos."
        ),
        "tags": [
            "Runway",
            "Text to Video",
            "Video Editing",
            "Generative AI",
        ],
        "official_url": "https://runwayml.com/",
        "type": "video",
    },

    "pika": {
        "name": "Pika",
        "icon": "⚡",
        "category": "AI Video Generator",
        "description": (
            "Pika helps creators generate and animate videos "
            "from text prompts and images."
        ),
        "tags": [
            "Pika",
            "AI Video",
            "Image to Video",
            "Animation",
        ],
        "official_url": "https://pika.art/",
        "type": "video",
    },

    "heygen": {
        "name": "HeyGen",
        "icon": "🧑‍💻",
        "category": "AI Avatar Video",
        "description": (
            "Create professional AI avatar and talking presenter "
            "videos with HeyGen."
        ),
        "tags": [
            "HeyGen",
            "AI Avatar",
            "Talking Video",
            "AI Voice",
        ],
        "official_url": "https://www.heygen.com/",
        "type": "video",
    },


    # =====================================================
    # IMAGE TOOLS
    # =====================================================

    "chatgpt-image-generator": {
        "name": "ChatGPT Image Generator",
        "icon": "🤖",
        "category": "AI Image Generator",
        "description": (
            "Generate creative images from text prompts using "
            "ChatGPT's AI image generation capabilities."
        ),
        "tags": [
            "ChatGPT",
            "Image Generator",
            "Text to Image",
            "OpenAI",
        ],
        "official_url": "https://chatgpt.com/",
        "type": "image",
    },

    "midjourney": {
        "name": "Midjourney",
        "icon": "🎨",
        "category": "AI Image Generator",
        "description": (
            "Create detailed and artistic AI-generated images "
            "from natural language prompts."
        ),
        "tags": [
            "Midjourney",
            "AI Art",
            "Text to Image",
        ],
        "official_url": "https://www.midjourney.com/",
        "type": "image",
    },

    "adobe-firefly": {
        "name": "Adobe Firefly",
        "icon": "🔥",
        "category": "AI Image Generator",
        "description": (
            "Adobe Firefly offers generative AI tools for images, "
            "design and creative editing."
        ),
        "tags": [
            "Adobe",
            "Firefly",
            "AI Images",
            "Design",
        ],
        "official_url": "https://firefly.adobe.com/",
        "type": "image",
    },

    "canva-ai": {
        "name": "Canva AI",
        "icon": "🪄",
        "category": "AI Design Tool",
        "description": (
            "Use Canva's AI features to create images, designs, "
            "graphics and other visual content."
        ),
        "tags": [
            "Canva",
            "AI Design",
            "Graphics",
            "Image",
        ],
        "official_url": "https://www.canva.com/ai-image-generator/",
        "type": "image",
    },

    "leonardo-ai": {
        "name": "Leonardo AI",
        "icon": "🧠",
        "category": "AI Image Generator",
        "description": (
            "Generate high-quality AI artwork, characters and "
            "creative images with Leonardo AI."
        ),
        "tags": [
            "Leonardo AI",
            "AI Art",
            "Image Generator",
        ],
        "official_url": "https://leonardo.ai/",
        "type": "image",
    },

    "remove-bg": {
        "name": "Remove.bg",
        "icon": "✂️",
        "category": "Background Remover",
        "description": (
            "Automatically remove image backgrounds quickly "
            "using artificial intelligence."
        ),
        "tags": [
            "Background Removal",
            "Image Editing",
            "AI",
        ],
        "official_url": "https://www.remove.bg/",
        "type": "image",
    },

    "photoroom": {
        "name": "PhotoRoom",
        "icon": "📸",
        "category": "AI Photo Editor",
        "description": (
            "Edit product photos, remove backgrounds and create "
            "professional visuals using AI."
        ),
        "tags": [
            "Photo Editor",
            "Background Removal",
            "AI Image",
        ],
        "official_url": "https://www.photoroom.com/",
        "type": "image",
    },

    "pixlr": {
        "name": "Pixlr",
        "icon": "🖌️",
        "category": "AI Image Editor",
        "description": (
            "Edit and enhance photos online with Pixlr's "
            "AI-powered image editing tools."
        ),
        "tags": [
            "Pixlr",
            "Photo Editing",
            "AI Editor",
        ],
        "official_url": "https://pixlr.com/",
        "type": "image",
    },

    "upscale-media": {
        "name": "Upscale.media",
        "icon": "🔍",
        "category": "AI Image Enhancer",
        "description": (
            "Enhance image resolution and improve image quality "
            "using AI-powered upscaling."
        ),
        "tags": [
            "Image Upscaler",
            "Enhancer",
            "AI Image",
        ],
        "official_url": "https://www.upscale.media/",
        "type": "image",
    },
}


# =========================================================
# ADD SLUG TO EACH TOOL
# =========================================================

for slug, tool in TOOLS.items():
    tool["slug"] = slug


# =========================================================
# HOME PAGE
# =========================================================

def home(request):

    featured_slugs = [
        "chatgpt-image-generator",
        "midjourney",
        "flow-ai",
    ]

    featured_tools = {
        slug: TOOLS[slug]
        for slug in featured_slugs
        if slug in TOOLS
    }

    return render(
        request,
        "home.html",
        {
            "featured_tools": featured_tools,
        },
    )


# =========================================================
# IMAGE TOOLS
# =========================================================

def image_tools(request):

    query = request.GET.get("q", "").strip().lower()

    filtered_tools = {}

    for slug, tool in TOOLS.items():

        if tool["type"] != "image":
            continue

        searchable_text = " ".join([
            tool["name"],
            tool["category"],
            tool["description"],
            " ".join(tool["tags"]),
        ]).lower()

        if not query or query in searchable_text:
            filtered_tools[slug] = tool

    return render(
        request,
        "image_tools.html",
        {
            "tools": filtered_tools,
            "query": request.GET.get("q", ""),
        },
    )


# =========================================================
# VIDEO TOOLS
# =========================================================

def video_tools(request):

    query = request.GET.get("q", "").strip().lower()

    filtered_tools = {}

    for slug, tool in TOOLS.items():

        if tool["type"] != "video":
            continue

        searchable_text = " ".join([
            tool["name"],
            tool["category"],
            tool["description"],
            " ".join(tool["tags"]),
        ]).lower()

        if not query or query in searchable_text:
            filtered_tools[slug] = tool

    return render(
        request,
        "video_tools.html",
        {
            "tools": filtered_tools,
            "query": request.GET.get("q", ""),
        },
    )


# =========================================================
# TOOL DETAIL
# =========================================================

def tool_detail(request, slug):

    tool = TOOLS.get(slug)

    if not tool:
        return redirect("home")

    return render(
        request,
        "tool_detail.html",
        {
            "tool": tool,
        },
    )


# =========================================================
# LEGAL / INFORMATION
# =========================================================

def about(request):
    return render(request, "about.html")


def privacy(request):
    return render(request, "privacy.html")


def terms(request):
    return render(request, "terms.html")


def disclaimer(request):
    return render(request, "disclaimer.html")


def contact(request):
    return render(request, "contact.html")


# =========================================================
# SIGNUP
# =========================================================

def signup_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            # IMPORTANT:
            # We have two authentication backends:
            #
            # 1. Django ModelBackend
            # 2. django-allauth AuthenticationBackend
            #
            # This user was created using normal Django signup,
            # so explicitly use Django's ModelBackend.

            auth_login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend",
            )

            return redirect("welcome")

    else:

        form = UserCreationForm()

    return render(
        request,
        "signup.html",
        {
            "form": form,
        },
    )


# =========================================================
# NORMAL LOGIN
# =========================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST,
        )

        if form.is_valid():

            user = form.get_user()

            # AuthenticationForm already authenticated
            # the user through Django's authentication system.

            auth_login(request, user)

            return redirect("welcome")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "login.html",
        {
            "form": form,
        },
    )


# =========================================================
# LOGOUT
# =========================================================

def logout_view(request):

    logout(request)

    return redirect("home")


# =========================================================
# PROFILE
# =========================================================

@login_required(login_url="login")
def profile_view(request):

    return render(
        request,
        "profile.html",
    )


# =========================================================
# WELCOME
# =========================================================

@login_required(login_url="login")
def welcome_view(request):

    return render(
        request,
        "welcome.html",
    )