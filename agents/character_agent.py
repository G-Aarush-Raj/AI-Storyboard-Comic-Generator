from services.grok_client import client, MODEL

def generate_characters(story):

    prompt = f"""
    Based on the story below, create 3 main characters.

    Story:
    {story}

    For each character provide:

    1. Name
    2. Role
    3. Personality
    4. Appearance
    5. Motivation
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a character design expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content