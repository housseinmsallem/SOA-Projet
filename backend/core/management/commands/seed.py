import os
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Seeds the MSSQL database with initial data"

    def handle(self, *args, **options):
        # 1. Path to your .sql file
        file_path = os.path.join(os.getcwd(), "seed_data.sql")

        self.stdout.write(f"Reading script from: {file_path}")

        try:
            with open(file_path, "r") as f:
                sql_script = f.read()

            # 2. Execute against MSSQL
            with connection.cursor() as cursor:
                # Note: MSSQL 'GO' commands aren't supported by the driver.
                # If your script has 'GO', split it or remove it.
                commands = sql_script.split("GO")

                for command in commands:
                    if command.strip():
                        cursor.execute(command)

            self.stdout.write(self.style.SUCCESS("Successfully seeded the database"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Seeding failed: {e}"))
