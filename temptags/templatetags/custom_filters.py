from django import template
import datetime
import os

register = template.Library()

@register.filter(name='split_ret1st')
def split_ret1st(arg,sep="."):
    return arg.split(sep)[0]

@register.filter(name='get_list')
def get_list(arg,sep=" "):
    return arg.split(sep)

@register.simple_tag
def get_current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
 