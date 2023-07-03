Codes to deploy a stable diffusion bento to RayServe. Example of Ray forward 2023.

## Setup the environment and import the model

`python3 -m venv venv && . venv/bin/activate && pip install -U pip && pip install -r requirements.txt`

then

`python import_model.py`

Run `bentoml models list` to check the newly imported model.

## Run BentoML service

`bentoml serve service:svc`

Visit <http://127.0.0.1:3000> to view BentoML api page. Or run `txt2img_test.sh` in terminal to generate an image from command line.

## Build a bento

Run `bentoml build`, then `bentoml list` to view the newly built bento.

## Deploy the bento to RayServe

Run `serve run ray_deploy:deploy -p 3000`. Again you can run `txt2img_test.sh` to generate an image.
