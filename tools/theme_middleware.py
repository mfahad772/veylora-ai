import re

from .models import SiteTheme


# =========================================================
# VEYLORA AI - GLOBAL THEME ENGINE
# =========================================================

DEFAULT_THEME = {
    "primary_color": "#7568ff",
    "secondary_color": "#00d4ff",
    "accent_color": "#d946ef",
    "background_color": "#0b0f19",
    "card_color": "#121827",
    "text_color": "#ffffff",
    "muted_text_color": "#9da6b8",
}

HEX_COLOR = re.compile(
    r"^#[0-9a-fA-F]{6}$"
)


# =========================================================
# HELPERS
# =========================================================

def safe_color(value, fallback):

    if (
        isinstance(value, str)
        and HEX_COLOR.fullmatch(value)
    ):
        return value.lower()

    return fallback


def rgb(color):

    color = color.lstrip("#")

    return ", ".join(
        str(
            int(
                color[i:i + 2],
                16,
            )
        )
        for i in (
            0,
            2,
            4,
        )
    )


def theme_values(theme):

    values = {

        "primary":
            safe_color(
                getattr(
                    theme,
                    "primary_color",
                    None,
                ),
                DEFAULT_THEME[
                    "primary_color"
                ],
            ),

        "secondary":
            safe_color(
                getattr(
                    theme,
                    "secondary_color",
                    None,
                ),
                DEFAULT_THEME[
                    "secondary_color"
                ],
            ),

        "accent":
            safe_color(
                getattr(
                    theme,
                    "accent_color",
                    None,
                ),
                DEFAULT_THEME[
                    "accent_color"
                ],
            ),

        "background":
            safe_color(
                getattr(
                    theme,
                    "background_color",
                    None,
                ),
                DEFAULT_THEME[
                    "background_color"
                ],
            ),

        "card":
            safe_color(
                getattr(
                    theme,
                    "card_color",
                    None,
                ),
                DEFAULT_THEME[
                    "card_color"
                ],
            ),

        "text":
            safe_color(
                getattr(
                    theme,
                    "text_color",
                    None,
                ),
                DEFAULT_THEME[
                    "text_color"
                ],
            ),

        "muted":
            safe_color(
                getattr(
                    theme,
                    "muted_text_color",
                    None,
                ),
                DEFAULT_THEME[
                    "muted_text_color"
                ],
            ),

    }


    for key in (
        "primary",
        "secondary",
        "accent",
        "background",
        "card",
    ):

        values[
            f"{key}_rgb"
        ] = rgb(
            values[key]
        )


    return values


def replace_tokens(
    text,
    values,
):

    mapping = {

        "__PRIMARY__":
            values["primary"],

        "__SECONDARY__":
            values["secondary"],

        "__ACCENT__":
            values["accent"],

        "__BACKGROUND__":
            values["background"],

        "__CARD__":
            values["card"],

        "__TEXT__":
            values["text"],

        "__MUTED__":
            values["muted"],

        "__PRIMARY_RGB__":
            values["primary_rgb"],

        "__SECONDARY_RGB__":
            values["secondary_rgb"],

        "__ACCENT_RGB__":
            values["accent_rgb"],

        "__BACKGROUND_RGB__":
            values["background_rgb"],

        "__CARD_RGB__":
            values["card_rgb"],

    }


    for (
        old,
        new,
    ) in mapping.items():

        text = text.replace(
            old,
            new,
        )


    return text


# =========================================================
# BASE THEME
# =========================================================

