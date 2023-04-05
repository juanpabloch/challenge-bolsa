from django.db import models
import uuid

# Create your models here.

class Products(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code    = models.CharField(max_length=10, unique=True)
    buy     = models.DecimalField(max_digits=10, decimal_places=2)
    sell    = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.code
    
    class Meta:
        db_table = "products"
        verbose_name_plural = "Products"
