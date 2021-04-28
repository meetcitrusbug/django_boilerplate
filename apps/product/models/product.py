from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import ugettext_lazy as _
from apps.utils.get_user_model import get_user_model
from product.models.product_image import ProductImage

class Product(ActivityTracking):
    
    STATUS_CHOICES = (
        ("OFS", _("OFS")),
        ("PENDING", _("PENDING")),
        ("ACTIVE", _("ACTIVE")),
        ("INACTIVE", _("INACTIVE")),
        ("DECLINED", _("DECLINED")),
        ("SOLD", _("SOLD")),
    )

    SHIPPING_METHOD_CHOICES = (
        ("LOCAL_SHIPPING", _("LOCAL_SHIPPING")),
        ("LOGISITC_COMPANY", _("LOGISITC_COMPANY")),
        ("PICKUP", _("PICKUP")),
    )
    
    name = models.CharField(_('name'), max_length=255)
    user = models.ForeignKey(get_user_model(), db_index=True, on_delete=models.CASCADE, 
                                        null=True, blank=True)
    product_number = models.CharField( max_length=25, null=True, blank=True)
    description = models.TextField(_("description"), blank=True, null=True)
    sub_category = models.ForeignKey("category.SubCategory", db_index=True, on_delete=models.CASCADE)
    product_shipping_method = models.CharField(_('product_shipping_method'),max_length=128 ,
                                               choices=SHIPPING_METHOD_CHOICES, null=True,
                                               blank=True)
    status = models.CharField(_("status"), db_index=True, max_length=128,choices=STATUS_CHOICES,
                                null=True, blank=True, default='PENDING')
    price = models.FloatField(null=True, blank=True)
    is_refundable = models.BooleanField(
        ('is_refundable'),
        default=False, 
    )
    
    class Meta: 
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        
        return self.name
   
    @property 
    def image(self):
        image = ''
        product_image = ProductImage.objects.filter(product__pk=self.pk).order_by('-id').first()
        if product_image and product_image.image:
            image = product_image.image.url
        return image