if __name__ == '__main__':
    from navycut.command import manage_command
    from os import environ
    environ.setdefault('NAVYCUT_SETTINGS_MODULE', 'project_name___boiler_var.settings')
    manage_command()