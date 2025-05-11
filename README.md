# 🎵 Music Recommender

A web application that predicts music genres, extracts audio features, and recommends similar songs based on machine learning.

## 🚀 Features

- **Welcome Page**: Modern animated landing page (Urban Beatzs) with quick navigation
- **Contact Form**: Users can send feedback or queries (saved to `contacts.json`)
- **About, Genre Analysis, Audio Features Pages**: Informative pages for users
- **Genre Prediction**: Analyzes audio files to predict music genre using a TensorFlow/Keras model
- **Audio Feature Extraction**: Extracts energy, danceability, loudness, and more
- **Song Recommendations**: Suggests similar songs based on genre and audio features
- **YouTube Integration**: Downloads songs directly from YouTube for analysis
- **Audio Playback**: Built-in player for uploaded/downloaded songs
- **Genre Fun Facts**: Displays a random fun fact, tip, and icon for each predicted genre
- **Modern UI**: Animated visualizer, responsive design, and toast notifications

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
├── static/                # CSS, JS, images, videos
│   ├── style.css          # Main styles
│   ├── main.js            # Main JS logic
│   ├── navbar.js, navbar.css
│   └── ...
├── templates/             # HTML templates
│   ├── welcome.html       # Animated landing page
│   ├── index.html         # Main page with player and song list
│   ├── result.html        # Results page with predictions
│   ├── about.html         # About page
│   ├── contact.html       # Contact form
│   ├── genre-analysis.html# Genre info
│   ├── audio-features.html# Audio features info
│   └── 404.html, 500.html # Error pages
├── uploads/               # Uploaded and downloaded audio files
├── utils/                 # Helper functions
│   ├── file_utils.py      # File handling utilities
│   └── model_utils.py     # Model prediction utilities
├── genre_facts.json       # Fun facts, tips, and icons for each genre
├── contacts.json          # Stores contact form submissions
└── ...
```

## 🌐 Main Routes & Endpoints

- `/` : Welcome page (Urban Beatzs)
- `/index` : Main app (upload, play, analyze, download)
- `/about` : About the project
- `/contact` : Contact form
- `/genre-analysis` : Genre info
- `/audio-features` : Audio features info
- `/download` : POST endpoint for YouTube song download
- `/uploads/<filename>` : Serve uploaded/downloaded audio

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ to Python 3.10
- pip
- yt-dlp (for YouTube downloads)
- 4GB RAM minimum
- 2GB free disk space
- Internet connection for YouTube downloads

### Installation

1. Clone the repository:
   ```powershell
   git clone https://github.com/yourusername/MusicRecommender.git
   cd MusicRecommender
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   pip install yt-dlp
   ```
4. Run the app:
   ```powershell
   python app.py
   ```
5. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🎥 Demo

[Add screenshots or GIF of your application in action]

## ⚠️ Error Handling

- Invalid audio file formats
- Failed YouTube downloads
- Network connectivity issues
- File permission errors
- Memory limitations
- Custom 404 and 500 error pages

## 🔧 Troubleshooting

- **YouTube Download Fails**: Update yt-dlp, check internet, try a different URL
- **Audio Analysis Error**: Use supported formats (MP3, WAV), check file integrity, ensure enough memory
- **Model Prediction Issues**: Clear browser cache, restart app, check model files in `/model`

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Web Interface

### Main Page
- Music player with controls and animated visualizer
- List of uploaded/downloaded songs (with search)
- YouTube search and download
- Song analysis button

### Results Page
- Predicted genre with confidence scores
- Extracted audio features (energy, danceability, loudness, etc.)
- Song recommendations
- Random fun fact, tip, and icon for the genre

### Welcome, About, Contact, Genre/Audio Info Pages
- Modern animated welcome page
- About page with project and tech info
- Contact form (saves to `contacts.json`)
- Genre and audio feature info pages

## 🎤 Genre Fun Facts

- Results page displays a random fun fact, tip, and icon for each predicted genre, loaded from `genre_facts.json`
- Each genre has multiple unique facts/tips
- Backend randomly selects a fact for the predicted genre and passes it to the UI

### Customizing Genre Facts

- Edit `genre_facts.json` to add or update facts, tips, or icons for any genre

## 🖌️ Modern UI Enhancements
- Animated confidence bars, genre icons, and a visually engaging, rhythm-inspired layout
- Responsive design for desktop and mobile
- Toast notifications for user feedback

## 🛣️ Ready for React (Optional)
- Backend is API-ready and can be connected to a React frontend in the future

## 🧩 How It Works

1. **Upload or Download**: Add songs by uploading files or downloading from YouTube
2. **Select and Play**: Choose a song to play in the built-in player
3. **Analyze**: Click "Analyze Song" to process the selected song
4. **View Results**: See the predicted genre, audio features, recommendations, and fun facts

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [librosa](https://librosa.org/) for audio processing
- [TensorFlow](https://www.tensorflow.org/) for machine learning
- [Flask](https://flask.palletsprojects.com/) for web framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube downloads