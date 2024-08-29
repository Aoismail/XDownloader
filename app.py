from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'best',
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    video_path = 'video.mp4'
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
