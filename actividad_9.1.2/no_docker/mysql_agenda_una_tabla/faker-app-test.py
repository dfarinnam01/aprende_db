import random
import logging
from faker import Faker

from db.agenda_dao import AgendaDao
from utils.cepy_progress_printer import CepyProgressPrinter

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] [%(name)s] %(message)s',
    filename='errores.log',
    filemode='a',
    encoding='utf-8'
)

fake = Faker("es_ES")

# DAO
agenda_dao = AgendaDao()

# ======================================
# CONFIG
# ======================================
TOTAL_CONTACTOS = 100

progress = CepyProgressPrinter(msg="Generando contactos:", total=TOTAL_CONTACTOS)

# Para evitar teléfonos duplicados (IMPORTANTÍSIMaO por UNIQUE)
telefonos_usados = set()

def generar_telefono_unico():
    while True:
        telefono = str(random.choice([6, 7])) + "".join(
            [str(random.randint(0, 9)) for _ in range(8)]
        )
        if telefono not in telefonos_usados:
            telefonos_usados.add(telefono)
            return telefono

# ======================================
# GENERAR CONTACTOS
# ======================================
for i in range(1, TOTAL_CONTACTOS + 1):

    contacto = {
        "nombre": fake.name(),
        "telefono": generar_telefono_unico(),
        "email": fake.email(),
        "localidad": fake.city()
    }

    resultado = agenda_dao.add(contacto)

    if resultado == -1:
        logging.warning(f"No se pudo insertar: {contacto}")

    progress.update(i)

progress.check_finish()