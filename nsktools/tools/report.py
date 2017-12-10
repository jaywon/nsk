from .tool import Tool

class report(Tool):
    def __init__(self, verbose):
        Tool.__init__(self, verbose)

        if verbose:
            print('sysinfo')

    def __str__(self):
        return "report: " + verbose

    def __repr__(self):
        return "report(" + verbose + ")"

    def __del__(self):
        print ("Destroying report Instance")
