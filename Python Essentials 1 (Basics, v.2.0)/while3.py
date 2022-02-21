word = "chupacabra"
guess = str(input("Choose your animal: "))

while True:
    if guess == word:
        break
    else:
        print("Wrong animal, pick again")
        guess = str(input("Choose your animal: "))
print("You've successfully left the loop.")
