from django.contrib import admin
from .models import Producto, Carrito, ItemCarrito


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nombre',)
    list_editable = ('precio', 'stock')  # edición rápida desde la lista


class ItemCarritoInline(admin.TabularInline):
    """Permite agregar/editar los ítems de un carrito en la misma pantalla."""
    model = ItemCarrito
    extra = 1
    readonly_fields = ('subtotal_display',)

    def subtotal_display(self, obj):
        # Reto opcional 2: mostrar el subtotal como columna de solo lectura
        if obj.pk:
            return obj.subtotal()
        return "-"
    subtotal_display.short_description = "Subtotal"


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'creado', 'total')
    inlines = [ItemCarritoInline]