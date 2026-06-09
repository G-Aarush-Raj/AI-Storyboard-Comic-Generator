from services.grok_client import client, MODEL

def generate_image_prompts(
    story,
    characters,
    scenes
):

    prompt = f"""
    Create image generation prompts for a comic storyboard.

    Story:
    {story}

    Characters:
    {characters}

    Scenes:
    {scenes}

    Generate 5 detailed image prompts.

    Each prompt should include:

    - Environment
    - Characters
    - Lighting
    - Camera Angle
    - Art Style
    - Mood

    Format:

    Panel 1:
    Prompt...

    Panel 2:
    Prompt...
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a visual prompt engineering expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content