def build_base_css(theme):

    values = (
        theme_values(theme)
    )


    css = r"""
<style id="veylora-theme-variables">

    :root {

        --v-primary:
            __PRIMARY__;

        --v-secondary:
            __SECONDARY__;

        --v-accent:
            __ACCENT__;

        --v-bg:
            __BACKGROUND__;

        --v-card:
            __CARD__;

        --v-text:
            __TEXT__;

        --v-muted:
            __MUTED__;


        --v-primary-rgb:
            __PRIMARY_RGB__;

        --v-secondary-rgb:
            __SECONDARY_RGB__;

        --v-accent-rgb:
            __ACCENT_RGB__;

        --v-bg-rgb:
            __BACKGROUND_RGB__;

        --v-card-rgb:
            __CARD_RGB__;


        --v-gradient:

            linear-gradient(
                110deg,
                var(--v-secondary),
                var(--v-primary),
                var(--v-accent)
            );


        --v-border:

            rgba(
                var(--v-primary-rgb),
                0.26
            );


        --v-border-soft:

            rgba(
                var(--v-primary-rgb),
                0.14
            );

    }


    ::selection {

        background:
            var(--v-primary);

        color:
            #ffffff;

    }


    ::-webkit-scrollbar {

        width:
            10px;

        height:
            10px;

    }


    ::-webkit-scrollbar-track {

        background:
            var(--v-bg);

    }


    ::-webkit-scrollbar-thumb {

        background:
            var(--v-primary);

        border:
            2px solid
            var(--v-bg);

        border-radius:
            999px;

    }

</style>
"""


    return replace_tokens(
        css,
        values,
    )


# =========================================================
# PUBLIC WEBSITE THEME
# NO RUNNING / RGB LIGHTS
# =========================================================

