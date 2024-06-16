import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message) s:')
logging.info("Welcome to GEN AI")
file_list = [
    'src/__init__.py', 
    'src/helper.py',
    'src/prompt.py'
    '.env',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'app.py'
]

for filepath in file_list:
   filepath = Path(filepath)
   dir, filename = os.path.split(filepath)
   if dir!="":
      if not os.path.exists(dir):
         os.makedirs(dir)
         logging.info(f"created directory {dir}")
      if not os.path.exists(filepath):
         with open(filepath, 'w') as f:
            f.write("")
            logging.info(f"created file {filepath}")
      else:
         logging.info(f"file {filepath} already exists") 

