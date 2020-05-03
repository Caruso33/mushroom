import sys
import torch
# from fastai import Path
# from fastai.core import defaults
import uvicorn

from production.routes import upload, classify_url, form, redirect_to_homepage
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

# export_file_url = 'https://drive.google.com/uc?export=download&id=1-FMZZkM4BMTS_EJh4f-DnW1uYx__suoa'
# export_file_name = 'export.pkl'

# path = Path(__file__).parent

# async def download_file(url, dest):
#     if dest.exists(): return
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.read()
#             with open(dest, 'wb') as f:
#                 f.write(data)

# async def setup_learner():
#     await download_file(export_file_url, path / export_file_name)
#     try:
#         learn = load_learner(path, export_file_name)
#         return learn
#     except RuntimeError as e:
#         if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
#             print(e)
#             message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
#             raise RuntimeError(message)
#         else:
#             raise


def run_production():
    # defaults.device = torch.device('cpu')

    app = Starlette(debug=True, routes=[
        Route("/", form, methods=['GET']),
        Route("/upload", upload, methods=["POST"]),
        Route("/classify-url", classify_url, methods=["GET"]),
        Route("/form", redirect_to_homepage, methods=["GET"])
    ])
    app.add_middleware(CORSMiddleware, allow_origins=[
                       '*'], allow_headers=['Content-Type'])
    app.mount('/static', StaticFiles(directory='app/static'))

    uvicorn.run(app, host="0.0.0.0", port=8008)


if __name__ == '__main__':
    if 'serve' in sys.argv:
        run_production()