def build_public_css(theme):

    values = (
        theme_values(theme)
    )


    css = r"""
<style id="veylora-public-theme">


    html,
    body {

        background-color:
            var(--v-bg)
            !important;

        color:
            var(--v-text)
            !important;

    }


    body {

        background-image:

            radial-gradient(
                circle at 12% 8%,
                rgba(
                    var(--v-secondary-rgb),
                    0.08
                ),
                transparent 31%
            ),

            radial-gradient(
                circle at 88% 12%,
                rgba(
                    var(--v-primary-rgb),
                    0.11
                ),
                transparent 33%
            ),

            radial-gradient(
                circle at 52% 90%,
                rgba(
                    var(--v-accent-rgb),
                    0.06
                ),
                transparent 35%
            )

            !important;

    }


    /* =====================================================
       REMOVE OLD RUNNING EFFECTS
    ===================================================== */

    #veylora-live-runner,
    .v-video-runner-track,
    .v-video-runner-light {

        display:
            none
            !important;

        animation:
            none
            !important;

    }


    .v-video-running-button {

        animation:
            none
            !important;

    }


    /* =====================================================
       HEADER
    ===================================================== */

    header {

        background:

            rgba(
                var(--v-bg-rgb),
                0.94
            )

            !important;

        border-color:
            var(--v-border-soft)
            !important;

        backdrop-filter:
            blur(16px)
            saturate(125%)
            !important;

    }


    .logo,
    .brand,
    .brand-name,
    .account-nav,
    .user-nav {

        color:
            var(--v-text)
            !important;

    }


    nav a:not(
        .account-button
    ):not(
        .account-nav
    ):not(
        .user-nav
    ) {

        color:
            var(--v-muted)
            !important;

    }


    nav a:hover {

        color:
            var(--v-text)
            !important;

    }


    .logo span,
    .gradient-text,
    .hero h1 span {

        background:
            var(--v-gradient)
            !important;

        background-clip:
            text
            !important;

        -webkit-background-clip:
            text
            !important;

        -webkit-text-fill-color:
            transparent
            !important;

        animation:
            none
            !important;

    }


    /* =====================================================
       HERO
    ===================================================== */

    .hero {

        position:
            relative
            !important;

        overflow:
            hidden
            !important;

        background:

            linear-gradient(
                135deg,

                rgba(
                    var(--v-secondary-rgb),
                    0.10
                ),

                rgba(
                    var(--v-primary-rgb),
                    0.08
                ),

                rgba(
                    var(--v-accent-rgb),
                    0.06
                )
            )

            !important;

        border-color:
            var(--v-border-soft)
            !important;

    }


    .hero::before,
    .hero::after {

        animation:
            none
            !important;

    }


    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    .hero h1,
    .hero h2,
    .section-title h2,
    .directory-heading h2,
    .page-heading h2 {

        color:
            var(--v-text)
            !important;

    }


    .hero p,
    .section-title p,
    .directory-heading p,
    .page-heading p,
    .description,
    .help-text,
    .social-note,
    .stat-desc,
    .brand-small,
    .login-info,
    .muted {

        color:
            var(--v-muted)
            !important;

    }


    .hero-badge,
    .badge,
    .tool-count,
    .category,
    .tool-category,
    .tag,
    .tag-purple,
    .tag-green,
    .tag-gray {

        color:
            var(--v-text)
            !important;

        background:

            rgba(
                var(--v-primary-rgb),
                0.09
            )

            !important;

        border-color:

            rgba(
                var(--v-primary-rgb),
                0.28
            )

            !important;

    }


    /* =====================================================
       HOME TOP 4 BUTTONS

       Explore Video Tools ab bilkul
       baqi buttons jaisa hoga.
    ===================================================== */

    .hero-buttons .hero-button,
    .hero-buttons .hero-button.secondary,
    .hero-buttons .hero-button.saved,
    .hero-buttons .hero-button.recent {

        position:
            relative
            !important;

        overflow:
            hidden
            !important;

        color:
            #ffffff
            !important;

        background:
            var(--v-gradient)
            !important;

        border:

            1px solid

            rgba(
                var(--v-primary-rgb),
                0.38
            )

            !important;

        box-shadow:

            0 10px 26px

            rgba(
                var(--v-primary-rgb),
                0.18
            )

            !important;

        animation:
            none
            !important;

        transition:

            transform
            0.22s
            ease,

            box-shadow
            0.22s
            ease,

            filter
            0.22s
            ease

            !important;

    }


    .hero-buttons .hero-button:hover,
    .hero-buttons .hero-button.secondary:hover,
    .hero-buttons .hero-button.saved:hover,
    .hero-buttons .hero-button.recent:hover {

        transform:
            translateY(-2px)
            !important;

        box-shadow:

            0 15px 34px

            rgba(
                var(--v-primary-rgb),
                0.27
            )

            !important;

        filter:
            brightness(1.05);

    }


    .hero-buttons .hero-button::before,
    .hero-buttons .hero-button::after,
    .hero-buttons .hero-button.secondary::before,
    .hero-buttons .hero-button.secondary::after,
    .hero-buttons .hero-button.saved::before,
    .hero-buttons .hero-button.saved::after,
    .hero-buttons .hero-button.recent::before,
    .hero-buttons .hero-button.recent::after {

        content:
            none
            !important;

        display:
            none
            !important;

        animation:
            none
            !important;

    }


    /* =====================================================
       CARDS
    ===================================================== */

    .category-card,
    .tool-card,
    .info-box,
    .info-card,
    .feature,
    .faq-item,
    .seo-content,
    .contact-box,
    .page-card,
    .login-card,
    .signup-card,
    .profile-card,
    .account-panel,
    .dashboard-item,
    .quick-link,
    .quick-item,
    .saved-card,
    .recent-card,
    .welcome,
    .card,
    .stat-card,
    .tool-stat,
    .preview-card,
    .filter-button,
    .table-wrap {

        background:

            linear-gradient(
                145deg,

                rgba(
                    var(--v-card-rgb),
                    0.98
                ),

                rgba(
                    var(--v-card-rgb),
                    0.91
                )
            )

            !important;

        color:
            var(--v-text)
            !important;

        border-color:
            var(--v-border-soft)
            !important;

        box-shadow:

            inset
            0 1px 0
            rgba(
                255,
                255,
                255,
                0.025
            ),

            0 12px 32px
            rgba(
                0,
                0,
                0,
                0.13
            )

            !important;

    }


    .category-card,
    .tool-card,
    .info-card,
    .feature,
    .faq-item,
    .dashboard-item,
    .quick-link,
    .saved-card,
    .recent-card {

        transform-style:
            preserve-3d;

        transition:

            transform
            0.24s
            ease,

            border-color
            0.24s
            ease,

            box-shadow
            0.24s
            ease

            !important;

    }


    .category-card:hover,
    .tool-card:hover,
    .info-card:hover,
    .feature:hover,
    .faq-item:hover,
    .dashboard-item:hover,
    .quick-link:hover,
    .saved-card:hover,
    .recent-card:hover {

        transform:

            perspective(900px)

            translateY(-5px)

            rotateX(1deg)

            !important;

        border-color:

            rgba(
                var(--v-primary-rgb),
                0.42
            )

            !important;

        box-shadow:

            0 18px 46px

            rgba(
                var(--v-primary-rgb),
                0.20
            )

            !important;

    }


    .tool-card p,
    .category-card p,
    .info-box p,
    .info-card p,
    .feature p,
    .faq-item p,
    .seo-content p,
    .contact-box p,
    .page-card p,
    .quick-text p,
    .empty,
    footer,
    footer p,
    .footer-links a,
    .info-label,
    .stat-label {

        color:
            var(--v-muted)
            !important;

    }


    /* =====================================================
       INPUTS
    ===================================================== */

    input:not(
        [type="color"]
    ),
    textarea,
    select,
    .search-box input {

        background:

            rgba(
                var(--v-card-rgb),
                0.95
            )

            !important;

        color:
            var(--v-text)
            !important;

        border-color:
            var(--v-border)
            !important;

    }


    input:not(
        [type="color"]
    ):focus,
    textarea:focus,
    select:focus,
    .search-box input:focus {

        outline:
            none
            !important;

        border-color:
            var(--v-primary)
            !important;

        box-shadow:

            0 0 0 3px

            rgba(
                var(--v-primary-rgb),
                0.13
            )

            !important;

    }


    input::placeholder,
    textarea::placeholder {

        color:
            var(--v-muted)
            !important;

        opacity:
            0.76;

    }


    /* =====================================================
       BUTTONS
       STATIC THEME ONLY
    ===================================================== */

    .category-button,
    .tool-button,
    .primary-btn,
    .open-btn,
    .explore-btn,
    .continue-button,
    .login-button,
    .signup-button,
    .save-button,
    .preview-button,
    .visit-button,
    .search-box button,
    .account-button,
    .account-btn,
    .top-button {

        position:
            relative
            !important;

        overflow:
            hidden
            !important;

        color:
            #ffffff
            !important;

        background:
            var(--v-gradient)
            !important;

        border-color:
            transparent
            !important;

        box-shadow:

            0 9px 24px

            rgba(
                var(--v-primary-rgb),
                0.18
            )

            !important;

        animation:
            none
            !important;

        transition:

            transform
            0.22s
            ease,

            box-shadow
            0.22s
            ease,

            filter
            0.22s
            ease

            !important;

    }


    .category-button:hover,
    .tool-button:hover,
    .primary-btn:hover,
    .open-btn:hover,
    .explore-btn:hover,
    .continue-button:hover,
    .login-button:hover,
    .signup-button:hover,
    .save-button:hover,
    .preview-button:hover,
    .visit-button:hover,
    .search-box button:hover,
    .account-button:hover,
    .account-btn:hover,
    .top-button:hover {

        transform:
            translateY(-2px)
            !important;

        box-shadow:

            0 14px 32px

            rgba(
                var(--v-primary-rgb),
                0.27
            )

            !important;

        filter:
            brightness(1.05);

    }


    .category-button::after,
    .tool-button::after,
    .primary-btn::after,
    .open-btn::after,
    .explore-btn::after,
    .continue-button::after,
    .login-button::after,
    .signup-button::after,
    .visit-button::after,
    .search-box button::after {

        content:
            none
            !important;

        display:
            none
            !important;

        animation:
            none
            !important;

    }


    /* =====================================================
       GOOGLE LOGIN
    ===================================================== */

    .google-button {

        background:
            #ffffff
            !important;

        color:
            #202124
            !important;

        border-color:
            #dadce0
            !important;

        box-shadow:

            0 7px 22px

            rgba(
                0,
                0,
                0,
                0.14
            )

            !important;

        animation:
            none
            !important;

    }


    .google-button:hover {

        background:
            #f8f9fa
            !important;

        color:
            #202124
            !important;

    }


    /* =====================================================
       FOOTER
    ===================================================== */

    footer {

        color:
            var(--v-muted)
            !important;

        border-color:
            var(--v-border-soft)
            !important;

        background:

            rgba(
                var(--v-bg-rgb),
                0.42
            )

            !important;

    }


    .footer-links a:hover {

        color:
            var(--v-text)
            !important;

    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media (
        max-width: 700px
    ) {

        .category-card:hover,
        .tool-card:hover,
        .dashboard-item:hover,
        .quick-link:hover,
        .saved-card:hover,
        .recent-card:hover,
        .feature:hover,
        .info-card:hover,
        .faq-item:hover {

            transform:
                translateY(-3px)
                !important;

        }

    }

</style>
"""


    return replace_tokens(
        css,
        values,
    )


