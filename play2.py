import time
import sys

def type_text(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # new line after text is done

def get_song_for_name(name):
    name = name.lower()
    songs = {
        
        "muath": "🎶 *muath* by Leah, In a world that spins both fast and wide, You’ve been my calm, my steady tide. Not by blood, but choice and grace, A true companion in life’s long race. You hear the words I never say,So here’s to you, my dear, my friend, A bond I hope will never end.No treasure greater could I find,Than someone with your heart and mind.",
    }

    if name in songs:
        return f"\n{name.title()}, this song is for you!\n\n{songs[name]}"
    else:
        return f"\n{name.title()}, you're special — but I don't have a song just for you.\n\nHere's a little something instead:\n\n{name.title()}, you're amazing just the way you are<3!"
def main():
    name = input("Hi, Baby! What's your name?: ").strip()
    if not name.isalpha():
        print("Please enter a valid name using only letters.")
        return
    lyrics = get_song_for_name(name)
    type_text(lyrics, delay=0.05)  # Adjust speed as desired

if __name__ == "__main__":
    main()
