from django.shortcuts import render


# =========================================================
# AI TOOLS DATABASE
# =========================================================

TOOLS = {

    # =====================================================
    # VIDEO TOOLS
    # =====================================================

    "flow-ai": {
        "name": "Flow AI",
        "icon": "🌊",
        "category": "AI Video Generator",
        "description": "Create cinematic AI-generated videos, scenes and visual content using Google's creative AI platform.",
        "tags": [
            "Text to Video",
            "Image to Video",
            "Creative"
        ],
        "official_url": "https://labs.google/fx/tools/flow",
        "type": "Video Tool",
    },

    "ai-video-generator": {
        "name": "AI Video Generator",
        "icon": "🎬",
        "category": "Video Generator",
        "description": "Create AI-generated videos from text prompts and transform creative ideas into engaging visual content.",
        "tags": [
            "Text to Video",
            "AI Video"
        ],
        "official_url": "https://runwayml.com/",
        "type": "Video Tool",
    },

    "image-to-video-ai": {
        "name": "Image to Video AI",
        "icon": "🖼️",
        "category": "Image to Video",
        "description": "Transform static images into engaging animated videos with AI-powered image-to-video technology.",
        "tags": [
            "Image to Video",
            "Animation"
        ],
        "official_url": "https://pika.art/",
        "type": "Video Tool",
    },

    "ai-video-editor": {
        "name": "AI Video Editor",
        "icon": "✨",
        "category": "Video Editing",
        "description": "Edit and enhance videos with AI-powered editing tools, effects and creative features.",
        "tags": [
            "Video Editing",
            "AI"
        ],
        "official_url": "https://runwayml.com/",
        "type": "Video Tool",
    },

    "ai-avatar-video": {
        "name": "AI Avatar Video",
        "icon": "👤",
        "category": "AI Avatar",
        "description": "Create talking avatar videos from text using AI-generated presenters.",
        "tags": [
            "AI Avatar",
            "Talking Video"
        ],
        "official_url": "https://www.heygen.com/",
        "type": "Video Tool",
    },

    "ai-voice-video": {
        "name": "AI Voice Video",
        "icon": "🎙️",
        "category": "AI Voice",
        "description": "Create videos with AI voices, narration and realistic speech using AI-powered voice technology.",
        "tags": [
            "AI Voice",
            "Narration"
        ],
        "official_url": "https://www.heygen.com/",
        "type": "Video Tool",
    },

    "ai-animation-generator": {
        "name": "AI Animation Generator",
        "icon": "🚀",
        "category": "Animation",
        "description": "Create animated scenes and creative video content with artificial intelligence.",
        "tags": [
            "Animation",
            "Creative"
        ],
        "official_url": "https://pika.art/",
        "type": "Video Tool",
    },

    "runway": {
        "name": "Runway",
        "icon": "🎞️",
        "category": "AI Video",
        "description": "Create and edit AI-generated videos with advanced generative video tools.",
        "tags": [
            "Text to Video",
            "Video Editing"
        ],
        "official_url": "https://runwayml.com/",
        "type": "Video Tool",
    },

    "pika": {
        "name": "Pika",
        "icon": "⚡",
        "category": "AI Video Generator",
        "description": "Generate creative AI videos and animations from text and images.",
        "tags": [
            "AI Video",
            "Animation"
        ],
        "official_url": "https://pika.art/",
        "type": "Video Tool",
    },

    "heygen": {
        "name": "HeyGen",
        "icon": "🧑‍💻",
        "category": "AI Avatar",
        "description": "Create professional AI avatar videos, presentations and talking videos.",
        "tags": [
            "AI Avatar",
            "Voice"
        ],
        "official_url": "https://www.heygen.com/",
        "type": "Video Tool",
    },


    # =====================================================
    # IMAGE TOOLS
    # =====================================================

    "chatgpt-image-generator": {
        "name": "ChatGPT Image Generator",
        "icon": "🤖",
        "category": "Image Generator",
        "description": "Create detailed and creative images from simple text prompts using AI image generation.",
        "tags": [
            "Text to Image",
            "Creative"
        ],
        "official_url": "https://chatgpt.com/",
        "type": "Image Tool",
    },

    "midjourney": {
        "name": "Midjourney",
        "icon": "🎨",
        "category": "AI Art",
        "description": "Generate high-quality artistic images and stunning visuals using advanced AI.",
        "tags": [
            "AI Art",
            "Creative"
        ],
        "official_url": "https://www.midjourney.com/",
        "type": "Image Tool",
    },

    "adobe-firefly": {
        "name": "Adobe Firefly",
        "icon": "🔥",
        "category": "AI Generator",
        "description": "Create and edit images with generative AI tools designed for creative professionals.",
        "tags": [
            "Generation",
            "Editing"
        ],
        "official_url": "https://firefly.adobe.com/",
        "type": "Image Tool",
    },

    "canva-ai": {
        "name": "Canva AI",
        "icon": "🖌️",
        "category": "Design",
        "description": "Generate images and creative designs with AI-powered Canva features.",
        "tags": [
            "Design",
            "AI Image"
        ],
        "official_url": "https://www.canva.com/",
        "type": "Image Tool",
    },

    "leonardo-ai": {
        "name": "Leonardo AI",
        "icon": "🦁",
        "category": "AI Art",
        "description": "Generate detailed images, characters and creative artwork with AI.",
        "tags": [
            "Image Generation",
            "Art"
        ],
        "official_url": "https://leonardo.ai/",
        "type": "Image Tool",
    },

    "remove-bg": {
        "name": "Remove.bg",
        "icon": "✂️",
        "category": "Background",
        "description": "Remove image backgrounds automatically and create transparent background images.",
        "tags": [
            "Background Remover",
            "Editing"
        ],
        "official_url": "https://www.remove.bg/",
        "type": "Image Tool",
    },

    "photoroom": {
        "name": "Photoroom",
        "icon": "📸",
        "category": "Photo Editing",
        "description": "Edit product photos, remove backgrounds and create professional visuals with AI.",
        "tags": [
            "Editing",
            "Background"
        ],
        "official_url": "https://www.photoroom.com/",
        "type": "Image Tool",
    },

    "pixlr": {
        "name": "Pixlr",
        "icon": "🪄",
        "category": "Photo Editor",
        "description": "Edit photos online with AI-powered tools, filters and creative image features.",
        "tags": [
            "Photo Editing",
            "AI Tools"
        ],
        "official_url": "https://pixlr.com/",
        "type": "Image Tool",
    },

    "upscale-media": {
        "name": "Upscale.media",
        "icon": "🚀",
        "category": "Image Enhancer",
        "description": "Increase image resolution and improve image quality using AI-powered upscaling.",
        "tags": [
            "Upscaling",
            "Enhancement"
        ],
        "official_url": "https://www.upscale.media/",
        "type": "Image Tool",
    },

}


