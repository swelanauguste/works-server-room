import csv

from django.core.management.base import BaseCommand

from ...models import Rack, Stack


class Command(BaseCommand):
    help = "Load racks and stacks into the database"

    def handle(self, *args, **options):

        for name in ["one", "two"]:

            # Create a new racks and stacks instance
            name, created = Rack.objects.get_or_create(
                name=name,
            )
        
        for name in ["one", "two"]:
            
            name, created = Stack.objects.get_or_create(
                name=name,
            )

        self.stdout.write(self.style.SUCCESS("Racks and stacks loaded successfully from CSV!"))
