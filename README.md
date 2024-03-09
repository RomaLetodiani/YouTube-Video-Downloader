# YouTube Video Downloader

This Python script allows you to download YouTube videos using the `pytube` library.

## Prerequisites

- Python 3.x installed on your system
- `pytube` library installed. You can install it via pip:

```
pip install pytube
```

## Usage

1. Run the script by executing `python "Youtube Video Downloader.py"`.
2. You will be prompted to enter the URL of the YouTube video you want to download.
3. After entering the URL, the script will fetch information about the video such as title and views.
4. The script will then download the video in the highest available resolution to the directory where the script is located.

## Example

```

$ python youtube_downloader.py
Enter the YouTube URL: [Enter the YouTube URL here]
Title: [Video Title]
Views: [Number of Views]
Download complete.

```

## Note

- Make sure you have the necessary permissions to download videos from YouTube and comply with YouTube's terms of service.
- The downloaded video will be saved in the same directory as the script.
- In case of any errors during the process, an error message will be displayed.
