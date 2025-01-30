from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from shop.filters import ProductFilter
from shop.forms import CategoryForm, CategoryUpdateForm, ProductForm, ProductUpdateForm, OrderCreateForm
from shop.models import Category, Product, Order
import datetime



class CategoryCreateView(PermissionRequiredMixin, LoginRequiredMixin,CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = '/'
    permission_required = 'category.add_category'


class CategoryListView(ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'


class CategoryDetailView(DetailView):
    template_name = 'category/details_category.html'
    model = Category



    # def get_context_data(self, **kwargs):
    #     data=super().get_context_data(**kwargs)
    #
    #     trainers = Trainer.objects.filter(active=True)
    #     filters = TrainerFilter(self.request.GET,queryset=trainers)
    #     data['all_trainers']=filters.qs
    #     data['filters_form'] = filters.form
    #     return data

class CategoryUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    template_name = 'category/update_category.html'
    model= Category
    form_class = CategoryUpdateForm
    success_url='/'
    permission_required = 'category.change_category'

class CategoryDeleteView(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = '/'
    permission_required = 'category.delete_category'

# class TrainerDetailView(LoginRequiredMixin,DetailView):
#     template_name = 'trainer/details_trainer.html'
#     model = Trainer

# def get_all_students_per_trainer(request,pk):
#     get_students= Student.objects.filter(trainer_id=pk)   #Interogam baza tabela student sa ne aduca toti studentii alocati trainerului
#     return render(request, 'trainer/students_per_trainer.html', {
#         'get_all_students':get_students})

class ProductCreateView(PermissionRequiredMixin, LoginRequiredMixin,CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/'
    permission_required = 'product.add_product'

class ProductListView(ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)

        filters=ProductFilter(self.request.GET)
        data['all_products'] = filters.qs
        data['filters_form'] = filters.form
        return data

    # def get_context_data(self, **kwargs):
    #     data=super().get_context_data(**kwargs)
    #
    #     trainers = Trainer.objects.filter(active=True)
    #     filters = TrainerFilter(self.request.GET,queryset=trainers)
    #     data['all_trainers']=filters.qs
    #     data['filters_form'] = filters.form
    #     return data

class ProductUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    template_name = 'product/update_product.html'
    model= Product
    form_class = ProductUpdateForm
    success_url='/'
    permission_required='product.change_product'

class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin,DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = '/'
    permission_required = 'product.delete_product'

class ProductDetailView(DetailView):
    template_name = 'product/details_product.html'
    model = Product

def home(request):
    products=Product.objects.all()
    return render(request, 'home/homepage.html',{'products':products})

def get_all_products_per_category(request,pk):
    get_products= Product.objects.filter(category_id=pk)

    return render(request, 'category/product_per_category.html', {
        'get_all_products':get_products})

class OrderCreateView(LoginRequiredMixin,CreateView):
    template_name = 'cart/checkout.html'
    model = Order
    form_class = OrderCreateForm
    success_url = '/'

def news(request):
    return render(request, 'news/news_template.html')