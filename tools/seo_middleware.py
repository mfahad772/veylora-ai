import json
import re
from html import escape


BASE_URL = "https://veyloraai.online"


STATIC_SEO = {

    "/": {
        "title": "Best AI Image & Video Tools Directory | Veylora AI",
        "description": (
            "Discover powerful AI image generators, video generators, "
            "editors, animation tools and creative AI platforms on Veylora AI."
        ),
        "type": "WebSite",
    },

    "/ai-image-tools/": {
        "title": "Best AI Image Tools & Generators | Veylora AI",
        "description": (
            "Explore AI image generators, editors, background removers, "
            "image enhancers and creative AI image tools on Veylora AI."
        ),
        "type": "CollectionPage",
    },

    "/ai-video-tools/": {
        "title": "Best AI Video Tools & Generators | Veylora AI",
        "description": (
            "Discover AI video generators, image-to-video tools, AI avatars, "
            "animation platforms and video editing tools on Veylora AI."
        ),
        "type": "CollectionPage",
    },

    "/about/": {
        "title": "About Veylora AI | AI Tools Directory",
        "description": (
            "Learn about Veylora AI, an independent directory for discovering "
            "AI image, video and creative tools."
        ),
        "type": "WebPage",
    },

    "/privacy/": {
        "title": "Privacy Policy | Veylora AI",
        "description": (
            "Read the Veylora AI privacy policy and learn how information "
            "and website usage are handled."
        ),
        "type": "WebPage",
    },

    "/terms/": {
        "title": "Terms of Service | Veylora AI",
        "description": (
            "Read the terms and conditions for using the Veylora AI "
            "AI tools directory."
        ),
        "type": "WebPage",
    },

    "/disclaimer/": {
        "title": "Disclaimer | Veylora AI",
        "description": (
            "Read the Veylora AI disclaimer regarding third-party AI tools, "
            "platform information and external websites."
        ),
        "type": "WebPage",
    },

    "/contact/": {
        "title": "Contact Veylora AI | AI Tools Directory",
        "description": (
            "Contact Veylora AI for questions, suggestions and information "
            "about the AI tools directory."
        ),
        "type": "ContactPage",
    },
}


NOINDEX_PATHS = (
    "/admin/",
    "/accounts/",
    "/login/",
    "/signup/",
    "/logout/",
    "/profile/",
    "/welcome/",
)


def clean_description(text):

    text = " ".join(
        str(text).split()
    )

    if len(text) <= 160:
        return text

    return text[:157].rstrip() + "..."


def get_seo_data(path):

    if path in STATIC_SEO:
        return STATIC_SEO[path]

    if path.startswith("/tool/"):

        parts = path.strip("/").split("/")

        if len(parts) == 2:

            slug = parts[1]

            try:
                from tools.views import TOOLS

                tool = TOOLS.get(slug)

            except Exception:
                tool = None

            if tool:

                name = tool.get(
                    "name",
                    "AI Tool"
                )

                category = tool.get(
                    "category",
                    "AI Tool"
                )

                description = tool.get(
                    "description",
                    ""
                )

                return {
                    "title":
                        f"{name} - {category} | Veylora AI",

                    "description":
                        clean_description(
                            f"{description} Explore {name} details "
                            f"and visit its official website on Veylora AI."
                        ),

                    "type":
                        "WebPage",
                }

    return None


def remove_existing_seo(markup):

    patterns = [

        r'<meta\b[^>]*\bname=["\']description["\'][^>]*>\s*',

        r'<meta\b[^>]*\bname=["\']robots["\'][^>]*>\s*',

        r'<link\b[^>]*\brel=["\']canonical["\'][^>]*>\s*',

        r'<meta\b[^>]*\bproperty=["\']og:[^"\']+["\'][^>]*>\s*',

        r'<meta\b[^>]*\bname=["\']twitter:[^"\']+["\'][^>]*>\s*',

    ]

    for pattern in patterns:

        markup = re.sub(
            pattern,
            "",
            markup,
            flags=re.IGNORECASE,
        )

    return markup


class SEOMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(
            request
        )

        if getattr(
            response,
            "streaming",
            False
        ):
            return response

        content_type = response.get(
            "Content-Type",
            ""
        )

        if (
            response.status_code != 200
            or "text/html" not in content_type
        ):
            return response

        path = request.path

        try:

            charset = (
                response.charset
                or "utf-8"
            )

            markup = response.content.decode(
                charset
            )

        except Exception:

            return response


        # =====================================================
        # PRIVATE / AUTH PAGES - DON'T INDEX
        # =====================================================

        if path.startswith(
            NOINDEX_PATHS
        ):

            markup = re.sub(
                r'<meta\b[^>]*\bname=["\']robots["\'][^>]*>\s*',
                "",
                markup,
                flags=re.IGNORECASE,
            )

            noindex_tag = """
    <meta name="robots" content="noindex, nofollow">
"""

            markup = markup.replace(
                "</head>",
                noindex_tag + "\n</head>",
                1,
            )

            response.content = markup.encode(
                charset
            )

            if response.has_header(
                "Content-Length"
            ):

                response[
                    "Content-Length"
                ] = str(
                    len(response.content)
                )

            return response


        # =====================================================
        # PUBLIC SEO
        # =====================================================

        seo = get_seo_data(
            path
        )

        if not seo:
            return response


        title = seo["title"]

        description = clean_description(
            seo["description"]
        )

        canonical = (
            BASE_URL + path
        )


        # Replace existing title

        new_title = (
            f"<title>{escape(title)}</title>"
        )

        if re.search(
            r"<title\b[^>]*>.*?</title>",
            markup,
            flags=(
                re.IGNORECASE
                | re.DOTALL
            ),
        ):

            markup = re.sub(
                r"<title\b[^>]*>.*?</title>",
                new_title,
                markup,
                count=1,
                flags=(
                    re.IGNORECASE
                    | re.DOTALL
                ),
            )

        else:

            markup = markup.replace(
                "</head>",
                new_title + "\n</head>",
                1,
            )


        markup = remove_existing_seo(
            markup
        )


        # =====================================================
        # STRUCTURED DATA
        # =====================================================

        schema = {

            "@context":
                "https://schema.org",

            "@type":
                seo["type"],

            "name":
                title,

            "url":
                canonical,

            "description":
                description,

            "isPartOf": {

                "@type":
                    "WebSite",

                "name":
                    "Veylora AI",

                "url":
                    BASE_URL + "/",
            },
        }


        schema_json = json.dumps(
            schema,
            ensure_ascii=False,
            separators=(",", ":"),
        ).replace(
            "</",
            "<\\/"
        )


        seo_tags = f"""
    <!-- VEYLORA AI SEO -->
    <meta name="description" content="{escape(description)}">

    <meta name="robots"
          content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

    <link rel="canonical"
          href="{escape(canonical)}">

    <meta property="og:site_name"
          content="Veylora AI">

    <meta property="og:type"
          content="website">

    <meta property="og:title"
          content="{escape(title)}">

    <meta property="og:description"
          content="{escape(description)}">

    <meta property="og:url"
          content="{escape(canonical)}">

    <meta name="twitter:card"
          content="summary">

    <meta name="twitter:title"
          content="{escape(title)}">

    <meta name="twitter:description"
          content="{escape(description)}">

    <script type="application/ld+json">
    {schema_json}
    </script>
"""


        markup = markup.replace(
            "</head>",
            seo_tags + "\n</head>",
            1,
        )


        response.content = markup.encode(
            charset
        )


        if response.has_header(
            "Content-Length"
        ):

            response[
                "Content-Length"
            ] = str(
                len(response.content)
            )


        return response