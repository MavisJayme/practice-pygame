def generate_lyrics(name):
    # Normalize name for rhyme
    if name[0].lower() in 'aeiou':
        rhyme = name.lower()
    else:
        rhyme = name[1:].lower()

    lyrics = f"""
{name},Hold me, love me, touch me, honey
Be the first who ever did
{name}!
    """
    return lyrics

# Main program
def main():
    name = input("Hello! What's your name?l: ").strip().capitalize()
    if not name.isalpha():
        print("Please enter a valid name using only letters.")
        return
    lyrics = generate_lyrics(name)
    print("\nHere are your personalized lyrics:\n")
    print(lyrics)

# Run the program
if __name__ == "__main__":
    main()
