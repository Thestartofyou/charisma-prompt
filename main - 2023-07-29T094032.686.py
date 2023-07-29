import random

# List of prompts for charisma practice
prompts = [
    "Imagine you are introducing yourself to a group of new people. Write down a short, confident self-introduction.",
    "Practice making eye contact with yourself in the mirror for 1 minute. Smile genuinely.",
    "Think of a recent accomplishment or success. How would you share it with others in an engaging way?",
    "Find a TED talk or a speech online by a charismatic speaker. Watch it and take notes on their communication style.",
    "Choose a random topic and try to speak about it passionately for 1-2 minutes.",
    "Initiate a conversation with a friend or family member. Focus on active listening and asking open-ended questions.",
    "Write down three things you are grateful for today. Share your gratitude with someone close to you.",
    "Join a local group or club with shared interests. Practice interacting and connecting with new people.",
    "Experiment with using humor in conversations. Share a light-hearted joke or anecdote.",
    "Visualize yourself confidently handling a challenging situation. How would you approach it with charisma?",
]

def get_random_prompt():
    return random.choice(prompts)

def main():
    print("Welcome to the Charisma Practice Script!")
    print("Your charisma practice prompt for today is:")
    print(get_random_prompt())

if __name__ == "__main__":
    main()
