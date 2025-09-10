from django.db import models

# Create your models here.

class OTOPProduct(models.Model):
    product_name = models.CharField(max_length=500, verbose_name="Product Name")
    local_admin = models.CharField(max_length=200, verbose_name="Local Administration")
    district = models.CharField(max_length=100, verbose_name="District")
    province = models.CharField(max_length=100, verbose_name="Province")
    shop_name = models.CharField(max_length=500, verbose_name="Shop Name")
    address = models.TextField(verbose_name="Address")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Phone Number")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Latitude")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Longitude")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "OTOP Product"
        verbose_name_plural = "OTOP Products"
        ordering = ['province', 'district', 'product_name']
    
    def __str__(self):
        return f"{self.product_name} - {self.province}"
    
    @property
    def has_coordinates(self):
        return self.latitude is not None and self.longitude is not None
    
    @property
    def full_address(self):
        return f"{self.address}, {self.district}, {self.province}"
