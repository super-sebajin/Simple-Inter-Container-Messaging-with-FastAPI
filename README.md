# Simple Inter-Container Messaging with FasAPI

This is a simple docker-compose project designed to be a proof of concept of a simple messaging service between two containerized `FastApi` applications. This project came into fruition from a simple `docker init`. Using available resources, and in efforts to learn how to develop containerized apps, this project was created.

What this project does is quite simple. Each container `FastAPI` app contains a `GET` and a `POST` endpoint(s). A container A will receive a `POST` request with a "message" payload, and will make a `GET` request the container B's `GET` method.

This is done to serve as a base for reference for future service based architectural projects in the future.