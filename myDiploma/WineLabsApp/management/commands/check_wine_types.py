from django.core.management.base import BaseCommand
from WineLabsApp.models import Wine


class Command(BaseCommand):
    help = 'Check the number of [white/sparkling] wines'

    def handle(self, *args, **kwargs):
        num_white_wines = Wine.objects.filter(type='Sparkling').count()
        self.stdout.write(self.style.SUCCESS(f'Number of red wines: {num_white_wines}'))
