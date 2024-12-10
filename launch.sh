#!/bin/bash

python3 -m venv .venv
echo "source .venv/bin/activate"

pip install mocodo

python main.py
