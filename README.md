# Spotify-Recommendation-System
## 🔧 technique.py: Song Similarity Analysis Using Cosine Similarity

This script demonstrates how Spotify-style recommendations can be built by comparing the audio features of songs using **cosine similarity**.

### 📂 What It Does
- Loads song data from `data.csv`, including features like **danceability**, **energy**, **tempo**, and **genre tags**.
- Selects two songs and compares them using **vector similarity** techniques.
- Computes the **cosine similarity** and **angle** between the song vectors to measure how alike they are.

### 📊 Visual Outputs
- **Bar Chart** comparing feature values side-by-side
- **2D Vector Plots**:
  - Danceability vs Energy
  - Energy vs Tempo

These visualizations help explain how audio-based recommendation systems identify similar songs based on sound characteristics.

> 💡 You can modify the indices (`song_a`, `song_b`) in the code to compare any two songs from the dataset.

---

