from .tool import Tool
import urllib2
import json
import codecs

class maclookup(Tool):
    def __init__(self, verbose):
        if verbose:
            print('initializing maclookup')

        Tool.__init__(self, verbose)

        self.mac_address_scan()

    def mac_address_scan(self):
        if self._verbose:
            print('Starting mac address scan')

        url = 'http://macvendors.co/api/'
        mac_address = input('Enter MAC Address To Search: ')

        request = urllib.request.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
        response = urllib.request.urlopen(request)

        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))

        print ('=' * 40)
        print (obj['result']['company']);
        print (obj['result']['address']);
        print ('=' * 40)

    def __str__(self):
        return "maclookup " + verbose

    def __repr__(self):
        return "maclookup(" + verbose + ")"

    def __del__(self):
        print ("Destroying maclookup Instance")
