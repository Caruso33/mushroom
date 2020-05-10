from os import path, listdir
from os.path import join, listdir
from fastai.vision import Path

def get_class_names(data_directory):
   image_path = Path(f"{data_directory}/images")

   if not path.exists():
        raise FileExistsError("No image folder")

   class_names = [d for d in listdir(image_path) if listdir(join(image_path, d))]

   return class_names
