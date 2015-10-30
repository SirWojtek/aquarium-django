#!/usr/bin/python2

from os import environ
environ["DJANGO_SETTINGS_MODULE"] = "aquarium_django.settings"

from temperature_module.models import TemperatureHistory
from filter_module.models import FilterHistory
import django

def main():
    for i in range(1,20):
        t = TemperatureHistory(value = i)
        t.save()

    for i in [True, False, False, True]:
        f = FilterHistory(status = i)
        f.save()

if __name__ == '__main__':
    main()
