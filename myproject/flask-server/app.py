from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from serpapi import GoogleSearch
import json
import webbrowser
api_key = "682344854cbadadac08f5981a33e52990f024d4d285e69656d7645e604228cbf"


def searchAPI(image_url):

    #Reverse Image search: Google only
    params = {
    "api_key": api_key,
    "engine": "google_reverse_image",
    "google_domain": "google.com",
    "q": "",
    "image_url": image_url,
    "tbm": "shop"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    # Using a JSON string
    with open('result.json', 'w') as fp:
        json.dump(results, fp, indent=4)
    print("The results")
    
    theResults = results["image_results"]
    resultLink = results["search_metadata"]["google_reverse_image_url"]
    # webbrowser.open(resultLink)  # Go to link
    
    
    
    


    
    
    for i in range(0, len(theResults)):
        title = theResults[i]['title']
        print(title + '\n')


    params2 = {
    "api_key": api_key,
    "engine": "youtube",
    "search_query": theResults[0]['title']
    }

    search2 = GoogleSearch(params2)
    results2 = search2.get_dict()
    with open('resultYoutube.json', 'w') as fp:
        json.dump(results2, fp, indent=4)
    print("The results")

    theLink = results2["video_results"][1]['link']
    # webbrowser.open(theLink)  # Go to link

    productName = results['search_information']['query_displayed']

    paraProduct = {
    "q": productName,
    "tbm": "shop",
    "hl": "en",
    "gl": "us",
    "api_key": api_key
    }

    productSearch = GoogleSearch(paraProduct)
    productResults = productSearch.get_dict()
    shopping_results = productResults["shopping_results"]

    shopLink = productResults['search_metadata']['google_url']
    with open('resultProducts.json', 'w') as fp:
        json.dump(productResults, fp, indent=4)
    #webbrowser.open(shopLink) 
    #Go to link





app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def my_form_post():
    # text = request.form['text']
    text = request.json['text']
    
    searchAPI(text)
    if request.method == 'POST':
        # return {'text': res}
        with open('./resultYoutube.json', 'r') as file:
            return json.load(file)

if __name__ == "__main__":
	app.run(debug = True)