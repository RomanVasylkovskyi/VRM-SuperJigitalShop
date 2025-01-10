from django.core.management.base import BaseCommand
from Store.models import Product
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Наповнює базу даних тестовими товарами'

    def handle(self, *args, **kwargs):
        # Видалення старих даних (опціонально)
        Product.objects.all().delete()

        # Ініціалізація Faker
        faker = Faker('uk_UA')

        # Створення 10 тестових записів
        for _ in range(100):
            Product.objects.create(
                name=faker.word().capitalize(),
                price=random.uniform(10.0, 100.0),
                photo='photos/example.jpg',
                description=faker.text(),
                manufacturer=faker.company(),
                rate=random.uniform(1.0, 5.0),
            )

        self.stdout.write(self.style.SUCCESS('Сідер виконаний успішно!'))
