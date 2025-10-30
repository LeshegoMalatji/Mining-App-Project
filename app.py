"""
Flask Main Application
Mining Application for Critical Minerals Data Visualization
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.auth_controller import AuthController
from controllers.data_controller import DataController
from controllers.visualization_controller import VisualizationController
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  # Change this in production

# Initialize controllers
auth_controller = AuthController()
data_controller = DataController()
viz_controller = VisualizationController()

# ==================== Decorator for Login Required ====================

def login_required(f):
    """
    Decorator to require login for certain routes.
    
    Args:
        f: The function to wrap
        
    Returns:
        The wrapped function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.auth_controller import AuthController
from controllers.data_controller import DataController
from controllers.visualization_controller import VisualizationController
from functools import wraps


# ==================== Authentication Routes ====================

@app.route('/')
def index():
    """
    Home page - redirects to login if not authenticated, otherwise to dashboard.
    """
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login page - handles user authentication.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Authenticate user
        user = auth_controller.authenticate_user(username, password)
        
        if user:
            # Get user role
            role = auth_controller.get_user_role(user.get_role_id())
            
            # Store user information in session (convert numpy types to Python types)
            session['user_id'] = int(user.get_id())  # Convert to Python int
            session['username'] = str(user.get_username())  # Convert to Python str
            session['role_id'] = int(user.get_role_id())  # Convert to Python int
            session['role_name'] = str(role.get_name()) if role else 'Unknown'  # Convert to Python str
            session['email'] = str(user.get_email())  # Convert to Python str
            
            flash(f'Welcome, {user.get_username()}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """
    Logout - clears the session and redirects to login.
    """
    username = session.get('username', 'User')
    session.clear()
    flash(f'Goodbye, {username}! You have been logged out.', 'info')
    return redirect(url_for('login'))


# ==================== Dashboard Route ====================

@app.route('/dashboard')
@login_required
def dashboard():
    """
    Main dashboard - central hub after login.
    """
    # Get summary statistics
    countries = data_controller.get_all_countries()
    minerals = data_controller.get_all_minerals()
    sites = data_controller.get_all_sites()
    
    return render_template('dashboard.html',
                         username=session.get('username'),
                         role_name=session.get('role_name'),
                         countries_count=len(countries),
                         minerals_count=len(minerals),
                         sites_count=len(sites))


# ==================== Mineral Routes ====================

@app.route('/minerals')
@login_required
def minerals():
    """
    Display all minerals in the database.
    """
    minerals_list = data_controller.get_all_minerals()
    return render_template('minerals.html',
                         minerals=minerals_list,
                         username=session.get('username'),
                         role_name=session.get('role_name'))


@app.route('/mineral/<int:mineral_id>')
@login_required
def mineral_detail(mineral_id):
    """
    Display detailed information about a specific mineral.
    
    Args:
        mineral_id (int): The mineral ID
    """
    mineral = data_controller.get_mineral_by_id(mineral_id)
    
    if Mineral is None:
        flash('Mineral not found.', 'danger')
        return redirect(url_for('minerals'))
    
    # Get production statistics for this mineral
    production_stats = data_controller.get_production_by_mineral(mineral_id)
    
    # Get sites producing this mineral
    sites = data_controller.get_sites_by_mineral(mineral_id)
    
    # Generate charts
    production_trend_chart = None
    export_value_chart = None
    production_pie_chart = None
    
    if production_stats:
        production_trend_chart = viz_controller.create_production_trend_chart(mineral_id=mineral_id)
        export_value_chart = viz_controller.create_export_value_chart(mineral_id=mineral_id)
        production_pie_chart = viz_controller.create_production_by_country_pie_chart(mineral_id)
    
    return render_template('mineral_detail.html',
                         mineral=mineral,
                         production_stats=production_stats,
                         sites=sites,
                         production_trend_chart=production_trend_chart,
                         export_value_chart=export_value_chart,
                         production_pie_chart=production_pie_chart,
                         username=session.get('username'),
                         role_name=session.get('role_name'))


# ==================== Country Routes ====================

@app.route('/countries')
@login_required
def countries():
    """
    Display all countries in the database.
    """
    countries_list = data_controller.get_all_countries()
    return render_template('countries.html',
                         countries=countries_list,
                         username=session.get('username'),
                         role_name=session.get('role_name'))


@app.route('/country/<int:country_id>')
@login_required
def country_detail(country_id):
    """
    Display detailed information about a specific country.
    
    Args:
        country_id (int): The country ID
    """
    country = data_controller.get_country_by_id(country_id)
    
    if country is None:
        flash('Country not found.', 'danger')
        return redirect(url_for('countries'))
    
    # Get production statistics for this country
    production_stats = data_controller.get_production_by_country(country_id)
    
    # Get sites in this country
    sites = data_controller.get_sites_by_country(country_id)
    
    # Generate charts
    production_trend_chart = None
    export_value_chart = None
    country_map = None
    
    if production_stats:
        production_trend_chart = viz_controller.create_production_trend_chart(country_id=country_id)
        export_value_chart = viz_controller.create_export_value_chart(country_id=country_id)
    
    if sites:
        country_map = viz_controller.create_country_sites_map(country_id)
    
    return render_template('country_detail.html',
                         country=country,
                         production_stats=production_stats,
                         sites=sites,
                         production_trend_chart=production_trend_chart,
                         export_value_chart=export_value_chart,
                         country_map=country_map,
                         username=session.get('username'),
                         role_name=session.get('role_name'))

# ==================== Sites Routes ====================

@app.route('/sites')
@login_required
def sites():
    """
    Display all mining sites with map.
    """
    sites_list = data_controller.get_all_sites()
    
    # Get mineral and country names for each site
    sites_data = []
    for site in sites_list:
        mineral = data_controller.get_mineral_by_id(site.get_mineral_id())
        country = data_controller.get_country_by_id(site.get_country_id())
        
        sites_data.append({
            'site': site,
            'mineral_name': mineral.get_name() if mineral else 'Unknown',
            'country_name': country.get_name() if country else 'Unknown'
        })
    
    # Generate map
    sites_map = viz_controller.create_mining_sites_map()
    
    return render_template('sites.html',
                         sites_data=sites_data,
                         sites_map=sites_map,
                         username=session.get('username'),
                         role_name=session.get('role_name'))


# ==================== Admin Routes ====================

@app.route('/admin/users')
@login_required
@permission_required('manage_users')
def admin_users():
    """
    Admin page to view all users (Administrator only).
    """
    users = auth_controller.get_all_users()
    
    # Get role names for each user
    users_data = []
    for user in users:
        role = auth_controller.get_user_role(user.get_role_id())
        users_data.append({
            'user': user,
            'role_name': role.get_name() if role else 'Unknown'
        })
    
    return render_template('admin_users.html',
                         users_data=users_data,
                         username=session.get('username'),
                         role_name=session.get('role_name'))

# ==================== Error Handlers ====================

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return render_template('error.html', 
                         error_code=404,
                         error_message='Page not found'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors.
    """
    return render_template('error.html',
                         error_code=500,
                         error_message='Internal server error'), 500


    # ==================== Visualization Routes ====================

@app.route('/analytics')
@login_required
def analytics():
    """
    Analytics page with interactive charts and graphs.
    """
    # Generate charts
    mineral_price_chart = viz_controller.create_mineral_price_comparison_chart()
    country_gdp_chart = viz_controller.create_country_gdp_chart()
    production_trend_chart = viz_controller.create_production_trend_chart()
    export_value_chart = viz_controller.create_export_value_chart()
    
    return render_template('analytics.html',
                         mineral_price_chart=mineral_price_chart,
                         country_gdp_chart=country_gdp_chart,
                         production_trend_chart=production_trend_chart,
                         export_value_chart=export_value_chart,
                         username=session.get('username'),
                         role_name=session.get('role_name'))


@app.route('/map')
@login_required
def mining_map():
    """
    Interactive map showing all mining sites.
    """
    # Generate map
    sites_map = viz_controller.create_mining_sites_map()
    
    return render_template('map.html',
                         sites_map=sites_map,
                         username=session.get('username'),
                         role_name=session.get('role_name'))


# ==================== Run Application ====================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
