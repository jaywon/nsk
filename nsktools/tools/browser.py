from .tool import Tool

class browser(Tool):
    def __init__(self, verbose):
        Tool.__init__(self, verbose)

        if verbose:
            print('browser')

    def __str__(self):
        return "browser " + verbose

    def __repr__(self):
        return "browser(" + verbose + ")"

    def __del__(self):
        print ("Destroying browser Instance")
