from agents.story_agent import generate_story
from agents.character_agent import generate_characters
from agents.scene_agent import generate_scenes
from agents.prompt_agent import generate_image_prompts

story = generate_story(
    "A lonely robot finds a friend in a futuristic city"
)

characters = generate_characters(story)

scenes = generate_scenes(
    story,
    characters
)

prompts = generate_image_prompts(
    story,
    characters,
    scenes
)

print(prompts)