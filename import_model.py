import bentoml

bentoml.diffusers.import_model(
    "sd2.1",  # model tag in BentoML model store
    "stabilityai/stable-diffusion-2-1",  # huggingface model name
)
