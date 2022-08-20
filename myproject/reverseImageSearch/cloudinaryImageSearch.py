from serpapi import GoogleSearch
import json
import webbrowser
import os
import cloudinary
import cloudinary.uploader

def searchAPI(image_url):

    #Reverse Image search: Google only
    params = {
    "api_key": "ca13d0bf8ef1a4a0e4178d60fd95b20fee072112de73a4cf1447bc684e335ede",
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
    webbrowser.open(resultLink)  # Go to link

    thetitles = []
    for i in range(0, len(theResults)):
        title = theResults[i]['title']
        print(title + '\n')
        thetitles.append(title)

    # The title[3] is because second last usually at this point is the most relevant results
    
    if (len(thetitles)>=3):
        query = thetitles[2]
    else:
        query = thetitles[1]
    params2 = {
        "engine": "youtube",
         "search_query": query,
         "api_key": "ca13d0bf8ef1a4a0e4178d60fd95b20fee072112de73a4cf1447bc684e335ede"
    }

    search2 = GoogleSearch(params2)
    results2 = search2.get_dict()
    with open('resultYoutube.json', 'w') as fp:
        json.dump(results2, fp, indent=4)
    print("The results")
    aLink = results2['search_metadata']['youtube_url']
    webbrowser.open(aLink)

def list_file_name(path):
    fileList = os.listdir(path)
    return(fileList)

def inputImages(path):
    allFiles = list_file_name(path)
    allurls = []
    for name in allFiles:
        upload = cloudinary.uploader.upload("frames/"+name)
        url = upload['url']
        searchAPI(url)
        allurls.append(url)
    return allurls