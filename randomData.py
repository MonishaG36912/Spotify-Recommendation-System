import csv
import random

artists = [
    "Olivia Rodrigo", "The Weeknd", "Billie Eilish", "Dua Lipa", "Bruno Mars",
    "Taylor Swift", "Ed Sheeran", "Adele", "Coldplay", "Imagine Dragons",
    "Post Malone", "Lorde", "Shawn Mendes", "Ariana Grande", "Maroon 5",
    "Harry Styles", "Khalid", "Doja Cat", "Selena Gomez", "Sam Smith"
]

titles = [
    "Song A", "Song B", "Hit Track", "Latest Tune", "New Wave",
    "Summer Vibes", "Nightfall", "Heartbeat", "Sunshine", "Dreams"
]

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Artist', 'Title', 'Danceability', 'Energy', 'Tempo', 'Genre_Rock', 'Genre_Indie', 'Genre_Pop'])
    
    for _ in range(100):
        artist = random.choice(artists)
        title = random.choice(titles)
        danceability = round(random.uniform(0.3, 0.9), 2)  # Between 0.3 and 0.9
        energy = round(random.uniform(0.4, 0.95), 2)       # Between 0.4 and 0.95
        tempo = random.randint(60, 180)                     # Between 60 and 180 bpm
        genre_rock = random.choice([0, 1])
        genre_indie = random.choice([0, 1])
        genre_pop = random.choice([0, 1])
        
        writer.writerow([artist, title, danceability, energy, tempo, genre_rock, genre_indie, genre_pop])
