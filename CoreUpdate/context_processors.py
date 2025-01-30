from shop.models import Category, Product


def get_all_categories(request):
    return {'categories': Category.objects.all()}

def get_all_products(request):
    return {'products': Product.objects.all()}