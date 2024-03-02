from multiprocessing.spawn import import_main_path
from .celery import app as celery_app
__all__ = ("celery_app", )