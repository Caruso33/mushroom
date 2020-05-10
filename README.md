# Mushroom classifier based on [fastai](https://fast.ai)

## Tools

- Docker
- fastai / pyTorch
- Starlette

## Run

`docker build .`

`docker run -p 80:8008 -t star`
_\*OR\*_
`docker-compose up`

[localhost](http://0.0.0.0:80)

## Deploy to heroku

```
heroku login
heroku container:login
heroku create
heroku git:remote -a `name of heroku app`
heroku container:push web
heroku container:relase web
heroku open
```

## Debug

`heroku logs --tail`
