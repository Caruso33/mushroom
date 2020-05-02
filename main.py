#!/usr/bin/python

from fastai.vision import Path
# from utils.get_classes import get_class_names
from os import path
import sys
from development import run_development
from production import run_production


# from fastai.vision import (
#     ImageDataBunch,
#     ConvLearner,
#     open_image,
#     get_transforms,
#     models,
#     load_lerner
# )
# import torch


def get_learner(images_path, learner_filepath):

    # class_names = get_class_names(images_path)

    # data_bunch = ImageDataBunch.from_name_re(
    #     images_path,
    #     class_names,
    #     r"/([^/]+)_\d+.jpg$",
    #     ds_tfms=get_transforms(),
    #     size=224,
    # )

    # learner = ConvLearner(data_bunch, models.resnet34)
    # learner.model.load_state_dict(
    #     torch.load(learner_filepath, map_location="cpu")
    # )
    # learner = load_learner(learner_filepath)
    # return learner
    return


def main():
    mode = ""

    data_path = Path('data')
    images_path = path.join(data_path, 'images')
    learner_filepath = path.join(data_path, 'export.pkl')

    if len(sys.argv) != 2:
        raise ValueError('Please provide mode')
    mode = sys.argv[1]

    # learner = get_learner(images_path, learner_filename)

    if mode == 'development':
        run_development(data_path, images_path, learner_filepath)

    elif mode == 'production':
        run_production(learner_filepath)


if __name__ == '__main__':
    main()