# =========================================================
# CONTROL PANEL
# CLEAN 3D THEME CARDS
# NO RUNNING BARS
# =========================================================

CONTROL_PANEL_THEME_UI = r"""
<style id="veylora-theme-picker-css">


    .v-theme-picker-title {

        margin:
            22px 0 6px;

        color:
            var(--v-text);

        font-size:
            18px;

        font-weight:
            800;

    }


    .v-theme-picker-help {

        margin-bottom:
            18px;

        color:
            var(--v-muted);

        font-size:
            13px;

        line-height:
            1.6;

    }


    .v-theme-picker-grid {

        display:
            grid;

        grid-template-columns:

            repeat(
                auto-fit,
                minmax(
                    190px,
                    1fr
                )
            );

        gap:
            18px;

        margin-bottom:
            26px;

        perspective:
            1100px;

    }


    .v-theme-picker-card {

        --tp-primary:
            #7568ff;

        --tp-secondary:
            #00d4ff;

        --tp-accent:
            #d946ef;

        --tp-bg:
            #070b14;

        --tp-card:
            #101725;

        --tp-text:
            #ffffff;

        --tp-muted:
            #8f9caf;


        position:
            relative;

        min-height:
            160px;

        padding:
            18px;

        overflow:
            hidden;

        cursor:
            pointer;

        user-select:
            none;

        border-radius:
            20px;

        border:
            1px solid
            rgba(
                255,
                255,
                255,
                0.10
            );

        color:
            var(--tp-text);

        background:

            radial-gradient(
                circle at 84% 14%,

                color-mix(
                    in srgb,
                    var(--tp-primary)
                    24%,
                    transparent
                ),

                transparent 40%
            ),

            linear-gradient(
                145deg,
                var(--tp-bg),
                var(--tp-card)
            );

        box-shadow:

            inset
            0 1px 0
            rgba(
                255,
                255,
                255,
                0.04
            ),

            0 18px 42px
            rgba(
                0,
                0,
                0,
                0.28
            );

        transform-style:
            preserve-3d;

        transition:

            transform
            0.25s
            ease,

            border-color
            0.25s
            ease,

            box-shadow
            0.25s
            ease;

    }


    .v-theme-picker-card:hover {

        transform:

            perspective(900px)

            rotateX(4deg)

            rotateY(-4deg)

            translateY(-7px);

        border-color:
            var(--tp-primary);

        box-shadow:

            0 0 0 1px

            color-mix(
                in srgb,
                var(--tp-primary)
                38%,
                transparent
            ),

            0 24px 55px
            rgba(
                0,
                0,
                0,
                0.38
            );

    }


    .v-theme-picker-card.active {

        border:
            2px solid
            var(--tp-primary);

        box-shadow:

            0 0 0 4px

            color-mix(
                in srgb,
                var(--tp-primary)
                17%,
                transparent
            ),

            0 18px 48px
            rgba(
                0,
                0,
                0,
                0.34
            );

    }


    .v-theme-picker-name {

        position:
            relative;

        z-index:
            3;

        margin-bottom:
            16px;

        color:
            var(--tp-text);

        font-size:
            16px;

        font-weight:
            800;

    }


    /* STATIC COLOR PREVIEW */

    .v-theme-preview {

        position:
            relative;

        z-index:
            3;

        display:
            grid;

        grid-template-columns:
            repeat(
                3,
                1fr
            );

        gap:
            8px;

        margin:
            16px 0 14px;

    }


    .v-theme-preview span {

        height:
            28px;

        border-radius:
            9px;

        box-shadow:

            inset
            0 1px 0
            rgba(
                255,
                255,
                255,
                0.14
            ),

            0 5px 14px
            rgba(
                0,
                0,
                0,
                0.16
            );

    }


    .v-theme-preview span:nth-child(1) {

        background:
            var(--tp-secondary);

    }


    .v-theme-preview span:nth-child(2) {

        background:
            var(--tp-primary);

    }


    .v-theme-preview span:nth-child(3) {

        background:
            var(--tp-accent);

    }


    .v-theme-picker-note {

        position:
            relative;

        z-index:
            3;

        margin-top:
            13px;

        color:
            var(--tp-muted);

        font-size:
            11px;

    }


    .v-theme-picker-badge {

        position:
            absolute;

        z-index:
            5;

        top:
            11px;

        right:
            11px;

        padding:
            5px 9px;

        border-radius:
            999px;

        background:
            var(--tp-primary);

        color:
            #ffffff;

        font-size:
            10px;

        font-weight:
            800;

        letter-spacing:
            0.6px;

        text-transform:
            uppercase;

    }


    .v-theme-picker-card.applying {

        opacity:
            0.62;

        pointer-events:
            none;

    }


    @media (
        max-width: 650px
    ) {

        .v-theme-picker-grid {

            grid-template-columns:
                1fr;

        }

    }

</style>


<script id="veylora-theme-picker-js">

(function () {


    function initVeyloraThemePicker() {


        const select =
            document.getElementById(
                "themePreset"
            );


        if (
            !select
            ||
            select.dataset
                .veyloraPickerReady
                === "1"
        ) {

            return;

        }


        const form =
            select.closest(
                "form"
            );


        const field =
            select.closest(
                ".field"
            );


        if (
            !form
            ||
            !field
        ) {

            return;

        }


        select.dataset
            .veyloraPickerReady =
            "1";


        const themes = [


            {

                key:
                    "midnight",

                name:
                    "Midnight Purple",

                primary:
                    "#7568ff",

                secondary:
                    "#00d4ff",

                accent:
                    "#d946ef",

                bg:
                    "#070b14",

                card:
                    "#101725",

                text:
                    "#ffffff",

                muted:
                    "#8f9caf"

            },


            {

                key:
                    "ocean",

                name:
                    "Ocean Blue",

                primary:
                    "#0ea5e9",

                secondary:
                    "#22d3ee",

                accent:
                    "#6366f1",

                bg:
                    "#06111d",

                card:
                    "#0c1b2a",

                text:
                    "#ffffff",

                muted:
                    "#94a9bb"

            },


            {

                key:
                    "emerald",

                name:
                    "Emerald Green",

                primary:
                    "#10b981",

                secondary:
                    "#22c55e",

                accent:
                    "#06b6d4",

                bg:
                    "#06140f",

                card:
                    "#0c2119",

                text:
                    "#ffffff",

                muted:
                    "#9ab9ac"

            },


            {

                key:
                    "sunset",

                name:
                    "Sunset Orange",

                primary:
                    "#f97316",

                secondary:
                    "#f59e0b",

                accent:
                    "#ef4444",

                bg:
                    "#160d08",

                card:
                    "#24150d",

                text:
                    "#ffffff",

                muted:
                    "#c2a89a"

            },


            {

                key:
                    "rose",

                name:
                    "Rose Pink",

                primary:
                    "#e11d48",

                secondary:
                    "#f43f5e",

                accent:
                    "#a855f7",

                bg:
                    "#16090f",

                card:
                    "#25101a",

                text:
                    "#ffffff",

                muted:
                    "#c4a1ae"

            },


            {

                key:
                    "light",

                name:
                    "Clean Light",

                primary:
                    "#4f46e5",

                secondary:
                    "#0284c7",

                accent:
                    "#9333ea",

                bg:
                    "#f5f7fb",

                card:
                    "#ffffff",

                text:
                    "#111827",

                muted:
                    "#64748b"

            },


            {

                key:
                    "custom",

                name:
                    "Custom Theme",

                primary:
                    "#7568ff",

                secondary:
                    "#00d4ff",

                accent:
                    "#d946ef",

                bg:
                    "#0b0f19",

                card:
                    "#121827",

                text:
                    "#ffffff",

                muted:
                    "#9da6b8"

            }


        ];


        const title =
            document.createElement(
                "div"
            );


        title.className =
            "v-theme-picker-title";


        title.textContent =
            "3D One-Click Website Themes";


        const help =
            document.createElement(
                "div"
            );


        help.className =
            "v-theme-picker-help";


        help.textContent =

            "Click a theme card to apply it across Veylora AI. "
            +
            "Running and RGB light bars have been removed.";


        const grid =
            document.createElement(
                "div"
            );


        grid.className =
            "v-theme-picker-grid";


        themes.forEach(

            function (
                theme
            ) {


                const card =
                    document.createElement(
                        "div"
                    );


                card.className =
                    "v-theme-picker-card";


                card.tabIndex =
                    0;


                card.setAttribute(
                    "role",
                    "button"
                );


                card.setAttribute(

                    "aria-label",

                    "Apply "
                    +
                    theme.name

                );


                card.style.setProperty(
                    "--tp-primary",
                    theme.primary
                );


                card.style.setProperty(
                    "--tp-secondary",
                    theme.secondary
                );


                card.style.setProperty(
                    "--tp-accent",
                    theme.accent
                );


                card.style.setProperty(
                    "--tp-bg",
                    theme.bg
                );


                card.style.setProperty(
                    "--tp-card",
                    theme.card
                );


                card.style.setProperty(
                    "--tp-text",
                    theme.text
                );


                card.style.setProperty(
                    "--tp-muted",
                    theme.muted
                );


                card.innerHTML =

                    '<div class="v-theme-picker-name">'
                    +
                    theme.name
                    +
                    '</div>'

                    +

                    '<div class="v-theme-preview">'
                    +
                    '<span></span>'
                    +
                    '<span></span>'
                    +
                    '<span></span>'
                    +
                    '</div>'

                    +

                    '<div class="v-theme-picker-note">'
                    +

                    (
                        theme.key
                        === "custom"

                        ?

                        "Use the custom color controls below"

                        :

                        "Click to apply to the complete website"
                    )

                    +

                    '</div>';


                if (
                    select.value
                    === theme.key
                ) {


                    card.classList.add(
                        "active"
                    );


                    const badge =
                        document.createElement(
                            "span"
                        );


                    badge.className =
                        "v-theme-picker-badge";


                    badge.textContent =
                        "Active";


                    card.appendChild(
                        badge
                    );

                }


                function applyTheme() {


                    select.value =
                        theme.key;


                    card.classList.add(
                        "applying"
                    );


                    const oldBadge =
                        card.querySelector(
                            ".v-theme-picker-badge"
                        );


                    if (
                        oldBadge
                    ) {

                        oldBadge.remove();

                    }


                    const badge =
                        document.createElement(
                            "span"
                        );


                    badge.className =
                        "v-theme-picker-badge";


                    badge.textContent =
                        "Applying";


                    card.appendChild(
                        badge
                    );


                    setTimeout(

                        function () {


                            if (
                                typeof form.requestSubmit
                                === "function"
                            ) {

                                form.requestSubmit();

                            }

                            else {

                                form.submit();

                            }

                        },

                        140

                    );

                }


                card.addEventListener(
                    "click",
                    applyTheme
                );


                card.addEventListener(

                    "keydown",

                    function (
                        event
                    ) {


                        if (
                            event.key
                            === "Enter"
                            ||
                            event.key
                            === " "
                        ) {

                            event.preventDefault();

                            applyTheme();

                        }

                    }

                );


                grid.appendChild(
                    card
                );

            }

        );


        field.style.display =
            "none";


        field.parentNode.insertBefore(
            title,
            field
        );


        field.parentNode.insertBefore(
            help,
            field
        );


        field.parentNode.insertBefore(
            grid,
            field
        );

    }


    if (
        document.readyState
        === "loading"
    ) {

        document.addEventListener(

            "DOMContentLoaded",

            initVeyloraThemePicker

        );

    }

    else {

        initVeyloraThemePicker();

    }


})();

</script>
"""


