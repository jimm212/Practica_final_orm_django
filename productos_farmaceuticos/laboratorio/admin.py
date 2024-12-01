from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto

# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    search_fields = ('nombre',)
    ordering = ('id',)

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio')
    search_fields = ('nombre',)
    ordering = ('id',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    search_fields = ('nombre',)
    ordering = ('id',)