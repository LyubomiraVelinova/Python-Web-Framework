from django import template

register = template.Library()


@register.filter
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token

    return value


# Adding custom class
# @register.filter
# def form_field_class(form_field, className):
#     form_field.field.widget.attrs['class'] = className
#
#     return form_field
