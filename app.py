from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

playlists = []
playlist_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    global playlist_id
    if request.method == 'POST':
        if 'add_playlist' in request.form:
            name = request.form.get('name')
            playlists.append({'id': playlist_id, 'name': name, 'songs': []})
            playlist_id += 1
        elif 'add_song' in request.form:
            pid = int(request.form.get('playlist_id'))
            song = request.form.get('song')
            for pl in playlists:
                if pl['id'] == pid:
                    pl['songs'].append(song)
                    break
        elif 'delete_playlist' in request.form:
            pid = int(request.form.get('playlist_id'))
            playlists[:] = [pl for pl in playlists if pl['id'] != pid]
    return render_template('main.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)