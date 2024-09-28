import os

from django import setup

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
setup()
