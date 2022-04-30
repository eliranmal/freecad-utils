# -*- coding: utf-8 -*-

import os
import json
import FreeCAD
from pathlib import Path
from json.decoder import JSONDecodeError


def json_as_dict(json_str):
  try:
    input_dict = json.loads(json_str)
  except JSONDecodeError:
    input_dict = dict()
  return input_dict

def load_options(defaults_dict = {}):
  """
  loads a json string from the document comment field, and returns it as a dict.
  """
  user_options = load_json_as_dict(FreeCAD.ActiveDocument.Comment)
  return {**defaults_dict, **user_options}
