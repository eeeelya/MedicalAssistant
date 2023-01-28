from celery import shared_task

from calculations.options import segmentation


@shared_task
def run_launch(*args, **kwargs):
    model = kwargs.get("model")
    image = kwargs.get("image")

    data, status = segmentation(model, image)

    return data, status
