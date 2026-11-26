
# STAY TUNED

En tu próximo concierto, STAY TUNED.

## Descripción del proyecto

STAY TUNED es una plataforma web diseñada para mejorar la experiencia, la orientación y la seguridad de los asistentes a conciertos y eventos musicales.

El proyecto fue desarrollado como trabajo práctico final de Programación I, dentro de la Tecnicatura Superior en Desarrollo de Software del ISET N.º 25 Beppo Levi, durante el año 2026.

## Funcionalidades principales

- Visualización y búsqueda de eventos.
- Información detallada de cada evento.
- Cuenta regresiva.
- Visualización de setlists.
- Mapas de recintos con sectores y servicios.
- Registro e inicio de sesión de usuarios.
- Perfil de usuario.
- Credencial médica personal.
- Registro individual de medicamentos.
- Solicitudes de asistencia.
- Panel de administración.
- Modo claro y oscuro.
- Diseño adaptable a dispositivos móviles.
- Configuración como aplicación web progresiva (PWA).

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite
- Git y GitHub

## Estructura del proyecto

El sistema se divide en tres aplicaciones principales:

- `eventos`: gestión y visualización de eventos, sectores y servicios.
- `asistencia`: registro y gestión de solicitudes de asistencia.
- `usuarios`: registro, autenticación, perfiles y credenciales médicas.

La carpeta `config` contiene la configuración general del proyecto.

## Instalación y ejecución

### 1. Clonar el repositorio

Clonar el repositorio y acceder a la carpeta del proyecto.

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual en Windows

```bash
venv\Scripts\activate
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Configurar las variables de entorno

Crear un archivo `.env` en la carpeta principal del proyecto.

Generar una clave secreta mediante:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Agregar la clave generada al archivo `.env`:

```env
SECRET_KEY=clave_generada
```

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

### 7. Crear un superusuario

```bash
python manage.py createsuperuser
```

### 8. Iniciar el servidor

```bash
python manage.py runserver
```

Acceder a la aplicación desde:

http://127.0.0.1:8000/

Panel de administración:

http://127.0.0.1:8000/admin/

## Datos de demostración

Los eventos, sectores, servicios e imágenes pueden cargarse desde el panel de administración de Django.

La base de datos local, los archivos multimedia y las variables de entorno no se incluyen en el repositorio.

## Alcance del proyecto

STAY TUNED es un prototipo académico funcional. Las solicitudes de asistencia se registran en la base de datos y pueden gestionarse desde el panel de administración.

La integración con personal de eventos y servicios de emergencia reales queda contemplada como una mejora futura.

## Autora

Constanza Nicole Mansilla

ISET N.º 25 Beppo Levi — 2026
