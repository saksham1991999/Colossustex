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

@register.filter
def inquiry_product_quotation(product, supplier):
    quotations = coremodels.supplier_quotations.objects.filter(product=product, supplier = supplier)
    return quotations

@register.filter
def quotation(quotations, supplier):
    try:
        quotation = quotations.filter(supplier=supplier)[0]
        return str(quotation.price_kg)
    except:
        return '-'

@register.filter
def lowest_price(quotations, supplier):
    try:
        prices = quotations.values_list('price_kg', flat=True)
        prices = list(prices)

        min_price = 999999999999999999
        for price in prices:
            min_price = min(min_price, price)

        quotation = quotations.filter(supplier=supplier)[0]
        price_kg = quotation.price_kg
        if price_kg == min_price:
            return True
        else:
            return False
    except:
        return False

@register.filter
def max_price(quotations, supplier):
    try:
        prices = quotations.values_list('price_kg', flat=True)
        prices = list(prices)
        max_price = 0
        for price in prices:
            max_price = max(max_price, price)
        quotation = quotations.filter(supplier=supplier)[0]
        price_kg = quotation.price_kg
        if price_kg == max_price:
            return True
        else:
            return False
    except:
        return False
