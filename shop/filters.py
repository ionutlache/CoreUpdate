import django_filters
from django import forms
from .models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    price = django_filters.CharFilter(lookup_expr='icontains',label='Price',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}))
    brand = django_filters.CharFilter(lookup_expr='icontains',label='Brand',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}))
    cpu_socket = django_filters.CharFilter(lookup_expr='icontains',label='CPU Socket',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPU Socket'}))
    ram_type = django_filters.CharFilter(lookup_expr='icontains',label='RAM Type',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RAM Type'}))
    gpu_type = django_filters.CharFilter(lookup_expr='icontains',label='GPU Type',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GPU Type'}))
    power_tdp = django_filters.CharFilter(lookup_expr='icontains',label='Power TDP',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Power TDP'}))
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'brand', 'cpu_socket', 'power_tdp', 'ram_type', 'gpu_type']