# =========================================================
# ADD SLUG TO EVERY TOOL
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

    featured_tools = {}

    for slug in featured_slugs:

        tool = TOOLS.get(slug)

        if tool:
            featured_tools[slug] = tool

    return render(
        request,
        "home.html",
        {
            "featured_tools": featured_tools,
        }
    )


# =========================================================
# AI IMAGE TOOLS PAGE
# =========================================================

def image_tools(request):

    image_tools_list = []

    for slug, tool in TOOLS.items():

        if tool["type"] == "Image Tool":

            image_tools_list.append(tool)

    return render(
        request,
        "image_tools.html",
        {
            "tools": image_tools_list,
            "tool_count": len(image_tools_list),
        }
    )


# =========================================================
# AI VIDEO TOOLS PAGE
# =========================================================

def video_tools(request):

    video_tools_list = []

    for slug, tool in TOOLS.items():

        if tool["type"] == "Video Tool":

            video_tools_list.append(tool)

    return render(
        request,
        "video_tools.html",
        {
            "tools": video_tools_list,
            "tool_count": len(video_tools_list),
        }
    )


# =========================================================
# TOOL DETAIL PAGE
# =========================================================

def tool_detail(request, slug):

    tool = TOOLS.get(slug)

    if not tool:

        return render(
            request,
            "tool_detail.html",
            {
                "tool": {
                    "name": "Tool Not Found",
                    "slug": "",
                    "icon": "❌",
                    "category": "Unknown",
                    "description": "The requested AI tool could not be found.",
                    "tags": [],
                    "official_url": "/",
                    "type": "AI Tool",
                }
            },
            status=404
        )

    return render(
        request,
        "tool_detail.html",
        {
            "tool": tool
        }
    )


# =========================================================
# ABOUT PAGE
# =========================================================

def about(request):

    return render(
        request,
        "about.html"
    )


# =========================================================
# PRIVACY PAGE
# =========================================================

def privacy(request):

    return render(
        request,
        "privacy.html"
    )


# =========================================================
# TERMS PAGE
# =========================================================

def terms(request):

    return render(
        request,
        "terms.html"
    )


# =========================================================
# DISCLAIMER PAGE
# =========================================================

def disclaimer(request):

    return render(
        request,
        "disclaimer.html"
    )


# =========================================================
# CONTACT PAGE
# =========================================================

def contact(request):

    return render(
        request,
        "contact.html"
    )