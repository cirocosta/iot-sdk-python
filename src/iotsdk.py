import urllib2
import urllib
import json


class Iot(object):
    """ Wrapper for the IOT api """

    BASE_PATH = 'http://dca.telefonicabeta.com/m2m/v2/'
    
    def __init__(self, token):
        self.token = token
        self._buildEndpointsRoute()

    def _buildEndpointsRoute(self):
        self._ENDPOINTS_ROUTE = {
            "service_details": "services/%s" % (self.token,),
            "asset_details": "services/%s/assets" % (self.token,),
            "asset_history": "services/%s/assets/%s" % (self.token, self.token) 
        }
        return self._ENDPOINTS_ROUTE    

    def _buildQuery(self, arguments=dict()):   
        return urllib.urlencode(arguments)

    def _buildPath(self, code, query=""):
        return self.BASE_PATH + self._ENDPOINTS_ROUTE[code] + query

    def _parseJsonFromUrl(self, url):
        response = ""
        try:
            response = urllib2.urlopen(url).read()
        except:
            pass
        if response:
            return json.loads(response)
        return None

    def get_services_details(self):
        url = self._buildPath("service_details")
        return self._parseJsonFromUrl(url)

    def get_connected_devices(self):
        url = self._buildPath("asset_details")
        return self._parseJsonFromUrl(url)

    def get_device_data(self):
        url = self._buildPath("asset_history")
        return self._parseJsonFromUrl(url)
