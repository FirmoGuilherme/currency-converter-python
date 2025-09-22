import os
import logging


def setup_logging():
	logging.basicConfig(level=logging.INFO)
	logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
	logging.getLogger("pg_catalog.pg_class").setLevel(logging.WARNING)


def get_logger(file_name: str):
	return logging.getLogger(
		file_name.split("/" if "/" in file_name else "\\")[-1].strip(".py")
	)