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
# VEYLORA UNIQUE EDITORIAL CONTENT
# =========================================================
# VEYLORA UNIQUE EDITORIAL CONTENT START
EDITORIAL_DATA = {'flow-ai': {'review_summary': 'This tool is a strong fit for creators who think in scenes, shots and visual sequences rather than only one-click social clips. Its main value is the creative filmmaking workflow: a user can explore different scene ideas, visual directions and prompt variations before moving the strongest material into a conventional editing workflow.', 'strengths': ['Useful for cinematic concept development and visual pre-production.', 'Works well when a project is planned as a sequence of scenes rather than a single static output.', 'Good fit for creators who are comfortable refining prompts and visual references.'], 'limitations': ['Longer continuity may require multiple generations and careful iteration.', 'A generated clip still normally needs editing, sound and finishing in another workflow.', 'Model access, limits and available controls can change over time.'], 'choose_if': 'Choose it when your priority is cinematic ideation, scene creation and visual storytelling.', 'avoid_if': 'Consider a traditional editor first when you mainly need captions, cuts, music, transitions or template-based publishing.', 'practical_tip': 'Plan the purpose of each shot before generating. Short, clearly defined scene goals usually make iteration easier than asking one prompt to create an entire finished film.'}, 'ai-video-generator': {'review_summary': 'This listing suits creators who want AI-assisted generation inside a broader design workflow. The practical advantage is convenience: generated material can become part of a social post, presentation or marketing asset without forcing the user to build the complete layout from scratch.', 'strengths': ['Accessible for beginners and non-technical creators.', 'Useful when generation and design need to happen in the same project.', 'Good for marketing, presentation and social-content workflows.'], 'limitations': ['Specialist generative-video platforms can offer deeper motion or model controls.', 'Template-led output still needs customization to avoid looking generic.', 'Some advanced AI features or higher usage levels may depend on the current plan.'], 'choose_if': 'Choose it when speed, templates and an all-in-one creative workflow matter more than deep generative control.', 'avoid_if': 'Consider a specialist video generator when cinematic motion, shot consistency or advanced reference control is the main requirement.', 'practical_tip': 'Use generation for the difficult visual element, then spend time on branding, pacing and layout. The finished design usually matters more than the novelty of the generated clip.'}, 'image-to-video-ai': {'review_summary': 'Image-to-video is most useful when the creator already has a strong still image and wants to test motion without rebuilding the visual from zero. It works particularly well for short clips, product moments, artwork animation and social experiments where one visual idea is the center of attention.', 'strengths': ['Turns existing artwork or generated images into motion quickly.', 'Useful for short-form creative tests and social clips.', 'A practical way to explore camera or subject movement from a known starting image.'], 'limitations': ['Longer sequences can lose visual consistency.', 'Exact motion can require several attempts.', 'Complex scenes with many interacting objects are harder to control.'], 'choose_if': 'Choose it when you already have the image you like and the next problem is adding believable motion.', 'avoid_if': 'Consider text-to-video or conventional animation when you need a completely new scene, long continuity or frame-level control.', 'practical_tip': 'Start with a clean source image and describe one main motion at a time. Too many simultaneous actions often make the result less predictable.'}, 'ai-video-editor': {'review_summary': 'This type of tool is strongest as a finishing environment rather than a replacement for every generative video model. For Shorts, Reels and TikTok-style production, pacing, captions, audio and final assembly often contribute more to the finished result than generation alone.', 'strengths': ['Strong fit for short-form editing and final assembly.', 'Useful for captions, pacing, effects and social publishing.', 'Combines familiar editing tasks with AI-assisted shortcuts.'], 'limitations': ['It is not primarily designed for deep cinematic generation.', 'Some AI features can be plan-dependent.', 'Large or complex professional projects may still need a more advanced desktop editor.'], 'choose_if': 'Choose it when you already have footage or generated clips and need to turn them into a finished social video.', 'avoid_if': 'Choose a dedicated generator first when your main problem is creating new scenes that do not exist yet.', 'practical_tip': 'Use AI to save time on repetitive editing, but manually review the first seconds, caption timing and final cut because these directly affect viewer retention.'}, 'ai-avatar-video': {'review_summary': 'Avatar-video platforms are most useful for presenter-led communication. They can reduce the need to record the same type of explanation repeatedly and are therefore practical for training, onboarding, product explanations, personalized messages and other script-driven content.', 'strengths': ['Efficient for presenter-style scripted videos.', 'Useful for training, explanations and repeatable communication.', 'Can reduce camera-production requirements for straightforward talking-presenter content.'], 'limitations': ['Avatar delivery is not a substitute for natural acting in emotional scenes.', 'Naturalness can vary with script, voice and source material.', 'It is less suitable for cinematic storytelling with complex environments.'], 'choose_if': 'Choose it when the message is more important than cinematic action and a digital presenter fits the format.', 'avoid_if': 'Use conventional filming or generative scene tools when natural human performance, physical interaction or dramatic environments are central.', 'practical_tip': 'Write for speech, not for a document. Short sentences and natural pauses usually make presenter videos feel more convincing.'}, 'ai-voice-video': {'review_summary': 'AI voice and presenter workflows are best suited to structured communication such as tutorials, training and business explainers. The biggest benefit is repeatability: a team can update a script and produce a new version without organizing a complete filming session every time.', 'strengths': ['Practical for training and business communication.', 'Useful for repeatable script-to-video production.', 'Can simplify narration and presenter workflows.'], 'limitations': ['Formal presenter output may not suit entertainment-first content.', 'Voice and avatar naturalness still need human review.', 'Higher-volume or team use may require paid plans.'], 'choose_if': 'Choose it for structured narration, tutorials, onboarding and presenter-based communication.', 'avoid_if': 'Consider another workflow for cinematic scenes, natural interviews or highly expressive storytelling.', 'practical_tip': 'Keep scripts concise and conversational. Review names, numbers and technical terms carefully because pronunciation can change the credibility of the whole video.'}, 'ai-animation-generator': {'review_summary': 'Generative animation tools are useful for turning a visual idea into motion without manually constructing every frame. They are strongest for concept shots, stylized movement and creative experimentation where the creator is willing to iterate until motion and composition align.', 'strengths': ['Useful for motion concepts and creative visual experimentation.', 'Can shorten the path from a still idea to an animated test.', 'Good fit for artists and creators exploring generative movement.'], 'limitations': ['Precise timing and object movement can be difficult to reproduce exactly.', 'Temporal consistency may vary between generations.', 'A separate editor is usually still needed for a complete finished video.'], 'choose_if': 'Choose it when you want to explore visual motion quickly and can tolerate iterative generation.', 'avoid_if': 'Use deterministic animation software when exact keyframes, timing or repeatable movement are essential.', 'practical_tip': 'Treat the first result as a motion sketch. Refine one problem at a time—camera, subject motion or style—rather than changing every variable in the next prompt.'}, 'runway': {'review_summary': 'Runway is best suited to creators who want a broader AI-video production environment rather than a single generation button. Its value comes from combining generative creation with transformation and production-oriented tools, which can support more experimental visual workflows.', 'strengths': ['Broad generative-video and visual-production toolkit.', 'Useful for creators who want to experiment beyond basic text-to-video.', 'Good fit for visual transformation, concept shots and AI-assisted production.'], 'limitations': ['The broader feature set creates a steeper learning curve.', 'Repeated high-quality generations can consume credits quickly.', 'Consistency still depends on careful prompts, references and iteration.'], 'choose_if': 'Choose it when you want a more advanced AI filmmaking workspace and are comfortable learning a wider set of tools.', 'avoid_if': 'A simpler tool may be better if you only need a quick social clip, template or talking presenter.', 'practical_tip': 'Build a short test shot before committing credits to a longer sequence. Lock the visual direction first, then expand the idea.'}, 'pika': {'review_summary': 'Pika is a practical choice for fast, short-form experimentation. It works well when the goal is to turn a simple idea or image into a moving visual quickly, making it useful for social concepts, effects and creative tests where speed matters more than long narrative continuity.', 'strengths': ['Fast text- and image-to-video experimentation.', 'Good fit for short visual ideas and social effects.', 'Lower learning barrier than a full production suite.'], 'limitations': ['Long narrative continuity is not its main strength.', 'Fine motion control may require multiple attempts.', 'Frequent experimentation can run into usage or credit limits.'], 'choose_if': 'Choose it when you want to test a short visual idea quickly and value speed over deep production control.', 'avoid_if': 'Consider another workflow for long scenes, exact character continuity or professional timeline finishing.', 'practical_tip': 'Keep the action simple and make the starting image or prompt visually clear. A strong single idea usually produces a more usable short clip.'}, 'heygen': {'review_summary': 'HeyGen belongs to the presenter and avatar side of AI video rather than cinematic generation. It is useful when a business or creator needs repeatable scripted communication, product explanations or localized presenter content without scheduling a new recording session for every version.', 'strengths': ['Efficient presenter and avatar workflow.', 'Useful for product explainers, marketing and business communication.', 'Good fit for repeatable scripted content.'], 'limitations': ['Not intended to replace cinematic filmmaking tools.', 'Avatar realism depends on the selected voice, script and presenter.', 'Higher-volume business use can require paid tiers.'], 'choose_if': 'Choose it for presenter-led marketing, explainers, sales content or localized scripted communication.', 'avoid_if': 'Use another workflow when natural live-action performance or complex cinematic scenes are the priority.', 'practical_tip': 'Use shorter paragraphs, natural punctuation and clear emphasis. A well-written script often improves the result more than adding extra visual effects.'}, 'chatgpt-image-generator': {'review_summary': 'The main advantage of a conversational image workflow is iteration. A user can develop the brief, request alternatives and refine individual elements through natural-language follow-ups instead of treating every image request as an isolated prompt.', 'strengths': ['Natural conversational refinement of image ideas.', 'Useful for general-purpose concept and marketing visuals.', 'Convenient when planning, writing and image creation happen in one workflow.'], 'limitations': ['Specialist batch and asset-management controls may be more limited.', 'Exact character or style consistency can still require iteration.', 'Available image features and limits can depend on the current product plan.'], 'choose_if': 'Choose it when you want to discuss an idea, refine the brief and create visuals in the same conversational workflow.', 'avoid_if': 'A specialist platform may fit better if you need advanced batch controls, highly specialized model settings or a dedicated production pipeline.', 'practical_tip': 'Describe the subject, setting, composition and intended use before styling. Clear creative direction is usually more reliable than a long list of visual adjectives.'}, 'midjourney': {'review_summary': 'Midjourney is a strong fit for visual exploration, atmosphere and concept-art direction. It rewards users who are willing to test variations and develop a visual language, especially when the objective is an expressive image rather than a rigid marketing layout.', 'strengths': ['Strong artistic and concept-development orientation.', 'Useful for mood, style and visual exploration.', 'Good for creators who enjoy iterative variation workflows.'], 'limitations': ['Precise typography and layout may need a separate design tool.', 'The workflow can take time to learn for new users.', 'Exact subject consistency across many assets requires careful iteration.'], 'choose_if': 'Choose it when art direction, atmosphere and visual impact matter more than exact editable layout.', 'avoid_if': 'Use another tool when accurate text, strict brand layouts or a simple utility task is the main requirement.', 'practical_tip': 'Create a small set of visual directions first. Once one direction is strong, refine that branch instead of restarting with unrelated prompts.'}, 'adobe-firefly': {'review_summary': 'Firefly is most valuable when AI generation is part of a larger design and editing process. Its practical advantage is the connection between generative creation and established production workflows used for marketing, design and image editing.', 'strengths': ['Natural fit for Adobe-oriented creative workflows.', 'Useful for both generation and generative editing.', 'Good option for designers who need AI close to production tools.'], 'limitations': ['Users outside the Adobe ecosystem may gain less workflow benefit.', 'Pure art exploration may feel less specialized than art-first generators.', 'Generative usage can be affected by current plan or credit policies.'], 'choose_if': 'Choose it when generated material will continue into an Adobe-centered design or editing workflow.', 'avoid_if': 'A lighter tool may be better when you only need one quick utility task or an art-first experimentation environment.', 'practical_tip': 'Use AI for the part of the image that needs invention or repair, then finish typography, layout and brand details with conventional design controls.'}, 'canva-ai': {'review_summary': 'Canva AI is most useful when generation is only one step in a finished design. The surrounding layout, template and brand workflow makes it practical for creators who need to move quickly from an idea to a social post, presentation or marketing asset.', 'strengths': ['Generation and design layout live in one workflow.', 'Beginner-friendly templates and publishing tools.', 'Useful for fast social, presentation and marketing production.'], 'limitations': ['Specialist generators can provide deeper model controls.', 'Template-led work still needs customization to feel original.', 'Some AI and brand features can depend on the current plan.'], 'choose_if': 'Choose it when speed, layout and publishing matter as much as the generated image.', 'avoid_if': 'Consider a specialist generator when highly detailed art direction or advanced model control is the main goal.', 'practical_tip': 'Do not stop at the generated image. Adjust spacing, typography, brand elements and crop so the final asset looks intentionally designed.'}, 'leonardo-ai': {'review_summary': 'Leonardo AI is a stronger fit for asset-oriented creators who want more control than a basic prompt box. It can be useful for concept art, game-style assets, character ideas and repeatable visual exploration where multiple related outputs are needed.', 'strengths': ['Good fit for characters, concepts and creative assets.', 'More control-oriented than very simple image generators.', 'Useful for creators building several related visual ideas.'], 'limitations': ['The number of controls can feel complex to beginners.', 'Consistent characters still require careful references and prompting.', 'Heavy experimentation can be limited by tokens or plan allowances.'], 'choose_if': 'Choose it when you need detailed asset exploration and want more generation controls than a simple beginner tool.', 'avoid_if': 'A simpler design tool may be faster for basic social graphics, background removal or quick photo cleanup.', 'practical_tip': 'Save the settings and references that produced a good direction. Reusing a successful setup is more efficient than changing every parameter for each asset.'}, 'remove-bg': {'review_summary': 'Remove.bg is valuable because it focuses on one common production problem: separating a subject from the background quickly. For product photos, profile cutouts and design assets, a focused utility can be much faster than opening a full image editor.', 'strengths': ['Fast single-purpose background-removal workflow.', 'Useful for transparent product, profile and design cutouts.', 'Very small learning curve.'], 'limitations': ['It is not a complete photo editor.', 'Fine hair, glass and translucent objects can still need cleanup.', 'High-resolution or high-volume use may depend on paid options.'], 'choose_if': 'Choose it when the main task is simply separating a subject from its background.', 'avoid_if': 'Use a broader editor when you also need retouching, compositing, color correction or generative scene changes.', 'practical_tip': 'Always inspect difficult edges at full size before publishing. Automatic removal can look correct at a glance while leaving small halos or missing details.'}, 'photoroom': {'review_summary': 'PhotoRoom is particularly useful for sellers and small businesses because it treats product photography as a repeatable workflow. Background cleanup, product presentation and marketplace-ready imagery are more central here than artistic concept generation.', 'strengths': ['Strong e-commerce and product-photo focus.', 'Fast background and presentation workflows.', 'Useful for marketplace, catalogue and promotional assets.'], 'limitations': ['Less suitable for art-first image generation.', 'Some commercial features can be plan-dependent.', 'Complex professional retouching may still need a full editor.'], 'choose_if': 'Choose it when you regularly prepare product images for stores, marketplaces or advertising.', 'avoid_if': 'Consider another tool when the goal is concept art, cinematic illustration or deep manual photo manipulation.', 'practical_tip': 'Create a consistent background, crop and shadow style for a product range. Consistency across listings often matters more than a dramatic effect on one image.'}, 'pixlr': {'review_summary': 'Pixlr is a practical middle ground between a one-purpose AI utility and a heavy desktop editor. Its browser-based workflow is useful for everyday image cleanup, quick graphics and edits where installing or opening a larger application would slow the task down.', 'strengths': ['Browser-based editing with low setup friction.', 'Combines conventional editing with AI-assisted features.', 'Useful for everyday graphics and quick image cleanup.'], 'limitations': ['Not as deep as a full professional desktop editing suite.', 'Browser performance can depend on device and project size.', 'Some advanced or AI functions may be plan-dependent.'], 'choose_if': 'Choose it when you want a lightweight online editor with more flexibility than a single-purpose utility.', 'avoid_if': 'Use a full professional editor for complex compositing, very large production files or advanced color-managed work.', 'practical_tip': 'Use AI-assisted tools for speed, then review edges, text and export size manually before publishing the final image.'}, 'upscale-media': {'review_summary': 'AI upscaling is useful when an image is too small for its intended use, but it should be treated as enhancement rather than guaranteed recovery of real detail. A good upscaler can improve perceived clarity and make an asset more usable, especially for web, product and older images.', 'strengths': ['Simple resolution-enhancement workflow.', 'Useful for small product, web and older images.', 'Low learning curve for occasional users.'], 'limitations': ['Upscaling cannot guarantee detail that was never captured.', 'Faces, text and fine textures can sometimes develop artifacts.', 'It does not replace restoration or manual retouching.'], 'choose_if': 'Choose it when insufficient resolution is the main problem and you need a cleaner larger version quickly.', 'avoid_if': 'Use restoration or editing tools when the image also has damage, wrong objects, severe blur or major composition problems.', 'practical_tip': 'Compare the enhanced image at 100% zoom. If text, skin or fine patterns look artificial, use a lower enhancement level or keep the original size.'}}

for _slug, _editorial in EDITORIAL_DATA.items():
    if _slug in TOOLS:
        TOOLS[_slug].update(_editorial)
# VEYLORA UNIQUE EDITORIAL CONTENT END

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