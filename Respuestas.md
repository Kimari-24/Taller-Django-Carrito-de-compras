# Respuestas — Taller Introducción a Django 
Juan David Martinez Areiza - TDEA 
# 1 Arquitectura MTV

>Django separa responsabilidades en tres capas: Modelo establece la lógica de acceso a la base de datos mediante el ORM y define la estructura de los datos; Template es la capa de presentación, un archivo HTML que tiene una sintaxis especial para representar datos dinámicos. View es el intermediario que recibe las solicitudes y realiza consultas o modificaciones de datos mediante los modelos, y determina qué template utilizar con dicha información. El proceso de una solicitud es el siguiente: el usuario redacta una URL en urls.py, la cual compara con sus patrones y la envía a una vista. La vista corre su lógica, consultando al modelo si es necesario. Después, escoge un template y le entrega los datos (contexto). El template produce el HTML final, que Django envuelve en una respuesta HTTP que aparece en el navegador.

# Pregunta 2 — Proyecto vs. Aplicación

> A) Un proyecto es el contenedor de la configuración global de un sitio Django (URLs raíz, settings, WSGI/ASGI), mientras que una aplicación es un módulo autónomo y reutilizable que satisface una función específica. Un proyecto puede tener varias aplicaciones. Ejemplo: un proyecto de comercio electrónico que incluya aplicaciones para pagos, usuarios y tienda.

> B)
| Archivo | ¿Para qué sirve? |
| :--- | :--- |
| **models.py** | Define las clases que representan las tablas de la base de datos y sus campos (el "M" de MTV). |
| **views.py** | Contiene la lógica que procesa las peticiones y devuelve una respuesta (renderiza un template, redirige, etc.). |
| **admin.py** | Registra los modelos para que aparezcan (y se puedan personalizar) en el panel de administración de Django. |
| **migrations/** | Guarda el historial versionado de los cambios en los modelos, para poder aplicarlos a la base de datos. |

# Pregunta 3 — ORM y migraciones
>a) El ORM (Object-Relational Mapping) de Django permite que las clases y objetos de Python se conviertan en filas y tablas de una base de datos relacional, lo cual posibilita realizar consultas sin tener que redactar SQL directamente. Beneficio: el código se puede trasladar entre motores de bases de datos, es más fácil de leer y disminuye la probabilidad de inyección SQL. Inconveniente: puede producir SQL menos efectivo que el escrito de forma manual en consultas muy complicadas y añade una curva de aprendizaje propia.

>b) makemigrations examina las modificaciones realizadas en los modelos y produce los archivos de migración (que indican cómo cambiar el esquema); migrate, por su parte, toma esas migraciones y las aplica a la base de datos, creando o modificando las tablas. Makemigrations siempre se ejecuta antes que migrate.

>c) 
| SQL | ORM de Django |
| :--- | :--- |
| `SELECT * FROM producto;` | `Producto.objects.all()` |
| `SELECT * FROM producto WHERE precio > 50000;` | `Producto.objects.filter(precio__gt=50000)` |
    


