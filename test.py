from agents.story_agent import generate_story
from agents.character_agent import generate_characters

story = generate_story(
    "A lonely robot finds a friend in a futuristic city"
)

characters = generate_characters(story)

print(characters)