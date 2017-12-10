from .tool import Tool

class ipmap(Tool):
    def __init__(self, verbose):
        Tool.__init__(self, verbose)

        if verbose:
            print('ipmap')

    def __str__(self):
        return "ipmap " + verbose

    def __repr__(self):
        return "ipmap(" + verbose + ")"

    def __del__(self):
        print ("Destroying ipmap Instance")
