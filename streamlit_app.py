import streamlit as st
from pathlib import Path
from video_generator import generate_video_from_caption, set_output_folder  # Your refactored code

# Streamlit Interface
st.title("Text-to-Video Generation")
st.write("Enter a caption to generate a video.")

# Input for caption
caption = st.text_input("Caption", placeholder="Type your video caption here...")

# Input for output folder
output_folder_name = st.text_input("Output Folder Name", "generated_videos")

# Set and display the output folder path
output_folder = set_output_folder(output_folder_name)
st.write(f"Videos will be saved to: `{output_folder}`")

# Generate video on button click
if st.button("Generate Video"):
    if caption.strip():
        st.write("Generating video, please wait...")
        try:
            # Call the video generation function
            video_path = generate_video_from_caption(caption, output_folder)
            st.success("Video generated successfully!")
            st.video(video_path)
        except Exception as e:
            st.error(f"Error generating video: {e}")
    else:
        st.warning("Please enter a caption.")
