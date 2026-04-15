import random

words = {
    "buah":["RAMBUTAN","ANGGUR","TEMBIKAI"],
    "haiwan":["HARIMAU","PENGUIN","ZIRAFAH"],
    "benda":["KASUT","ALMARI","JADUAL"]
}

category = ["buah","haiwan","benda"]

cat = random.choice(category)
word = list(random.choice(words[cat]))

# 🔀 scramble huruf
scrambled = word[:]          # copy list
random.shuffle(scrambled)    # kacau susunan

print(f"Category: {cat}")
print(" ".join(scrambled))

while True:
    print()
    user = input("Teka perkataan apa ni: ")

    if user.lower() == ''.join(word).lower():
        print("Congratulations, you guessed it right!")
        break
    else:
        print("Try Again.")
