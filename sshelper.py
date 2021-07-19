import requests, json

class SSHelper:

    def __init__(self, apiKey, originCountry = "ESP", currency = "EUR", locale = "es-ES", rootURL="https://partners.api.skyscanner.net/apiservices/reference/v1.0"):
        self.currency = currency
        self.locale =  locale
        self.rootURL = rootURL
        self.originCountry = originCountry
        self.apiKey = apiKey
        self.countries = []

    def getCountries(self, debug = False):
        countriesSkyScannerURL = self.rootURL + "/countries/" + self.locale + "?apiKey=" +  self.apiKey
        if (debug):
            print("DEBUG - Url to acess the countries in skyskanner: " + countriesSkyScannerURL)
        response = requests.get(countriesSkyScannerURL)
        resultJSON = json.loads(response.text)
        if (debug):
            print("DEBUG - Response Countries: " + json.dumps(resultJSON, indent =2))
        if("Countries" in resultJSON):
            self.countries.append(resultJSON["Countries"])
        return self.countries
