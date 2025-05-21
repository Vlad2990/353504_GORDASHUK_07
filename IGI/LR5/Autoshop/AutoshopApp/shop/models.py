from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    article = models.PositiveIntegerField(unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.PositiveIntegerField()
    providers = models.ManyToManyField('Provider', blank=False, related_name='provider_product')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.localtime)
    utc_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}: {self.price}$'
    

class Provider(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    created = models.DateTimeField(default=timezone.localtime)
    utc_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        products = self.provider_product.all()
        for product in products:
            if product.providers.count() == 1 and product.providers.first() == self:
                product.delete()
        super().delete(*args, **kwargs)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders") 
    date = models.DateTimeField(default=timezone.localtime)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} made order on {self.date}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_at_order = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.price_at_order * self.quantity

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user=models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    age=models.PositiveSmallIntegerField(null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^\+37529\d{7}$', message="Phone number must be entered in the format: '+37529XXXXXXX'")
    phone_number = models.CharField(validators=[phone_regex], max_length=13)
    bio=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user.username)
    
class Feedback(models.Model):
    username = models.CharField(max_length=20)
    text = models.TextField(max_length=256)
    rate = models.PositiveSmallIntegerField()
    date = models.DateField(default=timezone.now)
    
class Description(models.Model):
    info = models.CharField(max_length=256)
    logo = models.ImageField(
        upload_to='img',
        verbose_name='Logo',
        blank=True,
        null=True
    )
    video_url = models.URLField(
        verbose_name='Video link',
        blank=True
    )
    
class News(models.Model):
    title = models.CharField(max_length=20)
    short = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class QandA(models.Model):
    question = models.CharField(max_length=30)
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.question
    
class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Promocode(models.Model):
    description = models.CharField(max_length=20)
    valid = models.DateField(blank=False)
    
    def __str__(self):
        return f'Valid until {self.valid}'
    
    def is_valid(self):
        return self.valid > timezone.now().date()
    
class Contact(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='img')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+37529\d{7}$', message="Phone number must be entered in the format: '+37529XXXXXXX'")
    phone_number = models.CharField(validators=[phone_regex], max_length=13)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class PickPoints(models.Model):
    adress = models.CharField(max_length=20)
    start_work = models.TimeField()
    end_work = models.TimeField()
    
    def __str__(self):
        return self.adress