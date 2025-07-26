import json
import os
import wikipedia
from difflib import get_close_matches

MEMORY_FILE = "super_bot_memory.json"

# Load the bot's memory (saved knowledge)
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {
        "hello": "Hey there! How's it going?",
        "who made you": "I was built by Eshan, the coding master!",
        "what is python": "Python is a popular programming language.",
        "what is ai": "AI means Artificial Intelligence, machines that can think (sort of)."
    }

# Save the bot's memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# Find close match for typos
def match_question(user_input, question_list):
    matches = get_close_matches(user_input.lower(), question_list, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

# Try to answer using memory, else Wikipedia
def get_answer(user_input, memory):
    # Check memory first
    question = match_question(user_input, memory.keys())
    if question:
        return memory[question]

    # Try Wikipedia if not in memory
    try:
        summary = wikipedia.summary(user_input, sentences=2)
        return summary
    except:
        return None

def chat():
    memory = load_memory()
    print("🤖 SuperSmartBot: Ask me *anything*! (type 'exit' to quit)")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🤖 SuperSmartBot: Bye! I’ll remember what I learned.")
            save_memory(memory)
            break

        answer = get_answer(user_input, memory)
        if answer:
            print(f"🤖 SuperSmartBot: {answer}")
        else:
            print("🤖 SuperSmartBot: I don’t know. What should I reply with?")
            new_answer = input("You (teach me): ").strip()
            memory[user_input.lower()] = new_answer
            print("🤖 SuperSmartBot: Got it! I’ll remember that.")

if __name__ == "__main__":
    chat()