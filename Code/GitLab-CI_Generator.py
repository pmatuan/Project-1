import yaml


def generate_gitlab_ci_yml():
    stages = [
        "test",
        "build",
        "deploy"
    ]
    run_test = {
        "stage": "test",
        "image": "python:3.9-slim-buster",
        "before_script": [
            "apt-get update && apt-get install make"
        ],
        "script": [
            "make test"
        ]
    }
    build_image = {
        "stage": "build",
        "image": "docker:20.10.16",
        "services": [
            "docker:20.10.16-dind"
        ],
        "variables": {
            "DOCKER_TLS_CERTDIR": "/certs"
        },
        "before_script": [
            "docker login -u $USER -p $PASS"
        ],
        "script": [
            "docker build -t pmatuan/demo-app-python:v1 .",
            "docker push pmatuan/demo-app-python:v1"
        ]
    }
    deploy = {
        "stage": "deploy",
        "before_script": [
            "chmod 400 $SSH_KEY"
        ],
        "script": [
            "ssh -o StrictHostKeyChecking=no -i $SSH_KEY pmat@20.187.72.154 \"docker login -u $USER -p $PASS && docker run -d -p 5000:5000 pmatuan/demo-app-python:v1\""
        ]
    }
    ci_config = {
        "stages": stages,
        "run_test": run_test,
        "build_image": build_image,
        "deploy": deploy
    }
    ci_config_ymp = yaml.dump(ci_config)
    with open(".gitlab-ci.yml", "w") as f:
        f.write(str(ci_config_ymp))


if __name__ == "__main__":
    generate_gitlab_ci_yml()