from flask import Flask,request
from geocodeConvertor import GeocodeAPI
app=Flask(__name__)

@app.route('/getGeocode',methods=['POST'])
def getGeocode():
    if not request.json or 'address' not in request.json or 'API' not in request.json:
        return "REQUEST IS NOT RIGHT"

    geocodeAPI=GeocodeAPI(request.json.get("API"))

    return str(geocodeAPI.getGeocode(request.json.get("address")))


@app.route('/getPlaceId',methods=['POST'])
def getPlaceId():
    if not request.json or 'address' not in request.json or 'API' not in request.json:
        return "REQUEST IS NOT RIGHT"

    geocodeAPI=GeocodeAPI(request.json.get("API"))

    return geocodeAPI.getPlaceId(request.json.get("address"))

@app.route('/getFormatData',methods=['POST'])
def getFormatData():
    if not request.json or 'isXML' not in request.json or 'API' not in request.json or 'address' not in request.json:
        return "REQUEST IS NOT RIGHT"

    geocodeAPI=GeocodeAPI(request.json.get("API"))

    return geocodeAPI.sendResponse(request.json.get("address"),request.json.get("isXML"))



if __name__=='__main__':
    app.run(debug=True)
