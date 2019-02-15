#!/bin/bash

# Entrainement 1
python End2end_maker.py
python -m rasa_core.evaluate default --core models/dialogue --nlu models/current/nlu --stories e2e_stories.md --e2e
python Score_reader.py
