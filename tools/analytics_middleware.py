import uuid

from .models import VisitorLog


# =========================================================
# DEVICE / BROWSER DETECTION
# =========================================================

def detect_device(user_agent):

    ua = user_agent.lower()

    if detect_bot(user_agent):
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


# =========================================================
# BOT DETECTION
# =========================================================

def detect_bot(user_agent):

    ua = user_agent.lower()

    bot_words = [
        "bot",
        "crawler",
        "spider",
        "slurp",
        "googlebot",
        "bingbot",
        "duckduckbot",
        "yandexbot",
        "baiduspider",
        "facebookexternalhit",
        "twitterbot",
        "linkedinbot",
        "semrushbot",
        "ahrefsbot",
    ]

    return any(
        word in ua
        for word in bot_words
    )


# =========================================================
# HOSTING / HEALTH CHECK DETECTION
# =========================================================

def is_internal_probe(user_agent):

    ua = user_agent.lower()

    probe_words = [
        "render/1.0",
        "render/",
        "go-http-client",
        "kube-probe",
        "healthcheck",
        "health-check",
        "uptimerobot",
        "statuscake",
        "pingdom",
        "curl/",
        "wget/",
        "python-requests",
    ]

    return any(
        word in ua
        for word in probe_words
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
            "/media/",
            "/favicon.ico",
            "/robots.txt",
            "/sitemap.xml",
            "/health/",
            "/healthz",
            "/metrics/",

        ]

        if any(
            path.startswith(item)
            for item in ignored_paths
        ):
            return


        # =================================================
        # ONLY REAL GET PAGE REQUESTS
        # =================================================

        if request.method != "GET":
            return


        # Do not count error pages as views
        if response.status_code >= 400:
            return


        # Only count HTML pages
        content_type = response.get(
            "Content-Type",
            "",
        ).lower()

        if "text/html" not in content_type:
            return


        # =================================================
        # USER AGENT
        # =================================================

        user_agent = request.META.get(
            "HTTP_USER_AGENT",
            "",
        )


        # =================================================
        # IGNORE RENDER / HOSTING HEALTH CHECKS COMPLETELY
        # =================================================

        if is_internal_probe(user_agent):
            return


        # =================================================
        # BOT STATUS
        # =================================================

        is_bot_visit = detect_bot(
            user_agent
        )


        # =================================================
        # VISITOR SESSION
        # =================================================

        if is_bot_visit:

            analytics_id = ""

        else:

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

            is_bot=is_bot_visit,

        )