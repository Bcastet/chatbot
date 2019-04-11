#!/bin/bash

# Entrainement 1
python3 ~/chatbot/Libs/Python/End2end_maker.py
python3 -m rasa_core.evaluate default --core models/dialogue --nlu models/current/nlu --stories e2e_stories.md --e2e
python3 ~/chatbot/Libs/Python/Score_reader.py
