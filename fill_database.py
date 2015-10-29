#!/usr/bin/python2

from os import environ
environ["DJANGO_SETTINGS_MODULE"] = "aquarium_django.settings"

from temperature_module.models import Temperature
import django

def main():
    for i in range(1,20):
        t = Temperature(value = i)
        t.save()

if __name__ == '__main__':
    main()
