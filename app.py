from flask import Flask, request, send_file
from yt_dlp import YoutubeDL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return "No URL provided", 400

    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
