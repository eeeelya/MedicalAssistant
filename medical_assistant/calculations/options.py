import json
import numpy as np
import botocore.exceptions

from calculations.preprocessing import SegmentationPreprocessing
from calculations.utils import start_segmentation, save_results


def segmentation(model, image_name):
    data = dict()

    segm_proc = SegmentationPreprocessing(img_name=image_name)

    try:
        segm_proc.save_image()
    except (TypeError, ValueError) as error:
        data["error"] = f"Error - {error}"
        # TODO: add record to history
        return data, 400

    try:
        source_image = segm_proc.preprocessing()
    except OSError as err:
        data["error"] = f"Error - {err}"
        # TODO: add record to history
        return data, 400

    try:
        result = start_segmentation(model, source_image)
    except botocore.exceptions.ConnectionClosedError as err:
        data["error"] = f"Error - {err}"
        # TODO: add record to history
        return data, 400

    if "body" in result.keys():
        resp = json.loads(result["body"])
        masks = np.asarray(resp, dtype=np.float32)

        masks_mapping = {}
        for index, mask in enumerate(masks[0]):
            masks_mapping[segm_proc.LABELS[index]] = segm_proc.mask_to_image(mask)

        mask = segm_proc.masks_to_one_mask(masks_mapping)

        s3_url = save_results(mask, segm_proc.img_name)
        data["s3_url"] = s3_url

        # TODO: add record to history
        return data, 200
    else:
        # TODO: add record to history
        data["error"] = result["errorMessage"]
        return data, 400