# =========================================================
# REMOVE OLD RUNNER ELEMENTS
# =========================================================

PUBLIC_CLEANUP_JS = r"""
<script id="veylora-theme-cleanup-js">

(function () {


    function cleanupOldEffects() {


        document
            .querySelectorAll(

                '#veylora-live-runner,'
                +
                '.v-video-runner-track,'
                +
                '.v-video-runner-light'

            )
            .forEach(

                function (
                    element
                ) {

                    element.remove();

                }

            );


        document
            .querySelectorAll(
                '.v-video-running-button'
            )
            .forEach(

                function (
                    element
                ) {


                    element.classList.remove(
                        'v-video-running-button'
                    );


                    if (
                        typeof
                        element.getAnimations
                        === 'function'
                    ) {


                        element
                            .getAnimations()
                            .forEach(

                                function (
                                    animation
                                ) {

                                    animation.cancel();

                                }

                            );

                    }

                }

            );

    }


    if (
        document.readyState
        === 'loading'
    ) {


        document.addEventListener(

            'DOMContentLoaded',

            cleanupOldEffects

        );

    }

    else {

        cleanupOldEffects();

    }


})();

</script>
"""


# =========================================================
# HTML INJECTION
# =========================================================

def inject_before_head_close(
    html,
    assets,
):

    return re.sub(

        r"</head\s*>",

        assets
        +
        "\n</head>",

        html,

        count=1,

        flags=re.IGNORECASE,

    )


