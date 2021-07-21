import datetime

from django import template

from src.admin_panel.services.user_passes_test import check_access

register = template.Library()


@register.filter(name="get_int")
def get_int(value):
    """Removes all values of arg from the given string"""
    return value.split("-")[1]


@register.filter(name="cool_phone_number")
def cool_phone_number(value):
    value = str(value)
    return f"{value[0:3]} ({value[3:6]}) {value[6:9]}-{value[9:11]}-{value[11:13]}"


@register.filter(name="get_id")
def get_id(value):
    try:
        result = str(value).split("-")[1]
    except IndexError:
        result = value
    return result


@register.filter(name="get_unique_houses")
def get_unique_houses(value):
    return value.distinct("house")


@register.filter(name="test")
def test(value):
    return value


@register.filter(name="check_access")
def check_user_access(user, variable):
    return check_access(user, variable)


@register.filter(name="decimalFormat")
def decimal_format(value):
    return "{:,}".format(value)
