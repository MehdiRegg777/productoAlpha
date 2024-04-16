from django.core.management.base import BaseCommand
from faker import Faker
from faker_vehicle import VehicleProvider
from myapp.models import Producto

fake = Faker()
fake.add_provider(VehicleProvider)

class Command(BaseCommand):
    help = 'Crea productos ficticios'

    def handle(self, *args, **options):
        self.create_fake_productos()

    def create_fake_productos(self):
        print("Creando productos ficticios...")
        for _ in range(10):  # Crear 10 productos ficticios
            producto = Producto(
                nombre=fake.vehicle_make_model(),  # Genera un nombre de vehículo
                descripcion=fake.sentence(nb_words=10),  # Genera una descripción corta
                precio=fake.random_number(digits=5) # Para tener un precio decimal
            )
            producto.save()
        print("Productos ficticios creados.")
