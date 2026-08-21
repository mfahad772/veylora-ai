import uuid

from .models import VisitorLog


# =========================================================
# DEVICE / BROWSER DETECTION
# =========================================================

def detect_device(user_agent):

    ua = user_agent.lower()

    if any(
        word in ua
        for word in [
            "bot",
            "crawler",
            "spider",
            "slurp",
        ]
    ):
        return "Bot"

    if any(
        word in ua
        for word in [
            "iphone",
            "android",
            "mobile",
        ]
    ):
        return "Mobile"

    if any(
        word in ua
        for word in [
            "ipad",
            "tablet",
        ]
    ):
        return "Tablet"

    return "Desktop"


def detect_browser(user_agent):

    ua = user_agent.lower()

    if "edg/" in ua:
        return "Microsoft Edge"

    if "chrome/" in ua:
        return "Google Chrome"

    if "firefox/" in ua:
        return "Firefox"

    if "safari/" in ua:
        return "Safari"

    if "opera" in ua or "opr/" in ua:
        return "Opera"

    return "Other"


def detect_os(user_agent):

    ua = user_agent.lower()

    if "windows" in ua:
        return "Windows"

    if "android" in ua:
        return "Android"

    if "iphone" in ua or "ipad" in ua:
        return "iOS"

    if "mac os" in ua or "macintosh" in ua:
        return "macOS"

    if "linux" in ua:
        return "Linux"

    return "Other"


def detect_bot(user_agent):

    ua = user_agent.lower()

    bot_words = [
        "bot",
        "crawler",
        "spider",
        "slurp",
        "googlebot",
        "bingbot",
    ]

    return any(
        word in ua
        for word in bot_words
    )


# =========================================================
# IP ADDRESS
# =========================================================

def get_client_ip(request):

    forwarded_for = request.META.get(
        "HTTP_X_FORWARDED_FOR"
    )

    if forwarded_for:

        return forwarded_for.split(",")[0].strip()

    return request.META.get(
        "REMOTE_ADDR"
    )


# =========================================================
# ANALYTICS MIDDLEWARE
# =========================================================

class AnalyticsMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(
            request
        )

        try:

            self.save_visit(
                request,
                response,
            )

        except Exception:

            pass

        return response


    def save_visit(
        self,
        request,
        response,
    ):

        path = request.path


        # =================================================
        # DO NOT TRACK ADMIN / INTERNAL REQUESTS
        # =================================================

        ignored_paths = [

            "/admin/",
            "/control-panel/",
            "/static/",
            "/favicon.ico",
            "/robots.txt",
            "/sitemap.xml",

        ]

        if any(
            path.startswith(item)
            for item in ignored_paths
        ):
            return


        # Only normal GET page visits
        if request.method != "GET":
            return


        user_agent = request.META.get(
            "HTTP_USER_AGENT",
            "",
        )


        # =================================================
        # VISITOR SESSION
        # =================================================

        analytics_id = request.session.get(
            "analytics_id"
        )

        if not analytics_id:

            analytics_id = uuid.uuid4().hex

            request.session[
                "analytics_id"
            ] = analytics_id


        # =================================================
        # USER
        # =================================================

        user = None

        is_authenticated = False

        if request.user.is_authenticated:

            user = request.user

            is_authenticated = True


        # =================================================
        # SAVE VISIT
        # =================================================

        VisitorLog.objects.create(

            user=user,

            session_key=analytics_id,

            ip_address=get_client_ip(
                request
            ),

            path=path,

            request_method=request.method,

            response_status=(
                response.status_code
            ),

            referrer=request.META.get(
                "HTTP_REFERER",
                "",
            ),

            user_agent=user_agent,

            device_type=detect_device(
                user_agent
            ),

            browser=detect_browser(
                user_agent
            ),

            operating_system=detect_os(
                user_agent
            ),

            is_authenticated_visit=(
                is_authenticated
            ),

            is_bot=detect_bot(
                user_agent
            ),

        )