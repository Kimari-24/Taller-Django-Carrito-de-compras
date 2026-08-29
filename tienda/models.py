from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-precio']  # Reto opcional 3: siempre de mayor a menor precio

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    cliente = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.cliente} ({self.creado:%Y-%m-%d %H:%M})"

    def total(self):
        return sum(item.subtotal() for item in self.items.all())
    total.short_description = "Total"


class ItemCarrito(models.Model):
    # related_name='items' es la relación inversa que usa Carrito.total()
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def subtotal(self):
        return self.producto.precio * self.cantidad