from os import path
from fastai.metrics import error_rate
from fastai.vision import (
    models, ImageDataBunch, ClassificationInterpretation, get_transforms, get_image_files, imagenet_stats, cnn_learner)


def load_images(images_path):
    print(images_path.ls())

    data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
                                      ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)
    print(data.classes)

    data.show_batch(rows=3, figsize=(7, 8))

    print(data.classes)
    print(data.c)
    print(len(data.train_ds))
    print(len(data.valid_ds))

    return data


def train_model(images_path):
    bs = 64

    data = load_images(images_path)

    learn = cnn_learner(data, models.resnet34, metrics=error_rate)

    learn.fit_one_cycle(4)
    learn.save('stage-1')

    # learn.load('stage-1')

    learn.unfreeze()
    learn.lr_find()
    learn.recorder.plot()

    learn.fit_one_cycle(2, max_lr=slice(3e-5, 3e-4))
    learn.save('stage-2')

    # learn.load('stage-2')

    interp = ClassificationInterpretation.from_learner(learn)

    interp.plot_confusion_matrix()
    
    return learn
