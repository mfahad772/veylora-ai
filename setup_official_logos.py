from pathlib import Path
from urllib.request import Request, urlopen


BASE_DIR = Path(__file__).resolve().parent
LOGO_DIR = BASE_DIR / "tools" / "static" / "tools" / "logos"
TEMPLATE_DIR = BASE_DIR / "tools" / "templates"

LOGO_DIR.mkdir(parents=True, exist_ok=True)

# Each slug is mapped to the official provider domain.
PROVIDERS = {
    # Video tools
    "flow-ai": "labs.google",
    "ai-video-generator": "canva.com",
    "image-to-video-ai": "pika.art",
    "ai-video-editor": "capcut.com",
    "ai-avatar-video": "d-id.com",
    "ai-voice-video": "synthesia.io",
    "ai-animation-generator": "lumalabs.ai",
    "runway": "runwayml.com",
    "pika": "pika.art",
    "heygen": "heygen.com",

    # Image tools
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

TEMPLATES = [
    "image_tools.html",
    "video_tools.html",
    "tool_detail.html",
    "home.html",
]

OLD_ICON_BLOCK = '<div class="tool-icon">{{ tool.icon }}</div>'
NEW_ICON_BLOCK = '''<div class="tool-icon">
    <img
        src="/static/tools/logos/{{ tool.slug }}.png"
        alt="{{ tool.name }} official logo"
        loading="lazy"
    >
</div>'''

LOGO_CSS = '''
.tool-icon img {
    width: 44px;
    height: 44px;
    display: block;
    object-fit: contain;
    border-radius: 10px;
}
'''


def download_logo(slug, domain):
    url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/151 Safari/537.36"
            )
        },
    )

    destination = LOGO_DIR / f"{slug}.png"

    try:
        with urlopen(request, timeout=20) as response:
            data = response.read()

        if not data:
            raise RuntimeError("empty response")

        destination.write_bytes(data)
        print(f"[OK] {slug}")

    except Exception as exc:
        print(f"[ERROR] {slug}: {exc}")


def update_template(filename):
    path = TEMPLATE_DIR / filename

    if not path.exists():
        print(f"[SKIP] {filename} not found")
        return

    text = path.read_text(encoding="utf-8")
    original = text

    # Convert the old emoji block only if it still exists.
    icon_replacements = text.count(OLD_ICON_BLOCK)
    if icon_replacements:
        text = text.replace(OLD_ICON_BLOCK, NEW_ICON_BLOCK)

    # Add logo CSS once if it is not already present.
    if ".tool-icon img" not in text:
        style_close = text.find("</style>")
        if style_close != -1:
            text = text[:style_close] + LOGO_CSS + "\n" + text[style_close:]

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"[UPDATED] {filename} ({icon_replacements} icon block(s))")
    else:
        print(f"[UNCHANGED] {filename}")


def main():
    print("\nDownloading brand logos...\n")

    for slug, domain in PROVIDERS.items():
        download_logo(slug, domain)

    for filename in TEMPLATES:
        update_template(filename)

    print("\n====================================")
    print("Official logo setup completed.")
    print("====================================")


if __name__ == "__main__":
    main()