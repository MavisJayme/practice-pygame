import time
import sys

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # new line after text is done

def get_song_for_name(name):
    name = name.lower()
    songs = {
        "sara": "🎶 *Sara* by Starship\nSara, you're the poet in my heart...",
        "layla": "🎶 *Layla* by Eric Clapton\nLayla, you've got me on my knees...",
        "julia": "🎶 *Julia* by The Beatles\nJulia, Julia, ocean child...",
        "roxanne": "🎶 *Roxanne* by The Police\nRoxanne, you don't have to put on the red light...",
        "amanda": "🎶 *Amanda* by Boston\nI'm gonna say it like a man, and make you unlayladerstand, Amanda...",
    }

    if name in songs:
        return f"\n{name.title()}, this song is for you!\n\n{songs[name]}"
    else:
        return f"\n{name.title()}, you're special — but I don't have a song just for your name.\nHere's a beautiful lyric for you anyway:\n\n🎶 You are amazing, just the way you are 🎶\n— Bruno Mars"

def main():
    name = input("Hi, Baby girl! What's your name?: ").strip()
    if not name.isalpha():
        print("Please enter a valid name using only letters.")
        return
    lyrics = get_song_for_name(name)
    type_text(lyrics, delay=0.05)  # Adjust speed as desired

if __name__ == "__main__":
    main()
