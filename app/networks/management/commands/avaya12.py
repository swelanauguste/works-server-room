import csv

from django.core.management.base import BaseCommand

from ...models import Port, Switch, vLan, Stack


class Command(BaseCommand):
    help = "Load ports and VLANs from a CSV file into the database"


    def handle(self, *args, **options):
        # Get the file path and switch name from the command arguments
        csv_file_path = "static/docs/avaya12.csv"

        # Get or create the switch instance
        with open(csv_file_path, newline="") as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                port_number = row["port"]
                vlan_str = row["vlan"]

                if not port_number:
                    self.stdout.write(
                        self.style.WARNING(
                            "Port number is missing for one row, skipping..."
                        )
                    )
                    continue

                # Create a new Port instance
                port, created = Port.objects.get_or_create(
                    switch=Switch.objects.get(serial_number__icontains="15JP314F805M"),
                    port=int(port_number),  # Make sure port number is an integer
                )

                if vlan_str:
                    # Parse VLAN IDs from the string, split by commas, and strip whitespace
                    vlan_ids = [
                        int(vlan.strip())
                        for vlan in vlan_str.split(",")
                        if vlan.strip()
                    ]

                    # Add VLANs to the port
                    for vlan_id in vlan_ids:
                        vlan, _ = vLan.objects.get_or_create(name=vlan_id)
                        port.vlan.add(vlan)

                # Save the final Port with all relationships
                port.save()

        self.stdout.write(self.style.SUCCESS("Ports loaded successfully from CSV!"))
