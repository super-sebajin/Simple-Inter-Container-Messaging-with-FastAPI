# Simple Inter-Container Messaging with FasAPI

This is a simple docker-compose project designed to be a proof of concept of a simple messaging service between two containerized `FastApi` applications. This project came into fruition from a simple `docker init`. Using available resources, and in efforts to learn how to develop containerized apps, this project was created.

What this project does is quite simple. Each container `FastAPI` app contains a `GET` and a `POST` endpoint(s). A container A will receive a `POST` request with a "message" payload, and will make a `GET` request the container B's `GET` method.

This is done to serve as a base for reference for future service based architectural projects in the future.

## Requirements
- Docker engine 
- Docker compose
- Python (optional to debug the python code locally)

## How to start the project:
This project assumes you have `docker` and `docker-compose` installed in your system. If you don't have them install please refer to the documentation:
- https://docs.docker.com/get-docker/
- https://docs.docker.com/compose/install/

Before running the project, please rename `.env.example` to `.env` . This file is included in the `.gitignore` file for security reasons, but an example file is provided so that users that wish to experiment with the project can have a sense of where things are coming from.

Apart from the above, all that is needed to start running the project is to have a terminal in the project's root directory and execute `docker-compose up` with any relevant options. I like to use the `-d` option so that the orchestrator leaves the current terminal session alone.

## Inter-container messaging
The project consists of services `app1` and `app2`. They are both generated from the same `Dockerfile`. Each container contains a `FastAPI` app that contains two endpoints: a `GET` (this get is from the `FastAPI` documentation itself) and a `POST` method. The `POST` method will receive a request with a json body that will contain:
    - A payload (semantics of this text field is user-based)
    - App name: has a general format, it goes according to what has been set up in the .env file
    - App Port: The same semantics as App name above.

In the project's files, you will find a file called `message_examples.txt`, notice that in the examples file, we have `json` strings that refer to the variables defined in the `.env` or `.end.example` file. You can see this behavior by looking at `api.py` in conjunction with `messages.py`. Also, for easy reference, they are denoted too.

Then, to have `app1` message `app2` and vice-versa, just use the appropriate `json` string in the `message_examples.txt`. 

You can use a tool like Postman or the containers' own Swagger UIs to test it out.

# Updates:

- 2024-08-2024 - Added and defaulted to bash activation with `bash app_run/commands/startapi.pl`.

