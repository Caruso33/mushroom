import os


def get_images(types, images_per_type=50):
    print(f"Start downloading types")

    for (ind, typ) in enumerate(types):
        search_term = typ

        print(f"{ind} / {len(types)} >> Start downloading: {search_term}")

        cmd = f"""python utils/bing_scraper.py \
        --search '{search_term}' \
        --limit {images_per_type} \
        --download \
        -o data/images \
        --chromedriver ~/Downloads/chromedriver"""

        os.system(cmd)

    print(f"Finished downloading types")
