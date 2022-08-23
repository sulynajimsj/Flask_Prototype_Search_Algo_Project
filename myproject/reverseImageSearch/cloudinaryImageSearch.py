from serpapi import GoogleSearch
import json
import webbrowser
import os
import cloudinary
import cloudinary.uploader
from Transcripts import ytranscripts
from Transcripts import TextCompare
def searchAPI(image_url):

    #Reverse Image search: Google only
    params = {
    "api_key": "01e56b5235e477b4c011c41ee2ec6bebeb6bb5876b7e4041586dd593d595eb2e",
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
         "api_key": "01e56b5235e477b4c011c41ee2ec6bebeb6bb5876b7e4041586dd593d595eb2e"
    }

    search2 = GoogleSearch(params2)
    results2 = search2.get_dict()
    with open('resultYoutube.json', 'w') as fp:
        json.dump(results2, fp, indent=4)
    print("The results")
    aLink = results2['search_metadata']['youtube_url']
    webbrowser.open(aLink)


    #Get speechtotext

    #Get all transcripts
    ytVideos = results2['video_results']

    for video in ytVideos:
        print(video['link'])
        try:
            ytranscripts.getYoutubeTranscript(video['link'])
            
        except:
            with open('op.txt', 'w') as opf:
                opf.write("ERROR Error")
            print("Transcript ERROR")
        
        
        # Compare the videos 
        theVideoLink = video['link']
        textComp = TextCompare.textCompare(r"C:\Users\Suleiman\Desktop\Flask_Prototype_Search_Algo_Project\myproject\op.txt", r"C:\Users\Suleiman\Desktop\Flask_Prototype_Search_Algo_Project\myproject\transcript.txt")

        isMatch = textComp.compare()
        if (isMatch):
            print('MATCH FOUND')
            webbrowser.open(theVideoLink)



        

            
        


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