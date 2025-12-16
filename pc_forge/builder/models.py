from django.db import models
from django.contrib.auth.models import User

# 1. CATEGORY (e.g., "CPU", "Motherboard")
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. PRODUCT (The Inventory)
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # Economic Data
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    # Engineering Specs (Nullable because not all parts have them)
    socket_type = models.CharField(max_length=50, blank=True, null=True, help_text="For CPU/Mobo")
    ram_type = models.CharField(max_length=50, blank=True, null=True, help_text="For RAM/Mobo")
    wattage = models.IntegerField(default=0, help_text="Power Draw (or Output for PSU)")
    
    # Image (Optional for now, helps with display later)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# 3. BUILD (The Project File)
class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="My New PC")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

# 4. BUILD ITEM (The Connector)
class BuildItem(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in {self.build.name}"