from django import forms

from shop.models import Category, Product, Order


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Price'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Brand'}),
            'cpu_socket': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPU Socket'}),
            'power_tdp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Power TDP'}),
            'ram_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ram Type'}),
            'gpu_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GPU Type'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Price'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Brand'}),
            'cpu_socket': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPU Socket'}),
            'power_tdp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Power TDP'}),
            'ram_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ram Type'}),
            'gpu_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GPU Type'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }
