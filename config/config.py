from collections import Mapping, Sequence
import os
import yaml, json


class Config:

    def __init__(self, config_path: str):
        """ Initialize a new instance of Config """
        self._config_path = config_path
        if os.path.isfile(self._config_path) and os.access(self._config_path, os.R_OK):
            with open(self._config_path, 'r') as stream:
                try:
                    self._config = yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            raise FileNotFoundError

    def _get(self, key):
        """ internal implementation of get """
        current_data = self._config

        for chunk in key.split('.'):
            if isinstance(current_data, Mapping):
                current_data = current_data[chunk]
            elif isinstance(current_data, Sequence):
                chunk = int(chunk)

                current_data = current_data[chunk]
            else:
                return current_data

        return current_data

    def get(self, key, default=None, default_none=False):
        """ return the configs for the passed key """
        try:
            return self._get(key)
        except KeyError:
            if default is None and not default_none:
                raise KeyError(key)
            else:
                return default
        except ValueError:
            raise ValueError("Sequence index not an integer")
        except IndexError:
            raise IndexError("Sequence index out of range")

def try_convert_number(inp):
    """ Tries to convert input to a number if it is a string"""
    if isinstance(inp, str):
        try:
            to_return = int(inp)
        except:
            try:
                to_return = float(inp)
            except:
                to_return = inp
        return to_return
    else:
        return inp
