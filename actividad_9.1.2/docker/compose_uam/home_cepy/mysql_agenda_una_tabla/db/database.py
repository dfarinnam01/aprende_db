# database.py
import logging
import pymysql
import json
from .cepy_spinner import CepySpinner

class Database:
    logger = logging.getLogger(__name__)
    _conn = None
    _config = None

    @classmethod
    def _load_config(cls):
        if cls._config is None:
            cls.logger.info("Cargando configuración desde config_db.json")

            try:
                with open("db/config_db.json", "r", encoding="utf-8") as f:
                    cls._config = json.load(f)

                # Ajustes recomendados para PyMySQL
                cls._config.setdefault("cursorclass", pymysql.cursors.DictCursor)
                cls._config.setdefault("autocommit", True)

            except Exception as e:
                cls.logger.critical(f"Error al cargar config_db.json: {e}")
                raise

    def __new__(cls):
        raise TypeError("Database es un singleton. No se puede instanciar Database")

    @classmethod
    def _is_connected(cls):
        try:
            cls._conn.ping(reconnect=False)
            return True
        except Exception:
            return False

    @classmethod
    def connect(cls):
        try:

            if cls._conn is None:
                cls._load_config()
                cls.ceppy_spinner = CepySpinner(message="Conectando a la BD", type=3)
                cls.ceppy_spinner.start()
                cls.logger.info("Creando nueva conexión a MySQL (PyMySQL)")
                cls._conn = pymysql.connect(**cls._config)
                cls.ceppy_spinner.stop()
            elif not cls._is_connected():
                cls.logger.warning("Conexión perdida. Recreando conexión...")
                try:
                    cls._conn.close()
                except Exception:
                    pass

                cls._conn = pymysql.connect(**cls._config)

            return cls._conn

        except Exception as e:
            cls.logger.critical(f"Error al conectar a la base de datos: {e}")
            cls._conn = None
            raise

    @classmethod
    def close(cls):
        if cls._conn:
            try:
                cls._conn.close()
            finally:
                cls._conn = None