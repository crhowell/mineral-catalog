#!/usr/bin/env python
# -*-coding=utf-8 -*-

import os
from urllib import parse

from django.core.management.base import BaseCommand
from mineral_catalog.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Decodes any encodings with % to proper UTF8 value on all files in a given folder.'

    def add_arguments(self, parser):
        parser.add_argument('folder_name')

    def handle(self, *args, **options):
        if options['folder_name']:
            path = os.path.join(BASE_DIR, options['folder_name'])
            directory = os.listdir(path)
            for file in directory:
                os.rename(
                    os.path.join(path, file),
                    os.path.join(path, parse.unquote(file))
                )
