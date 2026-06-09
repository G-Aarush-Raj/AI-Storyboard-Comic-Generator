from services.grok_client import client, MODEL

def generate_storyboard(
    story,
    characters,
    scenes,
    prompts
):

    prompt = f"""
    Create a professional storyboard document.

    Story:
    {story}

    Characters:
    {characters}

    Scenes:
    {scenes}

    Image Prompts:
    {prompts}

    Organize everything into:

    1. Story Overview
    2. Character Profiles
    3. Scene Breakdown
    4. Comic Panels
    5. Visual Directions
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a storyboard director."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content