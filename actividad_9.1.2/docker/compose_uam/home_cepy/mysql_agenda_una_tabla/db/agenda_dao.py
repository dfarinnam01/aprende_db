import logging
from .database import Database


class AgendaDao:
    logger = logging.getLogger(__name__)
    table_name = "contactos"

    SELECT = f"""
        SELECT id, nombre,telefono,email,localidad
        FROM {table_name}
    """

    def add(self, contactos: dict) -> int:
        sql = f"INSERT INTO {self.table_name} (nombre,telefono,email,localidad) VALUES (%s,%s,%s,%s)"

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                contactos.get('nombre'),
                contactos.get('telefono'),
                contactos.get('email'),
                contactos.get('localidad')
            ))
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            conn.rollback()
            self.logger.exception(f"Error al insertar el contacto: {e}")
            return -1

        finally:
            if cursor:
                cursor.close()

    def add_list(self, contactos: list[dict]) -> int:
        if not contactos:
            return 0

        sql = f"INSERT INTO {self.table_name} (nombre,telefono,email,localidad) VALUES (%s,%s,%s,%s)"

        datos = [
            (
                contacto.get('nombre'),
                contacto.get('telefono'),
                contacto.get('email'),
                contacto.get('localidad')
             )
            for contacto in contactos
        ]

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.executemany(sql, datos)
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al insertar lista de contactos")
            return 0

        finally:
            if cursor:
                cursor.close()

    def get(self, id: int) -> dict:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"{self.SELECT} WHERE id = %s", (id,))
            return cursor.fetchone()

        except Exception:
            self.logger.exception("Error al obtener contacto")
            return None

        finally:
            if cursor:
                cursor.close()

    def get_all(self) -> list:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(self.SELECT)
            return cursor.fetchall()

        except Exception:
            self.logger.exception("Error al obtener contactos")
            return []

        finally:
            if cursor:
                cursor.close()

    def get_by_telefono(self,telefono:str):
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"{self.SELECT} WHERE telefono = %s", (telefono,))
            return cursor.fetchone()

        except Exception:
            self.logger.exception("Error al obtener contacto")
            return None

        finally:
            if cursor:
                cursor.close()

    def get_by_nombre(self,nombre:str):
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"{self.SELECT} WHERE nombre = %s", (nombre,))
            return cursor.fetchall()

        except Exception:
            self.logger.exception("Error al obtener contacto")
            return None

        finally:
            if cursor:
                cursor.close()

    def delete(self, id: int) -> int:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE id = %s", (id,))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al eliminar contacto")
            return -1

        finally:
            if cursor:
                cursor.close()

    def update(self, id: int, contacto: dict) -> int:
        sql = f"UPDATE {self.table_name} SET nombre=%s,telefono=%s,email=%s,localidad=%s WHERE id=%s"

        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(sql, (
                contacto.get('nombre'),
                contacto.get('telefono'),
                contacto.get('email'),
                contacto.get('localidad'),
                id
            ))
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            self.logger.exception("Error al actualizar contacto")
            return -1

        finally:
            if cursor:
                cursor.close()


    def telefonos_by_nombre(self,nombre:str):
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT telefono FROM {self.table_name} WHERE nombre = %s", (nombre,))
            return cursor.fetchall()

        except Exception:
            self.logger.exception(f"Error al obtener los telefonos por el nombre: {nombre}")
            return None

        finally:
            if cursor:
                cursor.close()
    def numero_telefonos_contactos(self) -> list[tuple]:
        conn = Database.connect()
        cursor = None

        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT nombre, COUNT(telefono) AS numero_contactos FROM {self.table_name} GROUP BY nombre")
            return cursor.fetchall()

        except Exception:
            self.logger.exception(f"Error al obtener los telefonos ")
            return None

        finally:
            if cursor:
                cursor.close()