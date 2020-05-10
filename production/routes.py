from io import BytesIO
import sys
import asyncio

import aiohttp
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastai.vision import open_image, Path, load_learner

learn = load_learner('.', 'export.pkl')


async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def upload(request):
    data = await request.form()
    if not data or len(data) == 0:
        return JSONResponse({"error": True, "predictions": []})

    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)


async def classify_url(request):
    bytes = await get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)


def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))

    pred_class, pred_idx, losses = learn.predict(img)

    return JSONResponse({
        "error": False,
        "predictions": sorted(
            zip(learn.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True
        ),
    })


def form(request):
    return HTMLResponse(
        """
        Select image to upload:
        <form action="/upload" method="post" enctype="multipart/form-data">
            <br />
            <input type="file" name="file">
            <input type="submit" value="Upload Image">
        </form>
        <br />
        Or submit a URL:
        <br />
        <form action="/classify-url" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
    """)


def redirect_to_homepage(request):
    return RedirectResponse("/")
