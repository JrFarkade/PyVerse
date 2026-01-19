# Typing Speed Test
import time
import random

texts = [
    "Justice is decided by the winners, not the losers.",
    "The strong control the world and write the rules.",
    "In the end, only the victorious will be called righteous.",
    "History belongs to those who win the war.",
    "Good and evil can change depending on who survives.",
    "The world is shaped by power, not by truth.",
    "In a battle, the one who stands last decides what is right."
]

print("----- TYPING SPEED TEST -----")
print("Type the given sentence as fast as you can.\n")

sentence = random.choice(texts)
print("Sentence:\n", sentence)
print("\nPress Enter when you are ready...")
input()

start_time = time.time()
typed = input("Start typing here: ")
end_time = time.time()

time_taken = end_time - start_time
time_taken_minutes = time_taken / 60

# WPM calculation
words = len(sentence.split())
wpm = words / time_taken_minutes

# Accuracy calculation
correct_chars = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

print("\n----- RESULTS -----")
print(f"Time Taken: {time_taken:.2f} seconds")
print(f"Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")

if accuracy == 100:
    print("🔥 Perfect typing!")
elif accuracy >= 80:
    print("✅ Very good!")
elif accuracy >= 60:
    print("🙂 Nice, keep practicing!")
else:
    print("⚠️ Need more practice bro!")
