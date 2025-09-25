from django.db import models

# Create your models here.
class Category(models.Model):
    class CategoryType(models.TextChoices):
        INCOME = 'IN', 'Income'
        EXPENSE = 'EX', 'Expense'
    
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=CategoryType.choices, default=CategoryType.EXPENSE)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    # String representation
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    owner_id = models.ForeignKey('auth.User', related_name='owned_by', on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='subcategory', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner_id = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.amount} - {self.category.name} - {self.date}"