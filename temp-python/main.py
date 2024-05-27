from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="nova",
  input="""How might we...Design an AI feature for Spotify that promotes positive relations with others.

Imagine being at a party.

And then someone suggests the Spotify Music quiz

Setup the quiz as the host. 
By hosting a music quiz, AI will help you generate a quiz based on your friends' music tastes.

Let your friends join the quiz

As the host, you can adjust the quiz.
When you press this, you will make the quiz personal, so you and your friends can learn more about each other

After generating, the quiz can begin!

Here, the personalized feature is expressed.
You will meet questions like “Who among your friends had this song as their most played in 2023?”

Bring your friends closer with Spotify’s AI-powered music quiz. Discover more, connect more, and enjoy the music together!
"""
)

response.stream_to_file(speech_file_path)