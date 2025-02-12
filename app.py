from flask import Flask, render_template

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Simulación de datos de usuario para demostrar renderizado condicional
def get_user_data():
    return {
        'is_logged_in': True,  # Indica si el usuario ha iniciado sesión
        'username': 'Gerardo_Herrera',  # Nombre de usuario
        'role': 'admin',  # Rol del usuario (admin en este caso)
        'notifications': 10  # Número de notificaciones pendientes
    }

# Ruta para la página de inicio
@app.route('/')
def home():
    user_data = get_user_data()  # Obtenemos los datos del usuario
    return render_template(
        'pages/home.html', 
        user=user_data,
        show_notifications=user_data['notifications'] > 0  # Se mostrará si hay notificaciones
    )

# Ruta para el panel de administración (dashboard)
@app.route('/dashboard')
def dashboard():
    user_data = get_user_data()
    if user_data['role'] != 'admin':  # Restringimos el acceso solo a administradores
        return 'Acceso no autorizado', 403  # Código de error 403 (Prohibido)
    return render_template(
        'pages/dashboard.html',
        user=user_data,
        show_widgets=True,  # Activamos la visualización de widgets
        show_sidebar=True,  # Activamos la barra lateral
        show_notifications=user_data['notifications'] > 0  # Se mostrará si hay notificaciones

    )

# Ruta para la página de estadísticas
@app.route('/estadisticas')
def statistics():
    user_data = get_user_data()
    if user_data['role'] != 'admin':  # Solo los administradores pueden acceder
        return 'Acceso no autorizado', 403
    return render_template('pages/statistics.html', user=user_data, show_sidebar=True)

# Ruta para la página de configuración
@app.route('/configuracion')
def settings():
    user_data = get_user_data()
    if user_data['role'] != 'admin':  # Solo los administradores pueden acceder
        return 'Acceso no autorizado', 403
    return render_template('pages/settings.html', user=user_data, show_sidebar=True)

# Ruta para la página de reportes
@app.route('/reportes')
def reports():
    user_data = get_user_data()
    if user_data['role'] != 'admin':  # Solo los administradores pueden acceder
        return 'Acceso no autorizado', 403
    return render_template('pages/reports.html', user=user_data, show_sidebar=True)

# Iniciar la aplicación si se ejecuta este archivo directamente
if __name__ == '__main__':
    app.run(debug=True)  # Modo de depuración activado para facilitar el desarrollo