from pytube import YouTube
import os

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # Get the current directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Download the video to the current directory
    yd.download(output_path=script_dir)
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))