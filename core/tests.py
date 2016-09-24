import random

from django.test import TestCase, Client
from .models import Mineral

DATA = [
    {
        "name": "ATest Mineral 1",
        "image_filename": "200px-Test_Mineral_1.jpg",
        "image_caption": "A Testy Mineral",
        "category": "",
        "formula": "",
        "mohs_scale_hardness": "1.0",
        "group": "Oxides",
        "color": "green"
    },
    {
        "name": "ATest Mineral 2",
        "image_filename": "200px-Test_Mineral_2.jpg",
        "image_caption": "A Testy Mineral",
        "category": "",
        "formula": "",
        "mohs_scale_hardness": "2.0",
        "group": "Carbonates",
        "color": "red"
    },
    {
        "name": "CTest Mineral 3",
        "image_filename": "200px-Test_Mineral_2.jpg",
        "image_caption": "A Testy Mineral",
        "category": "",
        "formula": "",
        "mohs_scale_hardness": "2.0",
        "group": "Other",
        "color": "blue"
    }
]


class MineralTest(TestCase):
    def setUp(self):
        self.client = Client()

        for item in DATA:
            Mineral.objects.create(**item)

    def test_mineral_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['mineral_list']), 2)

    def test_mineral_by_letter(self):
        response = self.client.get('/by-letter/C/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['mineral_list']), 1)
        self.assertContains(response, 'CTest Mineral 3')

    def test_colors_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.context['color_list']), 0)

    def test_colors_choice(self):
        response = self.client.get('/by-color/red/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.context['color_list']), 0)
        self.assertContains(response, 'ATest Mineral 2')

    def test_group_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.context['group_list']), 0)

    def test_group_choice(self):
        response = self.client.get('/by-group/Oxides/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.context['group_list']), 0)
        self.assertContains(response, 'ATest Mineral 1')

    def test_mineral_detail(self):
        mineral = Mineral.objects.first()
        response = self.client.get('/detail/{}/'.format(mineral.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['mineral'].pk, mineral.pk)

    def test_mineral_random(self):
        minerals = Mineral.objects.all()
        choice = random.choice(minerals)
        response = self.client.get('/detail/{}/'.format(choice.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['mineral'].pk, choice.pk)
