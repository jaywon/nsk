from .tool import Tool
import json
import urllib.request
import codecs

class portscan(Tool):
    def __init__(self, verbose):
        Tool.__init__(self, verbose)
        self._verbose = verbose
        if verbose:
            print('intitializing portscan')

    def __repr__(self):
        return "portscan(" + verbose + ")"

    def __del__(self):
        print ("Destroying portscan Instance")
