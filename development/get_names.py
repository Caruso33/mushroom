import requests
from bs4 import BeautifulSoup
import json
import os
import re
from types import SimpleNamespace


sources = [{
    'source_tag': 'mushroomworld',
    'url': "https://www.mushroom.world/mushrooms/namelist",
    'common_selector': "small",
    'scientific_selector': "#name-list a"
}, {
    'source_tag': 'wildfood',
    'url': "https://www.wildfooduk.com/mushroom-guide/",
    'common_selector': "td:nth-child(2) a",
    'scientific_selector': ".spotlight-text a"
}]


def get_names(data_path):
    names = []

    for src in sources:
        src = SimpleNamespace(**src)

        path = path.join(data_path, f"{src.source_tag}.json")

        try:
            with open(path, 'r') as file:
                types = json.load(file)
                print(
                    f'successfully loaded {len(types)} types from {src.source_tag}')
                names.append({'origin': src.source_tag, 'data': types})

        except FileNotFoundError:
            page = requests.get(src.url)
            soup = BeautifulSoup(page.content, 'html.parser')

            common_names = soup.select(src.common_selector)
            scientific_names = soup.select(src.scientific_selector)

            type_tuples = zip(common_names, scientific_names)

            types = []

            counter = 0
            for (common, scientific) in type_tuples:

                types.append({
                    'common':  re.sub('[\n\(\)]', '', common.text.strip()),
                    'scientific':  re.sub('[\n\(\)]', '', scientific.text.strip())
                })

                counter += 1

            if not os.path.exists(data_path):
                os.makedirs(data_path)

            with open(path, 'w') as file:
                json.dump(types, file)

            print(f'successfully saved {counter} types from {src.source_tag}')
            names.append({'origin': src.source_tag, 'data': types})

        except Exception as e:
            print(f"Unknown error occured {e}")

    return names
