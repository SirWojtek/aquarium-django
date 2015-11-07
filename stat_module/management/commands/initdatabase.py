from django.core.management.base import NoArgsCommand
from stat_module.models import Settings
from defaults import Default

class Command(NoArgsCommand):
    help = 'Fills database with initial settings'

    def handle(self, *args, **options):
        if Settings.objects.all():
            raise CommandError('Settings are already filled')

        Settings(temperature = Default.temperature,
            heating_status = Default.heating_status,
            filter_status = Default.filter_status,
            light_status = Default.light_status).save()
