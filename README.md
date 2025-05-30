# Spotify-Recommendation-System
🔧 technique.py: Song Similarity Analysis Using Cosine Similarity
This script demonstrates how Spotify-style recommendations can be built by comparing the audio features of songs using cosine similarity.

Loads song data from data.csv, including features like danceability, energy, tempo, and genre tags.

Selects two songs and compares them using vector similarity techniques.

Computes the cosine similarity and angle between the song vectors to measure how alike they are.

Generates:

📊 A bar chart comparing feature values side-by-side.

🧭 Two 2D vector plots showing:

Danceability vs Energy

Energy vs Tempo

This helps visualize how the recommendation engine compares songs based on their audio profiles. You can modify the indices to compare any pair of songs in the dataset.
