
# MultielectricosGS - Sistema de Cotización, Facturación e Inventario

## Descripción

Este proyecto es un sistema web de gestión para **MultielectricosGS SAS** diseñado para manejar cotizaciones, facturación e inventario. El sistema está construido utilizando el framework **Django** como base para el backend, con **HTML5** y **Bootstrap** para el frontend, y **MySQL** como base de datos. 

El sistema permite gestionar productos, clientes, trabajadores y transacciones comerciales, brindando una solución integral para la administración de ventas y control de inventarios.

## Características

- **Gestión de productos:** Control detallado del inventario, incluyendo cantidad de stock, precios, categorías y alertas automáticas cuando el stock llega al mínimo.
- **Cotizaciones:** Creación de cotizaciones personalizadas para clientes, con la posibilidad de modificar detalles antes de generar la factura. Las cotizaciones incluyen selección de productos, cantidades, y descuentos.
- **Facturación:** Generación de facturas en formato **PDF** y **Excel**, con cálculo automático de impuestos como el **IVA** y la capacidad de aplicar descuentos. Las facturas pueden enviarse por correo electrónico u otros medios.
- **Control de inventario:** Gestión manual del inventario, con planes para automatizar el descuento de productos cuando se genera una factura. Alertas configurables cuando el stock de un producto está por debajo del mínimo.
- **Autenticación y roles de usuario:** El sistema cuenta con un sistema de autenticación basado en roles, que otorga permisos diferenciados según el rango en la empresa (administrador, vendedor, etc.).
- **Medios y formas de pago:** El sistema permite manejar múltiples formas de pago (efectivo, tarjeta, transferencia) y formas de pago (de contado, a crédito).
  
## Tecnologías Utilizadas

- **Backend:** Django (Python)
- **Frontend:** HTML5, Bootstrap, CSS, JavaScript
- **Base de datos:** MySQL
- **Herramientas:** MySQL Workbench (para la creación de la base de datos)
- **Control de versiones:** Git y GitHub

## Requisitos

Para ejecutar este proyecto en un entorno local, asegúrate de tener instaladas las siguientes herramientas:

- Python 3.10+
- Django 4.x
- MySQL
- Git

### Instalación

1. Clona el repositorio:
   \`\`\`bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   \`\`\`
2. Instala las dependencias (añadir `requirements.txt` una vez creado):
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Configura la base de datos en `settings.py`:
   \`\`\`python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nombre_de_la_base_de_datos',
           'USER': 'tu_usuario',
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   \`\`\`
4. Realiza las migraciones:
   \`\`\`bash
   python manage.py migrate
   \`\`\`
5. Ejecuta el servidor de desarrollo:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

## Uso

- **Productos:** Gestión de los productos disponibles, creación, edición y eliminación de productos, incluyendo su stock, precios y categorías.
- **Cotizaciones:** Creación y edición de cotizaciones, con posibilidad de modificar los detalles de productos y precios antes de generar la factura.
- **Facturación:** Generación de facturas basadas en las cotizaciones, con posibilidad de enviar facturas en **PDF** o **Excel** a través de correo electrónico.
- **Inventario:** Gestión manual del stock, con futuras funcionalidades para automatizar el descuento de productos al generar facturas.

## Flujo de Trabajo

1. **Creación de Cotización:** El usuario selecciona productos y cantidades para generar una cotización que puede ser modificada antes de aprobarse.
2. **Generación de Factura:** Una vez aprobada la cotización, los detalles de esta son utilizados para generar una factura, que incluye el cálculo automático de impuestos, descuentos y medios de pago.
3. **Manejo de Inventario:** En el futuro, al generar la factura se reducirá automáticamente el stock del producto en inventario. Actualmente, el control de inventario es manual.

## Dependencias

- Django
- MySQL
- Bootstrap
- (Añadir más dependencias cuando esté disponible el archivo `requirements.txt`)

## Capturas de Pantalla (Opcional)

Incluye imágenes o gifs de la interfaz de usuario para mostrar cómo se ve el sistema.

## Contribuciones

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

## Próximas Funcionalidades

- Automatización del descuento de stock al generar una factura.
- Implementación de alertas para stock mínimo.
- Creación de documentación técnica y guía de usuario.
