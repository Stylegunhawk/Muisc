import numpy as np
import librosa

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'flac'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_album_art_for_song(song_name):
    """Return an appropriate album art URL based on the song name."""
    # In a real app, you might look up album art from a database or API
    # For now, we'll use a simple mapping of first letters to colors
    
    # Make sure we have a valid string before trying to access characters
    if not song_name or not isinstance(song_name, str) or len(song_name) == 0:
        return "/static/images/album-art/gray.svg"
    
    first_char = song_name[0].lower()
    
    # Map first character to one of several color schemes
    color_map = {
        'a': 'blue', 'b': 'red', 'c': 'green', 'd': 'purple', 
        'e': 'orange', 'f': 'teal', 'g': 'pink', 'h': 'indigo',
        'i': 'amber', 'j': 'cyan', 'k': 'lime', 'l': 'yellow',
        'm': 'blue', 'n': 'red', 'o': 'green', 'p': 'purple',
        'q': 'orange', 'r': 'teal', 's': 'pink', 't': 'indigo',
        'u': 'amber', 'v': 'cyan', 'w': 'lime', 'x': 'yellow',
        'y': 'blue', 'z': 'red'
    }
    
    # Default to gray if the first character isn't a letter
    color = color_map.get(first_char, 'gray')
    
    # Check if the SVG file exists, if not default to gray
    svg_path = f"/static/images/album-art/{color}.svg"
    
    return svg_path

def load_and_preprocess_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=210)
    mel_spec = librosa.power_to_db(mel_spec, ref=np.max)
    mel_spec = (mel_spec - np.min(mel_spec)) / (np.max(mel_spec) - np.min(mel_spec))

    if mel_spec.shape[1] < 210:
        mel_spec = np.pad(mel_spec, ((0, 0), (0, 210 - mel_spec.shape[1])), mode='constant')
    else:
        mel_spec = mel_spec[:, :210]

    mel_spec = mel_spec.reshape(1, 210, 210, 1)
    return mel_spec
