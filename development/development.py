from os import path, listdir
from os.path import join, isdir
import sys
from pprint import pprint

from development import get_names, get_images, train_model


def data_sanity_check(images_path, images_per_type):
    if not path.exists(images_path):
        return False

    dir_paths = [d for d in listdir(
        images_path) if isdir(join(images_path, d))]

    if len(dir_paths) == 0:
        return False

    data_hist = {}
    data_errors = {}

    for dir in dir_paths:
        data_hist[dir] = len(listdir(path.join(images_path, dir)))

    for key, value in data_hist.items():
        if value < images_per_type:
            data_errors[key] = images_per_type - value

    if data_errors:
        pprint(f"Missing images per type: {data_errors}")

        # get_images(data_errors.keys(), images_per_type)

        return False

    return True


def prepare_data(data_path, images_per_type):
    names = get_names(data_path)

    print(f"Got {len(names)} name spaces.")

    for namespace in names:
        search_terms = []

        for types in namespace['data']:
            search_terms = [typ['common'] for typ in types]

        get_images(search_terms, images_per_type)


def run_development(data_path, images_path, learner_filepath):
    images_per_type = 50

    if not data_sanity_check(images_path, images_per_type):
        print('Data sanity check not successful')
        sys.exit(1)
        learn = train_model(images_path)
    # prepare_data(data_path, images_per_type)

    if not path.isfileexists(learner_filepath):
        learn.export(learner_filepath)
