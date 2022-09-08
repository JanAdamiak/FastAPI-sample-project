# Sample FastAPI project
This repository is a hobby project, that serves as a way to learn FastAPI.
I will additionally try to pick-up a few more technologies in this project.
All of them will be listed below.

## Running the project
To run the project locally you have to [install Docker on your machine] (https://docs.docker.com/get-docker/).

Then you can try building the Docker image by using:
`sudo docker build . -t myapp`

And running the Docker image with:
`sudo docker run myapp`

If no issues were present the server should be running on http://0.0.0.0:80

## Running the tests
To run the tests locally you have to ensure you have the environment setup with all the dependencies downloaded.
Then you can call: 
`pytest`