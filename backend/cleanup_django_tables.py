import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dairy_farm.settings')
django.setup()

def cleanup():
    tables_to_drop = [
        'django_admin_log',
        'django_session',
        'auth_group_permissions',
        'auth_user_groups',
        'auth_user_user_permissions',
        'auth_permission',
        'auth_group',
        'auth_user',
        'django_content_type',
        'django_migrations',
        'User_Auth',
    ]
    
    with connection.cursor() as cursor:
        print("Starting cleanup...")
        for table in tables_to_drop:
            try:
                print(f"Dropping {table}...")
                cursor.execute(f"DROP TABLE IF EXISTS {table}")
                print(f"Dropped {table}")
            except Exception as e:
                print(f"Error dropping {table}: {e}")
        print("Cleanup complete.")

if __name__ == "__main__":
    cleanup()
