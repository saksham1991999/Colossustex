from django import template
from core import models as coremodels
from employee import models as employeemodels

register = template.Library()


@register.filter
def product_supplier_quotations(product, supplier):
    quotations = coremodels.supplier_quotations.objects.filter(product = product, supplier = supplier).order_by('price_kg')
    return quotations

@register.filter
def lowest_quotation(quotation):
    lowestprice = quotation.price_kg
    other_quptations = coremodels.supplier_quotations.objects.filter(product=quotation.product)
    for other_quotation in other_quptations:
        lowestprice = min(lowestprice, other_quotation.price_kg)
    if lowestprice == quotation.price_kg:
        return True
    else:
        return False




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
def product_forwarded_quotations(product):
    quotations = coremodels.forwarded_quotation.objects.get(inquiry = product.inquiry).quotations.all()
    product_quotations = quotations.filter(product = product)
    return product_quotations

# @register.filter
# def inquiry_product_quotation(product, supplier):
#     quotations = coremodels.supplier_quotations.objects.filter(product=product, supplier = supplier)
#     return quotations
#
# @register.filter
# def quotation(quotations, supplier):
#     try:
#         quotation = quotations.filter(supplier=supplier)[0]
#         return str(quotation.price_kg)
#     except:
#         return '-'




# @register.filter
# def lowest_price(quotations, supplier):
#     try:
#         prices = quotations.values_list('price_kg', flat=True)
#         prices = list(prices)
#
#         min_price = 999999999999999999
#         for price in prices:
#             min_price = min(min_price, price)
#
#         quotation = quotations.filter(supplier=supplier)[0]
#         price_kg = quotation.price_kg
#         if price_kg == min_price:
#             return True
#         else:
#             return False
#     except:
#         return False
#
# @register.filter
# def max_price(quotations, supplier):
#     try:
#         prices = quotations.values_list('price_kg', flat=True)
#         prices = list(prices)
#         max_price = 0
#         for price in prices:
#             max_price = max(max_price, price)
#         quotation = quotations.filter(supplier=supplier)[0]
#         price_kg = quotation.price_kg
#         if price_kg == max_price:
#             return True
#         else:
#             return False
#     except:
#         return False
