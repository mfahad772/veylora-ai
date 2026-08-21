from .models import SiteTheme


def site_theme(request):
    """
    Provides the active Veylora AI website theme
    to every Django template.
    """

    try:
        theme = SiteTheme.get_active_theme()

    except Exception:
        theme = None

    return {
        "site_theme": theme,
    }