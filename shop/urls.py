from django.urls import path

from shop import views

urlpatterns = [
    path('create_categories/', views.CategoryCreateView.as_view(), name='create-categories' ),
    path('list_of_categories/', views.CategoryListView.as_view(), name='list-of-categories' ),
    path('update_category/<int:pk>/', views.CategoryUpdateView.as_view(), name='update-categories'),
    path('delete_category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete-categories'),
    path('category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('create_products/', views.ProductCreateView.as_view(), name='create-products' ),
    path('list_of_products/', views.ProductListView.as_view(), name='list-of-products' ),
    path('update_products/<int:pk>/', views.ProductUpdateView.as_view(), name='update-products'),
    path('delete_products/<int:pk>/', views.ProductDeleteView.as_view(), name='delete-products'),
    path('product_details/<int:pk>/', views.ProductDetailView.as_view(), name='product-details'),
    path('product_per_category/<int:pk>/', views.get_all_products_per_category, name='product-per-category'),
    path('news/', views.news, name='news'),

]
