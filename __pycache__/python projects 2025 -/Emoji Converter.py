message = input("> ")
words = message.split(' ')
emojis = {
    ":)" : "😄",
    ":(" : "😔",
    "Good".lower() : "👍",
    "Morning".lower() : "🌄",
    "Sunshine".lower() : "☀️"

}
output = ""
for word in words:
    output += emojis.get(word,word) + " "
print(output)
