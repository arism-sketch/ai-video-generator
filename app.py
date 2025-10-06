import streamlit as st

st.set_page_config(page_title="Scene-to-Video Generator", layout="centered")

st.title("🎬 AI Scene-to-Video Generator")
st.subheader("Type your scene. Choose your style. Get a video.")

# Prompt input
prompt = st.text_area("📝 Describe your scene", placeholder="e.g. A tired person sipping coffee in a cozy kitchen")

# Style selector
style = st.selectbox("🎨 Choose a visual style", ["Cinematic", "Cartoon", "Surreal", "Fantasy", "Minimalist"])

# Voiceover toggle
voiceover = st.checkbox("🎙️ Add voiceover narration")

# Submit button
if st.button("Generate Video"):
    st.info("🚀 Generating your video... This may take a minute.")
    # Placeholder for backend call
    st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")  # Replace with actual output

# Footer
st.markdown("---")
st.caption("Built by Aris • Powered by AI • Modular & Remixable")
