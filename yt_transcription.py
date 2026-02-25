#imports/libs/API'S
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

#gets the transcript from the captions of the video using yt API
def fetch_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        return " ".join(seg.text for seg in transcript)
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"No captions: {e}")
        return None
    except Exception as e:
        print(f"Error fetching captions: {e}")
        return None

#parse the video link for id only since thats what yt API accepts
def pull_id(video_url):
    parsed = urlparse(video_url)

    if "youtu.be" in parsed.netloc:
        return parsed.path.strip("/")

    params = parse_qs(parsed.query)
    return params.get("v", [None])[0]

#text, just for testing in CLI. will be switched later when hosted on web
print(f"welcome to YT Transcription bot \nplease enter a valid youtube url to begin processing")

#user input + message for conformation
url = input(f"enter video link: ")
print(f"processing - this may take a few seconds (depending on the length of the video)")

#parse url + pull transcript
transcript = fetch_captions(pull_id(url))

if transcript:
    print("video successfully processed\n")
    print(transcript)
else:
    print("No captions available for this video.")
