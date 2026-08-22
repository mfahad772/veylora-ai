from pathlib import Path
from urllib.request import Request, urlopen
import re


# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

LOGO_DIR = (
    BASE_DIR
    / "tools"
    / "static"
    / "tools"
    / "logos"
)

TEMPLATE_DIR = (
    BASE_DIR
    / "tools"
    / "templates"
)


# =========================================================
# TOOL -> OFFICIAL DOMAIN
# =========================================================

TOOLS = {

    # VIDEO TOOLS
    "flow-ai": "labs.google",
    "ai-video-generator": "canva.com",
    "image-to-video-ai": "pika.art",
    "ai-video-editor": "capcut.com",
    "ai-avatar-video": "heygen.com",
    "ai-voice-video": "synthesia.io",
    "ai-animation-generator": "runwayml.com",
    "runway": "runwayml.com",
    "pika": "pika.art",
    "heygen": "heygen.com",

    # IMAGE TOOLS
    "chatgpt-image-generator": "chatgpt.com",
    "midjourney": "midjourney.com",
    "adobe-firefly": "firefly.adobe.com",
    "canva-ai": "canva.com",
    "leonardo-ai": "leonardo.ai",
    "remove-bg": "remove.bg",
    "photoroom": "photoroom.com",
    "pixlr": "pixlr.com",
    "upscale-media": "upscale.media",
}


# =========================================================
# CREATE LOGO DIRECTORY
# =========================================================

LOGO_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# =========================================================
# DOWNLOAD OFFICIAL-SITE ICONS
# =========================================================

print("\nDownloading brand logos...\n")

for slug, domain in TOOLS.items():

    output_file = (
        LOGO_DIR
        / f"{slug}.png"
    )

    url = (
        "https://www.google.com/s2/favicons"
        f"?domain={domain}&sz=128"
    )

    try:

        request = Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "Veylora-AI-Logo-Setup"
                )
            },
        )

        with urlopen(
            request,
            timeout=20,
        ) as response:

            data = response.read()

        if len(data) < 100:
            raise ValueError(
                "Downloaded logo is too small"
            )

        output_file.write_bytes(
            data
        )

        print(
            f"[OK] {slug}"
        )

    except Exception as error:

        print(
            f"[ERROR] {slug}: {error}"
        )


# =========================================================
# TEMPLATE LOGO HTML
# =========================================================

NEW_ICON_HTML = """<div class="tool-icon">
                    <img
                        src="/static/tools/logos/{{ tool.slug }}.png"
                        alt="{{ tool.name }} official logo"
                        loading="lazy"
                    >
                </div>"""


# =========================================================
# LOGO CSS
# =========================================================

LOGO_CSS = """

        /* =========================================
           OFFICIAL TOOL LOGOS
        ========================================= */

        .tool-icon img {
            width: 44px;
            height: 44px;

            display: block;

            object-fit: contain;

            border-radius: 10px;
        }

"""


# =========================================================
# UPDATE TEMPLATE
# =========================================================

def update_template(filename):

    path = (
        TEMPLATE_DIR
        / filename
    )

    if not path.exists():

        print(
            f"[SKIP] {filename} not found"
        )

        return


    html = path.read_text(
        encoding="utf-8"
    )


    # -----------------------------------------------------
    # Replace emoji tool.icon block
    # -----------------------------------------------------

    pattern = re.compile(
        r'<div\s+class="tool-icon"\s*>\s*'
        r'\{\{\s*tool\.icon\s*\}\}'
        r'\s*</div>',
        flags=re.IGNORECASE,
    )

    html, replacements = (
        pattern.subn(
            NEW_ICON_HTML,
            html,
        )
    )


    # -----------------------------------------------------
    # Add CSS once
    # -----------------------------------------------------

    if (
        "OFFICIAL TOOL LOGOS"
        not in html
    ):

        html = html.replace(
            "</style>",
            LOGO_CSS
            + "\n    </style>",
            1,
        )


    path.write_text(
        html,
        encoding="utf-8",
    )


    print(
        f"[UPDATED] {filename} "
        f"({replacements} icon block(s))"
    )


# =========================================================
# UPDATE PUBLIC PAGES
# =========================================================

update_template(
    "image_tools.html"
)

update_template(
    "video_tools.html"
)

update_template(
    "tool_detail.html"
)

update_template(
    "home.html"
)


# =========================================================
# FINISH
# =========================================================

print(
    "\n===================================="
)

print(
    "Official logo setup completed."
)

print(
    "====================================\n"
)