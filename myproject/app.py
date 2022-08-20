from concurrent.futures import process
from flask import Flask, request, render_template
from serpapi import GoogleSearch
import json
import webbrowser
from datetime import timedelta
import cv2
import numpy as np
import sys
import cloudinary
import cloudinary.uploader
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Update github
allTranscripts = []

cloudinary.config( 
  cloud_name = "odinsully", 
  api_key = "152393343981388", 
  api_secret = "ZJWfM-yTEFEYYCd13epWWj6tINs",
  secure = True
)

def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def processVideo(path):
    video_file = path
    filename = "frames"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video file    
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, 0.3)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration, 
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"frame{frame_duration_formatted}.jpg"), frame) 
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1



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
    "api_key": "ca13d0bf8ef1a4a0e4178d60fd95b20fee072112de73a4cf1447bc684e335ede",
    "engine": "youtube",
    "search_query": query
    }

    search2 = GoogleSearch(params2)
    results2 = search2.get_dict()
    with open('resultYoutube.json', 'w') as fp:
        json.dump(results2, fp, indent=4)
    print("The results")
    aLink = results2['search_metadata']['youtube_url']
    webbrowser.open(aLink)


    # print("All transcripts")
    # ytVideos = results2['video_results']
    # for i in range(0,5):

    #     #Get transcripts of each video
    #     yt_transcripts = []
    #     thelink = ytVideos[i]['link']
    #     newLink = thelink.rsplit('v=', 1)[1]

    #     print(newLink)

    #     text = YouTubeTranscriptApi.get_transcript(newLink)
    #     if (text):
    #         for i in text:
    #             vidStr = ""
    #             outext = (i['text'])
    #             vidStr += outext
    #             yt_transcripts.append(vidStr)
    #             print(outext)

    #         print(yt_transcripts)
    #     else:
    #         continue





    

    # productName = results['search_information']['query_displayed']

    # paraProduct = {
    # "q": productName,
    # "tbm": "shop",
    # "hl": "en",
    # "gl": "us",
    # "api_key": api_key
    # }

    # productSearch = GoogleSearch(paraProduct)
    # productResults = productSearch.get_dict()
    # shopping_results = productResults["shopping_results"]

    # shopLink = productResults['search_metadata']['google_url']
    # with open('resultProducts.json', 'w') as fp:
    #     json.dump(productResults, fp, indent=4)
    # webbrowser.open(shopLink) 
    #Go to link


#list file names 
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



app = Flask(__name__)
@app.route('/')
def main():

    processVideo('ronaldo.mp4')
    imageUrls = inputImages('frames')
    print(imageUrls)

    # searchAPI('https://i.imgur.com/RSP1mdN.jpg')

    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    searchAPI(text)
    return render_template('index.html')
