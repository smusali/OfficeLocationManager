import pandas as pd
from myapp.models import Office, Employee, Coordinate
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load a spreadsheet of offices, employees, and coordinates into the database'

    def handle(self, *args, **kwargs):
        # Read Excel file
        offices_df = pd.read_excel('data.xlsx', sheet_name='Offices')
        employees_df = pd.read_excel('data.xlsx', sheet_name='Employees')
        coordinates_df = pd.read_excel('data.xlsx', sheet_name='Coordinates')

        # Import Offices
        for _, row in offices_df.iterrows():
            Office.objects.update_or_create(
                name=row['Location name'],
                defaults={
                    'address': row['Address'],
                    'city': row['City'],
                    'country': row['Country']
                }
            )

        # Import Employees
        for _, row in employees_df.iterrows():
            office = Office.objects.get(name=row['Location name'])
            Employee.objects.update_or_create(
                first_name=row['First name'],
                last_name=row['Last name'],
                defaults={'office': office}
            )

        # Import Coordinates
        for _, row in coordinates_df.iterrows():
            office = Office.objects.get(name=row['Location name'])
            Coordinate.objects.update_or_create(
                office=office,
                defaults={
                    'latitude': row['Latitude'],
                    'longitude': row['Longitude']
                }
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
