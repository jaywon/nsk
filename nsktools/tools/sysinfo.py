from .tool import Tool
import socket

class sysinfo(Tool):
    def __init__(self, verbose):
        if verbose:
            print('initializing sysinfo')

        Tool.__init__(self, verbose)

        self.gethostname()

    def gethostname(self):
        if self._verbose:
            print('getting system hostname')

        host_name = socket.gethostname()
        print("The hostname is: ", host_name)

    def __str__(self):
        return "sysinfo: " + str(self._verbose)

    def __repr__(self):
        return "sysinfo(" + str(self._verbose) + ")"

    def __del__(self):
        if self._verbose:
            print ("Destroying sysinfo Instance")
