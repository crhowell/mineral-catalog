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

    def parse_to_fields(self, data_list=[]):
        new_list = []
        if data_list:
            for data in data_list:
                d_list = {}
                for key, value in data.items():
                    d_list[key.replace(' ', '_').lower()] = value
                new_list.append(d_list)
        return new_list

    def handle(self, *args, **options):
        if options['filename']:
            filename = os.path.join(BASE_DIR, options['filename'])
            try:
                with open(filename, encoding='utf-8') as data_file:
                    data = json.load(data_file)
                    mineral_list = self.parse_to_fields(data)
                    for mineral in mineral_list:
                        mnr = Mineral(**mineral).save()
            except FileNotFoundError:
                print('Error, that file does not exist.')
