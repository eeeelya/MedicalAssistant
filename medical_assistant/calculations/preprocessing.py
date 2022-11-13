import os
from typing import Dict

import boto3
import botocore.exceptions
import cv2
import numpy as np
from PIL import Image

from medical_assistant.settings import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME


class SegmentationPreprocessing:
    LABELS = [
        "Gallblader",
        "Background",
        "Gastrointestinal Tract",
        "Fat",
        "Grasper",
        "Cystic Duct",
        "L-hook Electrocautery",
    ]

    def __init__(self, img_name) -> None:
        self.img_name = img_name
        self.img_height = None
        self.img_width = None

    def save_image(self) -> None:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION,
        )
        try:
            object_from_s3 = s3.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=self.img_name)
            response = object_from_s3["Body"]
        except botocore.exceptions.ClientError:
            raise ValueError(f"There is no such image with name {self.img_name}")

        image = Image.open(response)

        self.img_width = image.size[0]
        self.img_height = image.size[1]

        if image.format != "PNG":
            raise TypeError("File extension must be .png!")

        if self.img_width != 854 or self.img_height != 480:
            raise ValueError("File size must be 480x854!")

        image.save(self.img_name)

    def preprocessing(self) -> np.ndarray:
        image = cv2.imread(self.img_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, dsize=(256, 256), interpolation=cv2.INTER_NEAREST)

        mean = 255 * np.array([0.485, 0.456, 0.406])
        std = 255 * np.array([0.229, 0.224, 0.225])
        image = image.transpose(-1, 0, 1)
        image = (image - mean[:, None, None]) / std[:, None, None]
        normalized_image = np.expand_dims(image, 0).astype(np.float32)

        return normalized_image

    @staticmethod
    def mask_to_image(mask) -> Image.Image:
        mask = cv2.resize(mask, (854, 480), interpolation=cv2.INTER_NEAREST)
        mask = mask.reshape(480, 854, 1).astype(np.float32)

        return mask

    def masks_to_one_mask(self, masks: Dict[str, Image.Image]) -> Image.Image:
        masks_colors = {
            "Gallblader": (90, 79, 207),
            "Background": (210, 141, 141),
            "Gastrointestinal Tract": (254, 75, 114),
            "Fat": (255, 140, 0),
            "Grasper": (171, 254, 0),
            "Cystic Duct": (239, 254, 75),
            "L-hook Electrocautery": (169, 255, 184),
        }

        new_mask = (np.full((480, 854, 3), masks_colors["Background"]),)
        for mask_key in masks:
            mask = np.asarray(masks[mask_key]).reshape(480, 854, 1)
            new_mask = np.where(mask == 1, masks_colors[mask_key], new_mask)

        image = cv2.imread(self.img_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = cv2.addWeighted(image.reshape(480, 854, 3), 0.55, np.uint8(new_mask.reshape(480, 854, 3)), 0.45, 0)

        os.remove(self.img_name)

        return Image.fromarray(result)
