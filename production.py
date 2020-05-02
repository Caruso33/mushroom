import torch
from fastai.core import defaults
import uvicorn

from production.routes import upload, classify_url, form, redirect_to_homepage
from starlette.applications import Starlette
from starlette.routing import Route


def run_production():
    defaults.device = torch.device('cpu')

    app = Starlette(debug=True, routes=[
        Route("/", form, methods=['GET']),
        Route("/upload", upload, methods=["POST"]),
        Route("/classify-url", classify_url, methods=["GET"]),
        Route("/form", redirect_to_homepage, methods=["GET"])
    ])

    uvicorn.run(app, host="0.0.0.0", port=8008)


if __name__ == '__main__':
    run_production()