def inject_before_body_close(
    html,
    assets,
):

    return re.sub(

        r"</body\s*>",

        assets
        +
        "\n</body>",

        html,

        count=1,

        flags=re.IGNORECASE,

    )


# =========================================================
# MIDDLEWARE
# =========================================================

class ThemeMiddleware:


    def __init__(
        self,
        get_response,
    ):

        self.get_response = (
            get_response
        )


    def __call__(
        self,
        request,
    ):


        response = (
            self.get_response(
                request
            )
        )


        if getattr(
            response,
            "streaming",
            False,
        ):

            return response


        content_type = (
            response.get(
                "Content-Type",
                "",
            )
        )


        if (
            "text/html"
            not in
            content_type.lower()
        ):

            return response


        # Django default admin unchanged

        if request.path.startswith(
            "/admin/"
        ):

            return response


        try:

            theme = (
                SiteTheme
                .get_active_theme()
            )

        except Exception:

            return response


        try:

            charset = (
                response.charset
                or "utf-8"
            )


            html = (
                response.content
                .decode(
                    charset
                )
            )

        except Exception:

            return response


        # Prevent duplicate injection

        if (
            'id="veylora-theme-variables"'
            in html
        ):

            return response


        is_control_panel = (
            request.path.startswith(
                "/control-panel/"
            )
        )


        assets = (
            build_base_css(
                theme
            )
        )


        if is_control_panel:


            assets += (
                CONTROL_PANEL_THEME_UI
            )


            themed_html = (
                inject_before_head_close(

                    html,

                    assets,

                )
            )


        else:


            assets += (
                build_public_css(
                    theme
                )
            )


            themed_html = (
                inject_before_head_close(

                    html,

                    assets,

                )
            )


            themed_html = (
                inject_before_body_close(

                    themed_html,

                    PUBLIC_CLEANUP_JS,

                )
            )


        if (
            themed_html
            == html
        ):

            return response


        response.content = (
            themed_html.encode(
                charset
            )
        )


        if response.has_header(
            "Content-Length"
        ):

            del response[
                "Content-Length"
            ]


        if response.has_header(
            "ETag"
        ):

            del response[
                "ETag"
            ]


        return response