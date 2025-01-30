import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save





class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='uploads/categories')
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
    brand = models.CharField(max_length=20)
    cpu_socket = models.CharField(max_length=8, null=True, blank=True)
    power_tdp = models.CharField(max_length=6, null=True, blank=True)
    ram_type = models.CharField(max_length=6, null=True, blank=True)
    gpu_type = models.CharField(max_length=6, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products')

    def __str__(self):
        return f"{self.name} ({self.brand})"


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        ORDERED = 'ordered', 'Ordered'
        DELIVERING = 'delivering', 'Delivering'
        DELIVERED = 'delivered', 'Delivered'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_index=True)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.ORDERED,
    )

    def __str__(self):
        return f"Order #{self.id}: {self.product.name} for {self.customer.first_name} {self.customer.last_name} - {self.get_status_display()}"


class OrderNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    sent_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        date_display = self.sent_date.strftime("%Y-%m-%d %H:%M:%S")
        return f"Notification for Order #{self.order.id} - Sent: {date_display}"