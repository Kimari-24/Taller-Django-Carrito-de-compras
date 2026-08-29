
# Taller Django — Carrito de compras

**Integrante(s):** Juan David Martínez Areiza

## Descripción
Aplicación de tienda (`tienda`) dentro del proyecto `config`, con tres modelos relacionados (`Producto`, `Carrito`, `ItemCarrito`) totalmente operativos desde el panel de administración de Django.

## Pasos para ejecutar el proyecto

1. Clonar el repositorio y entrar a la carpeta:
   ```
   git clone <url-del-repo>
   cd <carpeta-del-repo>
   ```

2. Crear y activar un entorno virtual:
   ```
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Aplicar migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crear un superusuario:
   ```
   python manage.py createsuperuser
   ```

6. Levantar el servidor:
   ```
   python manage.py runserver
   ```

7. Entrar al panel de administración en `http://127.0.0.1:8000/admin/`.