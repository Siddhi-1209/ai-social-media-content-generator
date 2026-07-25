from google import genai

client = genai.Client(
    api_key="api_key"
)

print("Connected Successfully!")
models = client.models.list()

for model in models:
    print(model.name)
    break
topic = input("Enter the topic: ")

platform = input("Choose platform (LinkedIn/Instagram/X): ")

tone = input("Choose tone (Professional/Friendly/Funny): ")

audience = input("Target audience: ")

content_type = input("Content type (Post/Caption/Carousel): ")
prompt = f"""
You are an expert Social Media Content Creator.

Generate high-quality content based on the following details.

Topic: {topic}
Platform: {platform}
Tone: {tone}
Target Audience: {audience}
Content Type: {content_type}

Return the output in the following format only:

## 📢 Social Media Post
(Write one engaging post)

## 🏷️ Hashtags
(Generate exactly 5 trending hashtags)

## 📣 Call-To-Action
(Write one engaging CTA)

## 💡 Next Content Idea
(Suggest one related content idea)

Keep the language engaging, concise, and platform-specific.
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
print(response.text)
improvement_prompt = f"""
Rewrite the following social media content.

Content:

{response.text}

Make it:

- More engaging
- More professional
- More concise
- Add relevant emojis
- Keep it suitable for {platform}
"""

improved_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=improvement_prompt
)

print(improved_response.text)
image_prompt = f"""
You are an expert AI Image Prompt Engineer.

Generate one highly detailed image prompt for the following topic.

Topic: {topic}

Target Audience: {audience}

The image should look professional, modern, attractive, and suitable for posting on {platform}.

Only generate the image prompt.
"""

image_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=image_prompt
)

print(image_response.text)
from PIL import Image

image = Image.open("WhatsApp Image 2026-07-25 at 13.11.22.jpeg")
analysis_prompt = f"""
You are an expert social media marketing consultant.

Analyze this image based on the following details.

Topic: {topic}

Platform: {platform}

Target Audience: {audience}

Please answer:

1. Does this image match the topic?
2. Is it suitable for {platform}?
3. What emotions does it convey?
4. What could be improved?
5. Give the image a rating out of 10.
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        analysis_prompt,
        image
    ]
)

print(response.text)
from IPython.display import Markdown, display

display(Markdown(improved_response.text))
display(image)
