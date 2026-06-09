from services.grok_client import client, MODEL

def generate_scenes(story, characters):

    prompt = f"""
    Create a storyboard scene breakdown.

    Story:
    {story}

    Characters:
    {characters}

    Generate 5 scenes.

    For each scene provide:

    - Scene Number
    - Scene Title
    - Location
    - What Happens
    - Key Characters
    - Visual Description
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional storyboard artist."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content