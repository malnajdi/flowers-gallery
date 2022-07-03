from django.conf import settings


def get_login_logout_urls(request):
    return {
        "LOGIN_URL": settings.LOGIN_URL,
        "LOGOUT_URL": settings.LOGOUT_URL
    }