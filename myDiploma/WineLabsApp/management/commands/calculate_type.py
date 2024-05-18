from WineLabsApp.models import Wine
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'List spakrling wines:'

    def handle(self, *args, **kwargs):
        sparkling_wines = Wine.objects.all()

        # Extracting names of sparkling wines
        sparkling_wine_names = [wine.keyword for wine in sparkling_wines]

        # Printing the names of sparkling wines
        for name in sparkling_wine_names:
            self.stdout.write(self.style.SUCCESS(f'Sparkling wine: {name}'))


