# Proyecto de Implementación del Patrón Composite View en Flask

## Autor
- **Nombre:** Gerardo Isidro Herrera Pacheco
- **Matrícula:** ISC 68612
- **Semestre:** 8vo
- **Maestro:** Jose C Aguilar Canepa
- **Institución:** Universidad Autónoma de Campeche, Facultad de Ingeniería

## Descripción del Proyecto
Este proyecto implementa el patrón de diseño Composite View utilizando el framework Flask de Python. El sistema desarrollado es un panel de administración web que demuestra la modularización y reutilización efectiva de componentes de interfaz de usuario.

### Características Principales
- Sistema de autenticación con roles (administrador)
- Panel de control interactivo
- Componentes reutilizables (header, navigation, sidebar, footer)
- Sistema de notificaciones
- Interfaz responsiva y moderna
- Gestión de múltiples vistas (estadísticas, configuración, reportes)

## Estructura del Proyecto
```
composite_view_project/
│
├── static/
│   └── css/
│       └── styles.css
│
├── templates/
│   ├── base.html
│   ├── components/
│   │   ├── header.html
│   │   ├── navigation.html
│   │   ├── sidebar.html
│   │   ├── user_info.html
│   │   ├── dashboard_widgets.html
│   │   └── footer.html
│   └── pages/
│       ├── home.html
│       ├── dashboard.html
│       ├── statistics.html
│       ├── settings.html
│       └── reports.html
│
├── app.py
└── requirements.txt
```

## Funcionamiento del Sistema

### Patrón Composite View
El proyecto implementa el patrón Composite View para crear una interfaz de usuario modular y mantenible. Este patrón permite:
- Reutilización de componentes comunes en múltiples páginas
- Separación clara de responsabilidades
- Mantenimiento simplificado
- Consistencia en la interfaz de usuario

### Componentes Principales

1. **Base Template (base.html)**
   - Actúa como el esqueleto principal de la aplicación
   - Define la estructura común para todas las páginas
   - Incluye los componentes reutilizables (header, navigation, sidebar)

2. **Componentes Reutilizables**
   - Header: Muestra el título y la información del usuario
   - Navigation: Barra de navegación principal
   - Sidebar: Menú lateral con accesos rápidos
   - Footer: Información de contacto y enlaces útiles
   - User Info: Muestra datos del usuario y notificaciones
   - Dashboard Widgets: Componentes informativos del panel de control

3. **Páginas Específicas**
   - Home: Página principal
   - Dashboard: Panel de control administrativo
   - Statistics: Visualización de estadísticas
   - Settings: Configuración del sistema
   - Reports: Generación y visualización de reportes

### Sistema de Rutas
El sistema implementa rutas protegidas que:
- Verifican el rol del usuario (admin)
- Manejan la autorización de acceso
- Renderizan las plantillas correspondientes con sus componentes

## Diagramas UML

### Diagrama de Clases
<descripción>
El diagrama de clases muestra la estructura principal del sistema, incluyendo:
- Clase Flask Principal (App)
- Controladores de Rutas
- Modelo de Usuario
- Componentes de Vista
- Relaciones entre componentes

Las clases están organizadas siguiendo el patrón MVC con énfasis en la composición de vistas.
</descripción>
[Aquí va el diagrama de clases UML]

### Diagrama de Componentes
<descripción>
El diagrama de componentes ilustra la estructura modular del sistema, mostrando:
- Componentes del Frontend (Templates, CSS)
- Componentes del Backend (Flask, Rutas)
- Dependencias entre componentes
- Interfaces de comunicación
</descripción>
[Aquí va el diagrama de componentes UML]

### Diagrama de Secuencia
<descripción>
El diagrama de secuencia muestra el flujo de interacción para una solicitud típica:
1. Cliente realiza petición
2. Flask procesa la ruta
3. Verificación de autorización
4. Composición de vista
5. Renderizado de componentes
6. Respuesta al cliente
</descripción>
[Aquí va el diagrama de secuencia UML]
