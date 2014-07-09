from django.conf import settings


def add_settings(context):
    return {'settings': settings}
