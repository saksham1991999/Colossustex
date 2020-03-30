from django import template
from core import models as coremodels
from employee import models as employeemodels

register = template.Library()


@register.filter
def profileimage(user):
    if user.is_employee:
        try:
            image = employeemodels.employee.objects.get(user=user).image.url

            return image
        except:
            pass
    return ' '

