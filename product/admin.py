from django.contrib import admin
from product.models import Product
from django.utils.html import mark_safe


class ProductAdmin(admin.ModelAdmin):
    def image_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width="100px",
            height="100px",
        )
        )

    list_display = ["category", "brand", "supplier", "name",
                    "image_view", "discount_price", "sale_price", "total_quanitity"]

    list_filter = ["category", "name", "total_quanitity"]


admin.site.register(Product, ProductAdmin)
