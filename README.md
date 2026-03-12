# Stock Manager

Mini aplicación de gestión de inventario desarrollada con Django y Tailwind CSS.  
**By Bernardo Dieta**

---
**VIDEO DE MUESTRA** Raiz del proyecto
Video De muestra.mp4



## Requisitos

- Python 3.11+
- pip

## Instalación

```bash
git clone <url-del-repo>
cd stockManager
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acceder en `http://127.0.0.1:8000/`

---

## Roles

| Rol | Acceso |
|---|---|
| **Admin** / superusuario | CRUD completo en todas las secciones |
| **Empleado** | Ver productos y registrar salidas de stock |

---

## Estructura del proyecto

```
stockManager/
├── inventario/        # App: inventarios y categorías
├── producto/          # App: productos, movimientos de stock, proveedores
├── users/             # App: autenticación, roles, dashboard
├── stockMaganer/      # Configuración del proyecto (settings, urls)
├── templates/         # Templates globales (base, dashboard, users, inventario)
├── media/             # Archivos subidos (imágenes de productos)
├── manage.py
└── db.sqlite3
```

---

## Endpoints

### Autenticación (`/`)
| URL | Descripción |
|---|---|
| `/` | Dashboard principal |
| `/auth/login/` | Inicio de sesión |
| `/auth/logout/` | Cierre de sesión |
| `/auth/registro/` | Registro de usuario |

### Usuarios (`/usuarios/`) — solo admin
| URL | Descripción |
|---|---|
| `/usuarios/` | Listado de usuarios |
| `/usuarios/<id>/editar/` | Editar usuario y rol |
| `/usuarios/<id>/eliminar/` | Eliminar usuario |

### Inventarios (`/inventarios/`) — solo admin
| URL | Descripción |
|---|---|
| `/inventarios/` | Listado de inventarios |
| `/inventarios/nuevo/` | Crear inventario |
| `/inventarios/<id>/editar/` | Editar inventario |
| `/inventarios/<id>/eliminar/` | Eliminar inventario |
| `/inventarios/categorias/` | Listado de categorías |
| `/inventarios/categorias/nuevo/` | Crear categoría |
| `/inventarios/categorias/<id>/editar/` | Editar categoría |
| `/inventarios/categorias/<id>/eliminar/` | Eliminar categoría |

### Productos (`/productos/`)
| URL | Descripción | Rol mínimo |
|---|---|---|
| `/productos/` | Listado de productos | Empleado |
| `/productos/<id>/` | Detalle de producto | Empleado |
| `/productos/nuevo/` | Crear producto | Admin |
| `/productos/<id>/editar/` | Editar producto | Admin |
| `/productos/<id>/eliminar/` | Eliminar producto | Admin |
| `/productos/salida/` | Registrar salida de stock | Empleado |
| `/productos/salidas/` | Historial de salidas | Admin |

### Proveedores (`/productos/proveedores/`) — solo admin
| URL | Descripción |
|---|---|
| `/productos/proveedores/` | Listado de proveedores |
| `/productos/proveedores/nuevo/` | Crear proveedor |
| `/productos/proveedores/<id>/editar/` | Editar proveedor |
| `/productos/proveedores/<id>/eliminar/` | Eliminar proveedor |
| `/productos/proveedores/rapido/` | Crear proveedor vía modal (JSON) |

---

## Flujo completo — Administrador

Este flujo cubre la configuración inicial del sistema y el uso diario de todas las funcionalidades disponibles para un usuario con rol **Admin** o superusuario.

### 1. Primer acceso
1. Ir a `/auth/login/` e ingresar con las credenciales del superusuario creado con `createsuperuser`.
2. Se redirige automáticamente al **Dashboard** (`/`), donde se ven los totales de productos, inventarios y categorías, las acciones rápidas y los últimos movimientos.

### 2. Configurar la estructura base

Antes de cargar productos hay que tener inventarios, categorías y proveedores.

**Inventarios**
1. En el sidebar ir a **Inventarios** → `/inventarios/`.
2. Hacer clic en **Nuevo inventario**, completar nombre y descripción, guardar.

**Categorías**
1. En el sidebar ir a **Categorías** → `/inventarios/categorias/`.
2. Hacer clic en **Nueva categoría**, asignarle un nombre y seleccionar el inventario creado, guardar.

**Proveedores**
1. En el sidebar ir a **Proveedores** → `/productos/proveedores/`.
2. Hacer clic en **Nuevo proveedor**, completar nombre, contacto, teléfono y email, guardar.

### 3. Cargar productos
1. En el sidebar ir a **Productos** → `/productos/`.
2. Hacer clic en **Nuevo producto**.
3. Seleccionar inventario, categoría y proveedor en los desplegables.
   - Si el proveedor no existe aún, hacer clic en **+ Añadir** al lado del desplegable, completar los datos en el modal y guardar — queda seleccionado automáticamente.
4. Completar nombre, descripción, stock inicial e imagen, guardar.

### 4. Gestionar usuarios
1. En el sidebar ir a **Usuarios** → `/usuarios/`.
2. Ver el listado de usuarios registrados.
3. Hacer clic en **Editar** para cambiar el rol de un usuario entre `Admin` y `Empleado`.
4. Hacer clic en **Eliminar** para dar de baja un usuario.

### 5. Registrar una salida de stock
1. En el sidebar ir a **Salida de stock** → `/productos/salida/`.
2. Seleccionar el producto y la cantidad a descontar, guardar.
3. El stock del producto se actualiza automáticamente.

### 6. Revisar el historial
1. En el sidebar ir a **Historial de salidas** → `/productos/salidas/`.
2. Ver todas las salidas registradas con producto, cantidad, usuario y fecha.

### 7. Editar o eliminar registros
- Desde cualquier listado (productos, inventarios, categorías, proveedores) usar los enlaces **Editar** o **Eliminar** al costado de cada ítem.
- Para un producto, entrar al **detalle** (`/productos/<id>/`) para ver todos sus datos e imagen antes de editar.

---

## Flujo completo — Empleado

Este flujo cubre el uso diario de las funcionalidades disponibles para un usuario con rol **Empleado**.

### 1. Acceso
1. Ir a `/auth/login/` e ingresar con usuario y contraseña asignados por el administrador.
2. En la navbar se muestra el nombre de usuario con el badge **Empleado**.
3. Se redirige al **Dashboard**, donde se ven los totales y las acciones disponibles.

### 2. Consultar productos
1. En el sidebar ir a **Productos** → `/productos/`.
2. Ver el listado completo con nombre, inventario, categoría, proveedor y stock actual.
3. Hacer clic en el nombre o en **Ver** para abrir el detalle del producto (`/productos/<id>/`), donde se muestra la imagen, descripción, fecha de ingreso y proveedor asignado.

### 3. Registrar una salida de stock
1. En el sidebar ir a **Salida de stock** → `/productos/salida/`.
2. Seleccionar el producto del desplegable y la cantidad a retirar.
3. Agregar una observación opcional y confirmar.
4. El sistema descuenta la cantidad del stock automáticamente y redirige al listado de productos.

