print("Welcome to Netflix Movie Recommendation System")
print("Type 'bye' or 'exit' anytime to quit.\n")

while True:
    print("\nAvailable Genres:")
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")
    print("4. Romance")
    print("5. Kids")

    genre = input("\nEnter your favorite genre: ").lower()

    if genre == "bye" or genre == "exit":
        print("\n Thank you for using Netflix Movie Recommendation System!")
        break

    elif genre == "action":
        print("\n Recommended Action Movies:")
        print("- Godzilla Minus One")
        print("- Extraction")
        print("- RRR")
        print("- Rebel Ridge")
        print("- The Night Comes for Us")

    elif genre == "comedy":
        print("\n Recommended Comedy Movies:")
        print("- Hit Man")
        print("- Nice Girls")
        print("- Glass Onion: A Knives Out Mystery")
        print("- Japan")
        print("- Mandela")

    elif genre == "horror":
        print("\n Recommended Horror Movies:")
        print("- The Ritual")
        print("- His House")
        print("- Don't Move")
        print("- Andhaghaaram")
        print("- Virupaksha")

    elif genre == "romance":
        print("\n Recommended Romance Movies:")
        print("- People We Meet on Vacation")
        print("- Always Be My Maybe")
        print("- With Love")
        print("- Love Today")
        print("- Irugapatru")

    elif genre == "kids":
        print("\n Recommended Kids Movies:")
        print("- Leo")
        print("- The Sea Beast")
        print("- Orion and the Dark")
        print("- The Twits")
        print("- Plankton: The Movie")

    else:
        print("\n Sorry! Genre not found.")
        print("Please choose Action, Comedy, Horror, Romance, or Kids.")
