from django.template.defaulttags import register
from datetime import datetime, timezone


@register.simple_tag
def remainedtime(mytime):
    return mytime - datetime.now(timezone.utc)

@register.filter
def capitalize(title):
    return title.title()
