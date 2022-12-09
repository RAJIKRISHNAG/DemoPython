from django.contrib import admin
from.models import category,product

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    List_disply=['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    List_disply=['name','price','stock','available','created','updated',]
    List_editable=['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    List_per_page=20

admin.site.register(product,productAdmin)
