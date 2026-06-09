from services.grok_client import client, MODEL

def generate_story(story_idea):

    prompt = f"""
    Create a compelling story.

    Idea:
    {story_idea}

    Generate:

    1. Title
    2. Story Summary
    3. Beginning
    4. Conflict
    5. Resolution
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional storyteller."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content