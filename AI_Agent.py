#Graded Assignment: Create an AI Agent that automates tasks of creating posts on social media platforms
#like X.com(formerly Twitter), Facebook, Instagram, telegram, etc.
#For this I will be using Telegram as the platform to automate tasks.
#This code will create a Telegram bot that can post messages to a channel or group.
# Import necessary libraries
import  requests
import json
import random

import requests
import json
import random

class SocialMediaAgent:
    def __init__(self, api_key, chat_id):
        self.api_key = api_key
        self.base_url = f'https://api.telegram.org/bot{self.api_key}/'
        self.chat_id = chat_id

    def create_post(self, content):
        url = self.base_url + 'sendMessage'
        payload = {
            'chat_id': self.chat_id,
            'text': content
        }
        
        response = requests.post(url, data=payload)
        
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise Exception(f"Error creating post: {response.status_code} - {response.text}")

    def generate_content(self, topic):
        greetings = ["Hello", "Hi", "Greetings", "Hey"]
        content = f"{random.choice(greetings)}! Here's something about {topic}."
        return content

    def post_to_telegram(self, topic):
        content = self.generate_content(topic)
        try:
            response = self.create_post(content)
            print(f"Post created successfully: {response}")
        except Exception as e:
            print(f"Failed to create post: {e}")

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    chat_id = '@your_channel_or_user_id'  # Replace with your actual chat ID
    agent = SocialMediaAgent(api_key, chat_id)
    agent.post_to_telegram("AI advancements")

       