# 🎵 Music Recommender

A web application that predicts music genres, extracts audio features, and recommends similar songs based on machine learning.

## 🚀 Features

- **Genre Prediction**: Analyzes audio files to predict music genre using a TensorFlow/Keras model
- **Audio Feature Extraction**: Extracts energy, danceability, and loudness features from songs
- **Song Recommendations**: Suggests similar songs based on genre and audio features
- **YouTube Integration**: Downloads songs directly from YouTube for analysis
- **Audio Playback**: Built-in player for uploaded/downloaded songs

## 🧠 Machine Learning Model

The application uses a trained TensorFlow model that can classify songs into 10 genres:
- Blues
- Classical
- Country
- Disco
- Hip-Hop
- Jazz
- Metal
- Pop
- Reggae
- Rock

## 🛠️ Technical Stack

- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow, Keras
- **Audio Processing**: librosa, soundfile
- **Data Analysis**: pandas, scikit-learn
- **Frontend**: HTML, CSS, JavaScript
- **External Tools**: yt-dlp for YouTube downloads

## 📁 Project Structure

```
MusicRecommender/
├── app.py                 # Main Flask application
├── extract_features.py    # Audio feature extraction
├── recommend.py           # Song recommendation system
├── requirements.txt       # Python dependencies
├── data/                  # Dataset for recommendations
├── model/                 # Trained ML model
├── static/                # CSS and static assets
├── templates/             # HTML templates
│   ├── index.html         # Main page with player and song list
│   └── result.html        # Results page with predictions
├── uploads/               # Uploaded and downloaded audio files
└── utils/                 # Helper functions
    ├── file_utils.py      # File handling utilities
    └── model_utils.py     # Model prediction utilities
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- yt-dlp (for YouTube downloads)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/MusicRecommender.git
   cd MusicRecommender
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install yt-dlp for YouTube downloads:
   ```
   pip install yt-dlp
   ```

### Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📊 Web Interface

### Main Page
- Music player with controls
- List of uploaded songs
- YouTube search and download functionality
- Song analysis button

### Results Page
- Displays predicted genre with confidence scores
- Shows extracted audio features
- Lists song recommendations based on genre and features

## 🧩 How It Works

1. **Upload or Download**: Add songs to the application by uploading files or downloading from YouTube
2. **Select and Play**: Choose a song from the list to play it in the built-in player
3. **Analyze**: Click the "Analyze Song" button to process the selected song
4. **View Results**: See the predicted genre, audio features, and recommended similar songs

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [librosa](https://librosa.org/) for audio processing
- [TensorFlow](https://www.tensorflow.org/) for machine learning
- [Flask](https://flask.palletsprojects.com/) for web framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube downloads