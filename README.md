# Proyecto de Implementación del Patrón Composite View en Flask

## Autor
- **Nombre:** Gerardo Isidro Herrera Pacheco
- **Matrícula:** ISC 68612
- **Semestre:** 8vo
- Materia: Temas selectos de Programación
- **Maestro:** Jose C Aguilar Canepa
- **Institución:** Universidad Autónoma de Campeche, Facultad de Ingeniería

## Descripción del Proyecto
Este proyecto implementa el patrón de diseño Composite View utilizando el framework Flask de Python. El sistema desarrollado es un panel de administración web que demuestra la teorio básica del patron empresarial web "Composite View" mostrando modularización y reutilización efectiva de componentes de interfaz de usuario.

### Características Principales
- Panel de control interactivo
- Componentes reutilizables (header, navigation, sidebar, footer)
- Demostración de inclusiónes condicionales, para ello se coloco simulaciones de:
- Sistema de autenticación con roles: administrador. Dependiendo si admin o no se muestran algunos componentes(se maneja en el app.py)
- Sistema de notificaciones (Es SIMULADO, se maneja en los atributos en app.py) para mostrar las notificaciones si existen.
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

### Diagrama de Clases UML
El diagrama de clases muestra la estructura principal del sistema, incluyendo:
- Clase Flask Principal (App)
- UserManager
- ViewComponents
- PageViews
- Relaciones entre componentes

- ![Clase UML](https://github.com/user-attachments/assets/78672c93-0a66-4649-b383-8f8246d18406)




