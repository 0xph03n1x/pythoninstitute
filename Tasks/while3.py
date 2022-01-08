word = "chupacabra"
guess = str(input("Choose your animal: "))

while guess != word:
    if guess == word:
        break
    else:
        print("Wrong animal, pick again")
        guess = str(input("Choose your animal: "))
print("You've successfully left the loop.")