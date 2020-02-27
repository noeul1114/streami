#!/usr/bin/env bash
xhost +local:

sudo docker container run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY willypower/streami:latest bash
