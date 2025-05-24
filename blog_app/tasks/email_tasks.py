from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(username):
    time.sleep(5)  # simulate delay
    logger.info(f"Welcome email sent to {username}")
    return True
