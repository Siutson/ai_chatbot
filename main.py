import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.python.keras.models import load_model

lemmatizer = WordNetLemmatizer()

with open ("intents.json", 'r', encoding='utf8') as f:
    intents = json.load(f)