#!/bin/bash
cd ./backend/app
poetry export --without-hashes --format=requirements.txt > requirements.txt
