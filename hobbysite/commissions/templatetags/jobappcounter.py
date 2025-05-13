from django import template
"""
Guide on custom tags from
https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/#simple-tags
"""

register = template.Library()


@register.simple_tag(name="get_open_slots_count")
def get_open_slots_count(max_manpower, job_apps, status_to_check):
    """
    A custom tag to do all the math and QuerySearches
    that are otherwise unavailable in templates.
    This is to get the difference between max manpower
    and number of applications already accepted

    By default, it outputs the remaining slots
    """
    slots_filled = len(job_apps.all().filter(status=status_to_check))
    return max_manpower - slots_filled
