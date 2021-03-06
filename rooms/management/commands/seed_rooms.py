import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "방이름": lambda x: seeder.faker.address(),
                "주인장": lambda x: random.choice(all_users),
                "방종류": lambda x: random.choice(room_types),
                "투숙객": lambda x: random.randint(1, 20),
                "침대": lambda x: random.randint(1, 5),
                "화장실": lambda x: random.randint(1, 5),
                "욕조": lambda x: random.randint(1, 5),
                "가격": lambda x: random.randint(1, 300),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        houoserules = room_models.Houoserule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(1, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1,31)}.webp",
                    room=room,
                )

            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.편의시설.add(a)

            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.부대시설.add(f)

            for h in houoserules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.사용규칙.add(h)

        self.stdout.write(self.style.SUCCESS(f"{number}완료"))
