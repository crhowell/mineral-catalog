#!/usr/bin/env python
# -*-coding=utf-8 -*-

import os
import csv
import json

from django.core.management.base import BaseCommand, CommandError
from core.models import Mineral
from mineral_catalog.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Populates the database with minerals data.'

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        if options['filename']:
            mineral = Mineral()
            filename = os.path.join(BASE_DIR, options['filename'])
            try:
                data = json.load(open(filename, encoding="utf-8"))
                print(data)
            except FileNotFoundError:
                print('Error, that file does not exist.')
