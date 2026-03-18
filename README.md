# ⚗️ Laboratorio del Profesor Oak

Sistema de reserva de criaturas mágicas para el Laboratorio del Profesor Oak.

## Descripción
Este proyecto es una aplicación Django diseñada para gestionar la selección y reserva de criaturas en franjas horarias específicas. Incluye un sistema de autenticación completo y una interfaz inspirada en la estética retro de los videojuegos Pokémon.

## Tecnologías Utilizadas
- **Backend:** Django 6.0.3
- **Frontend:** HTML5, CSS3 (Vanilla)
- **Fuentes:** Google Fonts (Roboto, Press Start 2P)
- **Base de Datos:** SQLite3

## Instalación y Configuración

### 1. Clonar el repositorio y entrar al directorio
```bash
git clone <url-del-repo>
cd oak_lab
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear un superusuario (Admin)
Necesitarás un superusuario para cargar las criaturas y los horarios iniciales en el panel de administración.
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor
```bash
python manage.py run_server
```

## Configuración Inicial (Admin)
Una vez dentro del panel de administración (`/admin/`):
1. **Creature**: Agrega al menos una criatura (ej. Bulbasaur, Charmander, Squirtle).
2. **TimeSlot**: Agrega horarios disponibles con una capacidad mayor a 0.

## Estructura del Proyecto
- `config/`: Configuración global de Django (settings, urls).
- `scheduling/`: Aplicación principal que contiene los modelos de reserva, vistas y templates.

---
**¡Prepárate para elegir a tu compañero!** ⚗️🎉
