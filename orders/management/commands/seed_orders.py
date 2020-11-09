from django.core.management.base import BaseCommand, CommandError
# from django_seed import Seed
from orders import models as order_models
from accounts import models as account_models
from confirmations import models as confirmation_models
from datetime import datetime, timedelta
import random

# python manage.py seed --mode=refresh

Name = "orders"

class Command(BaseCommand):
    help = f"This Command creates {Name}"

    def add_arguments(self, parser):
        parser.add_argument(
        "--number", default=2, type=int, help="how many orders you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = account_models.User.objects.all()
        printer_house = confirmation_models.Printer_house.objects.all()
        seeder.add_entity(
            order_models.Order,
            number,
            {
                "is_canceled": lambda x: random.choice([True, False]),
                "is_in_process": lambda x: random.choice([True, False]),
                "customer" : lambda x: random.choice(users),
                "printer_house" : lambda x: random.choice(printer_house),
                "order_time" : lambda x: datetime.now() + timedelta(hours = random.randint(1,5)),
                "pickup_time" : lambda x: datetime.now() + timedelta(hours = random.randint(6,24)),
                "status" : lambda x: random.choice(["picked_up", "complete","pending"]),
                "options_color" : lambda x: random.choice(["black", "color"]),
                "options_print" : lambda x: random.choice(["single", "double"]),
                "options_pages" : lambda x: random.choice(["four", "two","one"]),
                "options_directions" : lambda x: random.choice(["horizontal", "vertical"]),
                "options_flip" : lambda x: random.choice(["horizontal", "vertical"]),
                "number_of_pages" : lambda x: random.randint(1,70),
                "comments" : lambda x: random.choice(["잘 부탁드립니다!", "탕수육은 부먹!", "스테이플러 찍어주세요!"]),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {Name} are created!"))
