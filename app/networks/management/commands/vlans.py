import csv

from django.core.management.base import BaseCommand

from ...models import vLan


class Command(BaseCommand):
    help = "Load ports and VLANs from a CSV file into the database"


    def handle(self, *args, **options):
        # Get the file path and switch name from the command arguments
        csv_file_path = "static/docs/vlans.csv"

        # Get or create the switch instance
        with open(csv_file_path, newline="") as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                name = row["name"]
                role = row["role"]

                if not name:
                    self.stdout.write(
                        self.style.WARNING(
                            "vlan name is missing for one row, skipping..."
                        )
                    )
                    continue

                # Create a new Port instance
                name, created = vLan.objects.get_or_create(
                    name=name,
                    role=role
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"vLan {name} created successfully."
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"vLan {name} already exists, skipping..."
                        )
                    )

        self.stdout.write(self.style.SUCCESS("vLans loaded successfully from CSV!"))
