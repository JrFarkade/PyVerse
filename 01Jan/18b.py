# Anime Recommendation
print("Anime Recommendation")

genre = input("Enter genre (action/romance/horror/comedy/isekai): ").lower()

if genre == "action":
    print("Recommended Anime:")
    print("1) One Piece")
    print("2) HunterXHunter")
    print("3) Fullmetal Alchemist Brotherhood")

elif genre == "romance":
    print("Recommended Anime:")
    print("1) Fruits Basket")
    print("2) Clanned")
    print("3) ReLife")

elif genre == "horror":
    print("Recommended Anime:")
    print("1) Another")
    print("2) Tokyo Ghoul")
    print("3) Parasyte")

elif genre == "comedy":
    print("Recommended Anime:")
    print("1) Gintama")
    print("2) Grand Blue")
    print("3) Mashle: Magic and Muscles")

elif genre == "isekai":
    print("Recommended Anime:")
    print("1) Re:Zero")
    print("2) That Time I Got Reincarnated as a Slime")
    print("3) Mushoku Tensei")

else:
    print("Sorry! Genre not found 😅")
    print("Try: action / romance / horror / comedy / isekai")
