import streamlit as st

from agents.story_agent import generate_story
from agents.character_agent import generate_characters
from agents.scene_agent import generate_scenes
from agents.prompt_agent import generate_image_prompts
from agents.storyboard_agent import generate_storyboard

st.set_page_config(
    page_title="AI Storyboard & Comic Generator",
    page_icon="🎨",
    layout="wide"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Characters",
    "3"
)

col2.metric(
    "Scenes",
    "5"
)

col3.metric(
    "Panels",
    "5"
)

st.title("🎨 AI Storyboard & Comic Generator")

st.markdown(
    """
    Transform simple ideas into complete storyboards using AI-powered creative agents.
    """
)

with st.expander("🏗️ Multi-Agent Workflow"):

    st.markdown("""
    User Idea
    ↓
    Story Agent
    ↓
    Character Agent
    ↓
    Scene Agent
    ↓
    Prompt Agent
    ↓
    Storyboard Agent
    ↓
    Final Storyboard
    """)

genre = st.selectbox(
    "Genre",
    [
        "Sci-Fi",
        "Fantasy",
        "Adventure",
        "Mystery",
        "Comedy",
        "Horror"
    ]
)

story_idea = st.text_area(
    "Enter Story Idea"
)

if st.button("Generate Storyboard"):

    if not story_idea.strip():
        st.error("Please enter a story idea.")
        st.stop()

    status = st.empty()

    # Story Agent
    status.info("📖 Story Agent Running...")

    story = generate_story(story_idea, genre)

    # Character Agent
    status.info("🎭 Character Agent Running...")

    characters = generate_characters(story)

    # Scene Agent
    status.info("🎬 Scene Agent Running...")

    scenes = generate_scenes(
        story,
        characters
    )

    # Prompt Agent
    status.info("🖼️ Prompt Agent Running...")

    prompts = generate_image_prompts(
        story,
        characters,
        scenes
    )

    # Storyboard Agent
    status.info("📚 Storyboard Agent Running...")

    storyboard = generate_storyboard(
        story,
        characters,
        scenes,
        prompts
    )

    status.success("✅ Storyboard Generated Successfully")

    st.divider()

    with st.expander("📖 Story", expanded=True):
        st.write(story)

    with st.expander("🎭 Characters"):
        st.markdown(characters)

    with st.expander("🎬 Scenes"):
        st.write(scenes)

    with st.expander("🖼️ Image Prompts"):
        st.write(prompts)

    with st.expander("📚 Final Storyboard"):
        st.write(storyboard)

    report = f"""
AI STORYBOARD REPORT

========================
STORY
========================

{story}

========================
CHARACTERS
========================

{characters}

========================
SCENES
========================

{scenes}

========================
IMAGE PROMPTS
========================

{prompts}

========================
STORYBOARD
========================

{storyboard}
"""

    st.download_button(
        label="📥 Download Storyboard",
        data=report,
        file_name="storyboard.txt",
        mime="text/plain"
    )