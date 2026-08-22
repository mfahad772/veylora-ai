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
            "Explore Google Flow for creating cinematic AI videos "
            "from prompts, ideas and visual references."
        ),
        "overview": (
            "Flow AI is designed for creators who want to experiment "
            "with AI-assisted filmmaking and visual storytelling. "
            "It can be useful for generating scenes, testing creative "
            "ideas and developing video concepts with generative AI."
        ),
        "best_for": (
            "AI filmmakers, content creators, visual storytellers "
            "and creators experimenting with cinematic AI video."
        ),
        "features": [
            "AI-assisted video creation",
            "Text-driven creative workflows",
            "Cinematic scene generation",
            "Visual storytelling workflows",
            "Creative concept development",
        ],
        "use_cases": [
            "Creating cinematic AI video concepts",
            "Testing short-film ideas",
            "Developing visual scenes from prompts",
            "Experimenting with generative filmmaking",
        ],
        "tags": [
            "AI Video",
            "Text to Video",
            "Google AI",
            "Cinematic Video",
            "AI Filmmaking",
        ],
        "official_url": "https://labs.google/fx/tools/flow",
        "type": "video",
    },


    "ai-video-generator": {
        "name": "AI Video Generator",
        "icon": "🎥",
        "category": "AI Video Generator",
        "description": (
            "Create AI-generated videos from text ideas and creative "
            "prompts using Canva's AI video creation tools."
        ),
        "overview": (
            "AI video generation can help creators turn written ideas "
            "into visual content more quickly. Canva combines AI-assisted "
            "generation with design and editing tools, making it useful "
            "for social content, presentations and creative video projects."
        ),
        "best_for": (
            "Social media creators, marketers, beginners and users "
            "who want AI video generation together with design tools."
        ),
        "features": [
            "AI-assisted video generation",
            "Text-based creative workflows",
            "Video design and editing tools",
            "Templates and visual assets",
            "Browser-based creative workflow",
        ],
        "use_cases": [
            "Creating social media videos",
            "Turning ideas into short visual content",
            "Creating promotional video concepts",
            "Building presentation-style videos",
        ],
        "tags": [
            "AI Video Generator",
            "Text to Video",
            "Canva AI",
            "Video Creation",
            "Creative AI",
        ],
        "official_url": "https://www.canva.com/ai-video-generator/",
        "type": "video",
    },


    "image-to-video-ai": {
        "name": "Image to Video AI",
        "icon": "🖼️",
        "category": "Image to Video",
        "description": (
            "Turn still images into animated AI videos with motion, "
            "creative effects and image-to-video generation using Pika."
        ),
        "overview": (
            "Image-to-video AI tools can transform a static picture into "
            "a moving visual sequence. Pika is useful for creators who "
            "want to animate artwork, photos or AI-generated images for "
            "short videos and creative experiments."
        ),
        "best_for": (
            "AI artists, social creators and users who want to animate "
            "still images without traditional animation workflows."
        ),
        "features": [
            "Image-to-video generation",
            "AI motion effects",
            "Creative animation workflows",
            "Prompt-based video generation",
            "Short-form visual creation",
        ],
        "use_cases": [
            "Animating AI-generated images",
            "Creating short social clips",
            "Adding motion to artwork",
            "Experimenting with image animation",
        ],
        "tags": [
            "Image to Video",
            "AI Animation",
            "Pika",
            "AI Video",
            "Photo Animation",
        ],
        "official_url": "https://pika.art/",
        "type": "video",
    },


    "ai-video-editor": {
        "name": "AI Video Editor",
        "icon": "✂️",
        "category": "AI Video Editing",
        "description": (
            "Edit and enhance videos with AI-assisted editing features "
            "and creative video tools available through CapCut."
        ),
        "overview": (
            "AI-assisted video editors can reduce repetitive editing work "
            "and help creators produce content faster. CapCut combines "
            "traditional timeline editing with automated and AI-powered "
            "creative features for short-form and general video editing."
        ),
        "best_for": (
            "TikTok creators, YouTube creators, short-form editors "
            "and users who want an accessible AI-assisted video editor."
        ),
        "features": [
            "Video editing workflow",
            "AI-assisted creative tools",
            "Text and caption tools",
            "Effects and transitions",
            "Short-form video editing",
        ],
        "use_cases": [
            "Editing social media videos",
            "Creating short-form content",
            "Adding captions and effects",
            "Improving video presentation",
        ],
        "tags": [
            "AI Video Editor",
            "CapCut",
            "Video Editing",
            "Short Video",
            "Creative Tools",
        ],
        "official_url": "https://www.capcut.com/",
        "type": "video",
    },


    "ai-avatar-video": {
        "name": "D-ID AI Avatar Video",
        "icon": "👤",
        "category": "AI Avatar Video",
        "description": (
            "Create talking avatar videos and digital-human content using "
            "D-ID's AI video and avatar tools."
        ),
        "overview": (
            "D-ID provides AI-powered video and digital-human tools for "
            "creating talking avatars from images, scripts and audio. "
            "It is useful for personalized presentations, training, "
            "marketing content and avatar-led communication."
        ),
        "best_for": (
            "Businesses, educators, marketers and creators who want "
            "talking-avatar and digital-presenter video workflows."
        ),
        "features": [
            "Talking AI avatars",
            "Digital-human video creation",
            "Text and audio driven workflows",
            "Presenter-style content",
            "Personalized video creation",
        ],
        "use_cases": [
            "Creating explainer videos",
            "Building training content",
            "Creating personalized presentations",
            "Producing avatar-led marketing content",
        ],
        "tags": [
            "D-ID",
            "AI Avatar",
            "Talking Avatar",
            "Digital Human",
            "AI Video",
        ],
        "official_url": "https://www.d-id.com/ai-videos/",
        "type": "video",
    },


    "ai-voice-video": {
        "name": "AI Voice Video",
        "icon": "🎙️",
        "category": "AI Voice & Video",
        "description": (
            "Create presenter-style videos with AI-generated narration, "
            "voices and automated video workflows using Synthesia."
        ),
        "overview": (
            "AI voice video platforms can combine generated narration "
            "with digital presenters and visual content. Synthesia is "
            "particularly useful for structured business videos, training "
            "materials, tutorials and presentation-style content."
        ),
        "best_for": (
            "Businesses, trainers, educators and teams creating "
            "narrated or presenter-based video content."
        ),
        "features": [
            "AI-generated narration",
            "Digital presenter workflows",
            "Business video creation",
            "Script-to-video workflow",
            "Training content creation",
        ],
        "use_cases": [
            "Employee training videos",
            "Product explainers",
            "Educational presentations",
            "Narrated business content",
        ],
        "tags": [
            "AI Voice",
            "Synthesia",
            "AI Video",
            "AI Narration",
            "AI Presenter",
        ],
        "official_url": "https://www.synthesia.io/",
        "type": "video",
    },


    "ai-animation-generator": {
        "name": "Luma AI Video",
        "icon": "✨",
        "category": "AI Video & Animation",
        "description": (
            "Create generative AI video and animated visual content using "
            "Luma's current creative AI video platform."
        ),
        "overview": (
            "Luma provides generative video tools for turning creative ideas "
            "into moving visual content. Its current video generation stack "
            "is built around the Ray family of models and can support "
            "cinematic video, motion and creative visual experimentation."
        ),
        "best_for": (
            "Filmmakers, designers, digital artists and creators who want "
            "AI-generated motion and cinematic video workflows."
        ),
        "features": [
            "Generative AI video",
            "Text-to-video workflows",
            "Image-to-video workflows",
            "Creative motion generation",
            "Cinematic visual creation",
        ],
        "use_cases": [
            "Creating animated visual concepts",
            "Generating cinematic AI clips",
            "Animating still-image ideas",
            "Developing creative motion content",
        ],
        "tags": [
            "Luma AI",
            "AI Video",
            "Generative Video",
            "AI Animation",
            "Ray",
        ],
        "official_url": "https://app.lumalabs.ai/",
        "type": "video",
    },


    "runway": {
        "name": "Runway",
        "icon": "🚀",
        "category": "AI Video Generator",
        "description": (
            "Explore Runway's generative AI tools for creating, editing "
            "and transforming video and visual content."
        ),
        "overview": (
            "Runway is a generative creative platform focused heavily "
            "on AI video and visual production. It can support workflows "
            "ranging from experimental video generation to visual effects "
            "and AI-assisted editing."
        ),
        "best_for": (
            "Filmmakers, designers, AI video creators and visual artists "
            "who need advanced generative video workflows."
        ),
        "features": [
            "Generative AI video",
            "Text-driven video creation",
            "Visual transformation tools",
            "AI-assisted editing",
            "Creative production workflows",
        ],
        "use_cases": [
            "Generating AI video scenes",
            "Creating experimental films",
            "Transforming video footage",
            "Developing visual concepts",
        ],
        "tags": [
            "Runway",
            "AI Video Generator",
            "Generative AI",
            "Text to Video",
            "Video Editing",
        ],
        "official_url": "https://runwayml.com/",
        "type": "video",
    },


    "pika": {
        "name": "Pika",
        "icon": "⚡",
        "category": "AI Video Generator",
        "description": (
            "Generate and animate short AI videos from text prompts "
            "and images with Pika's creative video tools."
        ),
        "overview": (
            "Pika is built around quick generative video creation. "
            "Creators can experiment with text-driven videos, animated "
            "images and visual effects, making it useful for short-form "
            "creative content and AI video experimentation."
        ),
        "best_for": (
            "Social media creators, AI artists and beginners exploring "
            "text-to-video and image-to-video generation."
        ),
        "features": [
            "AI video generation",
            "Image-to-video animation",
            "Prompt-based creation",
            "Creative visual effects",
            "Short-form video workflows",
        ],
        "use_cases": [
            "Creating AI social videos",
            "Animating still images",
            "Generating short visual concepts",
            "Experimenting with AI effects",
        ],
        "tags": [
            "Pika",
            "AI Video Generator",
            "Image to Video",
            "Text to Video",
            "AI Animation",
        ],
        "official_url": "https://pika.art/",
        "type": "video",
    },


    "heygen": {
        "name": "HeyGen",
        "icon": "🧑‍💻",
        "category": "AI Avatar Video",
        "description": (
            "Create AI avatar videos, digital presenters and talking "
            "video content using HeyGen."
        ),
        "overview": (
            "HeyGen focuses on AI avatar and presenter-based video creation. "
            "It can help users produce professional-looking communication "
            "without requiring a traditional filming setup for every video."
        ),
        "best_for": (
            "Marketing teams, educators, businesses and creators "
            "producing avatar-led presentation videos."
        ),
        "features": [
            "AI avatar video",
            "Digital presenters",
            "AI voice workflows",
            "Talking video creation",
            "Presentation-style content",
        ],
        "use_cases": [
            "Marketing explainers",
            "Training videos",
            "Product demonstrations",
            "Digital presenter content",
        ],
        "tags": [
            "HeyGen",
            "AI Avatar",
            "AI Presenter",
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
            "Create AI-generated images from natural-language prompts "
            "and creative instructions using ChatGPT."
        ),
        "overview": (
            "ChatGPT can help users move from an idea to a generated "
            "visual through conversational prompting. It is useful for "
            "creative concepts, illustrations, marketing ideas, mockups "
            "and many other text-to-image workflows."
        ),
        "best_for": (
            "Creators, marketers, designers and general users who want "
            "a conversational AI image generation workflow."
        ),
        "features": [
            "Text-to-image generation",
            "Conversational prompting",
            "Creative image concepts",
            "Image iteration through instructions",
            "General creative workflows",
        ],
        "use_cases": [
            "Creating concept artwork",
            "Generating social media visuals",
            "Designing creative mockups",
            "Producing illustration ideas",
        ],
        "tags": [
            "ChatGPT",
            "AI Image Generator",
            "Text to Image",
            "OpenAI",
            "AI Art",
        ],
        "official_url": "https://chatgpt.com/",
        "type": "image",
    },


    "midjourney": {
        "name": "Midjourney",
        "icon": "🎨",
        "category": "AI Image Generator",
        "description": (
            "Generate detailed artistic images and creative visuals "
            "from natural-language prompts with Midjourney."
        ),
        "overview": (
            "Midjourney is widely used for stylized and imaginative "
            "AI-generated visuals. It can help artists, designers and "
            "creative professionals explore visual concepts, artwork "
            "and design directions from written prompts."
        ),
        "best_for": (
            "AI artists, concept designers and creators who prioritize "
            "artistic and visually expressive image generation."
        ),
        "features": [
            "Text-to-image generation",
            "Creative visual styles",
            "Concept art workflows",
            "Prompt-based image creation",
            "Artistic image generation",
        ],
        "use_cases": [
            "Creating concept art",
            "Generating fantasy artwork",
            "Developing visual mood boards",
            "Exploring creative design ideas",
        ],
        "tags": [
            "Midjourney",
            "AI Image Generator",
            "AI Art",
            "Text to Image",
            "Concept Art",
        ],
        "official_url": "https://www.midjourney.com/",
        "type": "image",
    },


    "adobe-firefly": {
        "name": "Adobe Firefly",
        "icon": "🔥",
        "category": "AI Image Generator",
        "description": (
            "Create and edit visual content with Adobe Firefly's "
            "generative AI image and design tools."
        ),
        "overview": (
            "Adobe Firefly brings generative AI into creative design "
            "workflows. It is useful for generating visual concepts, "
            "editing creative assets and experimenting with AI-assisted "
            "image production."
        ),
        "best_for": (
            "Designers, Adobe users, marketers and creative professionals "
            "working with AI-assisted visual design."
        ),
        "features": [
            "Generative image creation",
            "AI-assisted image editing",
            "Creative design workflows",
            "Text-driven visual generation",
            "Adobe creative integration",
        ],
        "use_cases": [
            "Generating design concepts",
            "Creating marketing visuals",
            "Editing creative images",
            "Developing visual assets",
        ],
        "tags": [
            "Adobe Firefly",
            "AI Image Generator",
            "Generative AI",
            "AI Design",
            "Image Editing",
        ],
        "official_url": "https://firefly.adobe.com/",
        "type": "image",
    },


    "canva-ai": {
        "name": "Canva AI",
        "icon": "🪄",
        "category": "AI Design Tool",
        "description": (
            "Create images, graphics and design content with Canva's "
            "AI-assisted visual creation tools."
        ),
        "overview": (
            "Canva combines AI-powered creative features with its broader "
            "design platform. It is useful for users who want to generate "
            "visual ideas and then place them directly into social media, "
            "presentation or marketing designs."
        ),
        "best_for": (
            "Beginners, marketers, social media creators and small teams "
            "who want AI features inside a design platform."
        ),
        "features": [
            "AI-assisted design",
            "Image generation workflows",
            "Graphic design tools",
            "Templates and layouts",
            "Social media design",
        ],
        "use_cases": [
            "Creating social media graphics",
            "Designing promotional content",
            "Building presentations",
            "Generating visual concepts",
        ],
        "tags": [
            "Canva AI",
            "AI Design Tool",
            "Image Generator",
            "Graphic Design",
            "Social Media Design",
        ],
        "official_url": "https://www.canva.com/ai-image-generator/",
        "type": "image",
    },


    "leonardo-ai": {
        "name": "Leonardo AI",
        "icon": "🧠",
        "category": "AI Image Generator",
        "description": (
            "Generate AI artwork, characters and detailed creative images "
            "using Leonardo AI."
        ),
        "overview": (
            "Leonardo AI focuses on creative image generation and visual "
            "asset workflows. It can be useful for game concepts, character "
            "ideas, artwork, product visuals and other design-oriented "
            "image generation tasks."
        ),
        "best_for": (
            "AI artists, game designers, character creators and users "
            "developing detailed visual assets."
        ),
        "features": [
            "AI image generation",
            "Character artwork workflows",
            "Creative asset generation",
            "Prompt-based image creation",
            "Visual concept development",
        ],
        "use_cases": [
            "Creating character concepts",
            "Generating game artwork",
            "Developing product visuals",
            "Creating digital artwork",
        ],
        "tags": [
            "Leonardo AI",
            "AI Image Generator",
            "AI Art",
            "Character Generator",
            "Creative Images",
        ],
        "official_url": "https://leonardo.ai/",
        "type": "image",
    },


    "remove-bg": {
        "name": "Remove.bg",
        "icon": "✂️",
        "category": "Background Remover",
        "description": (
            "Automatically remove image backgrounds and create transparent "
            "background images with Remove.bg."
        ),
        "overview": (
            "Remove.bg is focused on a simple but common image-editing task: "
            "separating a subject from its background automatically. "
            "It is useful for product images, profile photos, design assets "
            "and quick transparent-background workflows."
        ),
        "best_for": (
            "E-commerce sellers, designers, photographers and users "
            "who frequently need clean transparent backgrounds."
        ),
        "features": [
            "Automatic background removal",
            "Transparent image output",
            "Quick image processing",
            "Product image workflows",
            "Design-ready cutouts",
        ],
        "use_cases": [
            "Removing product backgrounds",
            "Creating profile cutouts",
            "Preparing design assets",
            "Creating transparent PNG-style visuals",
        ],
        "tags": [
            "Remove.bg",
            "Background Remover",
            "Remove Background",
            "Image Editing",
            "Transparent Background",
        ],
        "official_url": "https://www.remove.bg/",
        "type": "image",
    },


    "photoroom": {
        "name": "PhotoRoom",
        "icon": "📸",
        "category": "AI Photo Editor",
        "description": (
            "Edit product photos, remove backgrounds and create polished "
            "visual content using PhotoRoom's AI photo tools."
        ),
        "overview": (
            "PhotoRoom is especially useful for product and commercial "
            "photo workflows. It combines background editing with tools "
            "for creating clean visual assets for stores, marketplaces "
            "and promotional content."
        ),
        "best_for": (
            "Online sellers, product photographers, marketers and "
            "small businesses creating commercial product images."
        ),
        "features": [
            "AI photo editing",
            "Background removal",
            "Product image workflows",
            "Visual cleanup tools",
            "Marketing image creation",
        ],
        "use_cases": [
            "Editing e-commerce photos",
            "Creating marketplace listings",
            "Preparing product advertisements",
            "Producing clean product visuals",
        ],
        "tags": [
            "PhotoRoom",
            "AI Photo Editor",
            "Product Photos",
            "Background Removal",
            "Ecommerce Images",
        ],
        "official_url": "https://www.photoroom.com/",
        "type": "image",
    },


    "pixlr": {
        "name": "Pixlr",
        "icon": "🖌️",
        "category": "AI Image Editor",
        "description": (
            "Edit, enhance and transform photos online with Pixlr's "
            "AI-assisted image editing tools."
        ),
        "overview": (
            "Pixlr provides browser-based image editing with a mix of "
            "traditional editing and AI-assisted features. It is useful "
            "for creators who want quick photo edits without relying on "
            "a large desktop editing application."
        ),
        "best_for": (
            "Bloggers, social creators, students and users who want "
            "a browser-based AI-assisted photo editor."
        ),
        "features": [
            "Online photo editing",
            "AI-assisted image tools",
            "Image enhancement",
            "Creative effects",
            "Browser-based workflow",
        ],
        "use_cases": [
            "Editing social media photos",
            "Enhancing online images",
            "Creating quick graphics",
            "Applying creative photo effects",
        ],
        "tags": [
            "Pixlr",
            "AI Image Editor",
            "Photo Editor",
            "Online Image Editor",
            "AI Photo Editing",
        ],
        "official_url": "https://pixlr.com/",
        "type": "image",
    },


    "upscale-media": {
        "name": "Upscale.media",
        "icon": "🔍",
        "category": "AI Image Enhancer",
        "description": (
            "Increase image resolution and improve visual clarity "
            "with AI-powered image upscaling from Upscale.media."
        ),
        "overview": (
            "AI image upscaling is useful when an existing image is too "
            "small or lacks detail for a particular use. Upscale.media "
            "focuses on improving resolution and preparing images for "
            "larger or cleaner presentation."
        ),
        "best_for": (
            "Photographers, designers, online sellers and users who need "
            "higher-resolution versions of existing images."
        ),
        "features": [
            "AI image upscaling",
            "Resolution enhancement",
            "Image quality improvement",
            "Photo enlargement workflows",
            "Automated enhancement",
        ],
        "use_cases": [
            "Upscaling small images",
            "Improving product photos",
            "Preparing images for larger displays",
            "Enhancing older or low-resolution visuals",
        ],
        "tags": [
            "Upscale.media",
            "AI Image Upscaler",
            "Image Enhancer",
            "Photo Upscaling",
            "Increase Image Resolution",
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

    query = request.GET.get(
        "q",
        "",
    ).strip().lower()

    filtered_tools = {}

    for slug, tool in TOOLS.items():

        if tool["type"] != "image":
            continue

        searchable_text = " ".join([
            tool["name"],
            tool["category"],
            tool["description"],
            tool["overview"],
            tool["best_for"],
            " ".join(tool["features"]),
            " ".join(tool["use_cases"]),
            " ".join(tool["tags"]),
        ]).lower()

        if (
            not query
            or query in searchable_text
        ):
            filtered_tools[slug] = tool

    return render(
        request,
        "image_tools.html",
        {
            "tools": filtered_tools,
            "query": request.GET.get(
                "q",
                "",
            ),
        },
    )


# =========================================================
# VIDEO TOOLS
# =========================================================

def video_tools(request):

    query = request.GET.get(
        "q",
        "",
    ).strip().lower()

    filtered_tools = {}

    for slug, tool in TOOLS.items():

        if tool["type"] != "video":
            continue

        searchable_text = " ".join([
            tool["name"],
            tool["category"],
            tool["description"],
            tool["overview"],
            tool["best_for"],
            " ".join(tool["features"]),
            " ".join(tool["use_cases"]),
            " ".join(tool["tags"]),
        ]).lower()

        if (
            not query
            or query in searchable_text
        ):
            filtered_tools[slug] = tool

    return render(
        request,
        "video_tools.html",
        {
            "tools": filtered_tools,
            "query": request.GET.get(
                "q",
                "",
            ),
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
    return render(
        request,
        "about.html",
    )


def privacy(request):
    return render(
        request,
        "privacy.html",
    )


def terms(request):
    return render(
        request,
        "terms.html",
    )


def disclaimer(request):
    return render(
        request,
        "disclaimer.html",
    )


def contact(request):
    return render(
        request,
        "contact.html",
    )


# =========================================================
# SIGNUP
# =========================================================

def signup_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = UserCreationForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            auth_login(
                request,
                user,
                backend=(
                    "django.contrib.auth.backends."
                    "ModelBackend"
                ),
            )

            return redirect(
                "welcome"
            )

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

            auth_login(
                request,
                user,
            )

            return redirect(
                "welcome"
            )

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

    return redirect(
        "home"
    )


# =========================================================
# PROFILE
# =========================================================

@login_required(
    login_url="login"
)
def profile_view(request):

    return render(
        request,
        "profile.html",
    )


# =========================================================
# WELCOME
# =========================================================

@login_required(
    login_url="login"
)
def welcome_view(request):

    return render(
        request,
        "welcome.html",
    )