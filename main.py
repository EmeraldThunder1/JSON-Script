import json
import sys

from commands import *
from errors import *

file = "main.json"

try:
    with open(file, 'r') as f:
        file_data = json.load(f)
        f.close()
except IOError:
    raise FileNotFoundException()

instructions = file_data['instructions']

run_code(instructions)