from youtube_transcript_api import YouTubeTranscriptApi

video_transcipts = []
thelink = "https://www.youtube.com/watch?v=hcwWJe2yX2w"
newLink = thelink.rsplit('v=', 1)[1]

print(newLink)

text = YouTubeTranscriptApi.get_transcript(newLink)
for i in text:
    vidStr = ""
    outext = (i['text'])
    vidStr += outext
    video_transcipts.append(vidStr)
    print(outext)

print(video_transcipts)