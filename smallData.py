import csv

# Create CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Artist', 'Title', 'Danceability', 'Energy', 'Tempo', 'Genre_Rock', 'Genre_Indie', 'Genre_Pop'])
    
    # Example latest artist data rows
    writer.writerow(['Olivia Rodrigo', 'vampire', 0.62, 0.75, 90, 0, 1, 1])
    writer.writerow(['The Weeknd', 'Blinding Lights', 0.73, 0.8, 171, 1, 0, 1])
    writer.writerow(['Billie Eilish', 'Happier Than Ever', 0.55, 0.6, 135, 0, 1, 1])
    writer.writerow(['Taylor Swift', 'Anti-Hero', 0.67, 0.7, 97, 0, 1, 1])
    writer.writerow(['One Direction', 'Story of My Life', 0.6, 0.65, 120, 1, 0, 1])
    writer.writerow(['Adele', 'Easy On Me', 0.48, 0.45, 70, 0, 1, 0])
