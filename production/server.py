import os
import sys
import torch
import uvicorn

from routes import upload, classify_url, form, redirect_to_homepage
from starlette.applications import Starlette
from starlette.routing import Route


app = Starlette(debug=True, routes=[
    Route("/", form, methods=['GET']),
    Route("/upload", upload, methods=["POST"]),
    Route("/classify-url", classify_url, methods=["GET"]),
    Route("/form", redirect_to_homepage, methods=["GET"])
])

if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run('server:app', host="0.0.0.0",
                    port=os.environ.get('PORT') or 8008)
    elif 'dev' in sys.argv:
        uvicorn.run('server:app', host="0.0.0.0", port=8008, reload=True)
