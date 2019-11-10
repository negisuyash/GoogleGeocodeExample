import urllib.request as urllib
import json


class GeocodeAPI:

    API_KEY = ""
    GClient_BaseURL = "https://maps.googleapis.com"
    GClient_PlaceInfoURL="/maps/api/geocode"
    GClient_AddressParameter="?address="
    GClient_xmlFormatInfo="/xml"
    GClient_jsonFormatInfo = "/json"

    def __init__(self,API):
        self.API_KEY=API

    def getGeocode(self,address):

        jsonData = json.loads(urllib.urlopen(self.GClient_BaseURL+ self.GClient_PlaceInfoURL+ self.GClient_jsonFormatInfo+ self.GClient_AddressParameter + address.replace(' ','+') + "&key=" + self.API_KEY).read())
        lat=jsonData['results'][0]['geometry']['location']['lat']
        lng=jsonData['results'][0]['geometry']['location']['lng']
        return lat,lng

    def getPlaceId(self,address):
        jsonData = json.loads(urllib.urlopen(self.GClient_BaseURL+ self.GClient_PlaceInfoURL+ self.GClient_jsonFormatInfo+ self.GClient_AddressParameter + address.replace(' ', '+') + "&key=" + self.API_KEY).read())
        return jsonData['results'][0]['place_id']

    def sendResponse(self,address,isXML=False):
        if isXML is True:
            return urllib.urlopen(
                self.GClient_BaseURL + self.GClient_PlaceInfoURL+ self.GClient_xmlFormatInfo+ self.GClient_AddressParameter + address.replace(' ', '+') + "&key=" + self.API_KEY).read()
        return urllib.urlopen(
                self.GClient_BaseURL + self.GClient_PlaceInfoURL+ self.GClient_jsonFormatInfo+ self.GClient_AddressParameter + address.replace(' ', '+') + "&key=" + self.API_KEY).read()

if __name__=='__main__':
    geocodeAPI=GeocodeAPI("AIzaSyCNIxgpyuhKEKrSQPf2FbodHcqyjH6gi4s")
    print(geocodeAPI.getGeocode("Tilak Nagar, New Delhi"))
    print(geocodeAPI.getPlaceId("Tilak Nagar, New Delhi"))
    # print(geocodeAPI.sendResponse("Tilak Nagar, New Delhi",True))
    print(geocodeAPI.sendResponse("Tilak Nagar, New Delhi", False))

