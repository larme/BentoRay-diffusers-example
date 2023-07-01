import bentoml
bentoml.set_serialization_strategy("LOCAL_BENTO")

deploy = bentoml.ray.deployment(
    "stable-diffusion-21:latest",
    {"num_replicas": 3, "ray_actor_options": {"num_cpus": 1}},
    {
        "sd21-runner": {
            "num_replicas": 1,
            "ray_actor_options": {"num_cpus": 4, "num_gpus": 1},
        }
    },
)
