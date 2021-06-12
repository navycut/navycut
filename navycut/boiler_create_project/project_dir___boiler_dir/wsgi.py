from navycut.utils.server import create_wsgi_app
from os import environ


# Web server gateway interface
# use gunicorn wsgi server to run this app

#define your default settings file here:
environ.setdefault("NAVYCUT_SETTINGS_MODULE", "project_name___boiler_var.settings")

application = create_wsgi_app()