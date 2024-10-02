import csv

from django.core.management.base import BaseCommand

from ...models import Rack, Stack, Switch


class Command(BaseCommand):
    help = "Load ports and VLANs from a CSV file into the database"

    def handle(self, *args, **options):
        # Get the file path and switch name from the command arguments
        csv_file_path = "static/docs/switches.csv"

        # Get or create the switch instance
        with open(csv_file_path, newline="") as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                name = row["name"]
                serial_number = row["serial_number"]
                try:
                    stack = Stack.objects.get(name__icontains=row["stack"])
                    rack = Rack.objects.get(name__icontains=row["rack"])
                except:
                    stack = None
                if not name:
                    self.stdout.write(
                        self.style.WARNING("name is missing for one row, skipping...")
                    )
                    continue

                # Create a new Port instance
                name, created = Switch.objects.get_or_create(
                    name=name, serial_number=serial_number, stack=stack, rack=rack
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"{name} created successfully.")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"{name} already exists, skipping...")
                    )

        self.stdout.write(self.style.SUCCESS("Switchs loaded successfully from CSV!"))
