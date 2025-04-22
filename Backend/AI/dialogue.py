import os
import openai
from dotenv import load_dotenv
from typing import Dict

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_dialogue(topic: str, level: str = "beginner", language: str = "English") -> Dict[str, str]:
    """
    Generates a simulated dialogue in the target language based on the given topic and level.
    
    Args:
        topic (str): The subject of the dialogue (e.g., "ordering food", "introductions).
        level (str): The language level of the user (e.g., beginner, intermediate, advanced).
        language (str): The language to generate the dialogue in.
        
    Returns:
        Dict[str, str]: Dictionary containing either a 'dialogue' or 'error' message.
    """
    prompt = (
        f"Create a simple and realistic dialogue in {language} for a language learner at the {level} level.\n"
        f"The topic is: '{topic}'. Include at least 4 lines per speaker.\n"
        f"Label the speakers as 'A:' and 'B:' and keep the conservation relevant to everyday situations. \n"
        f"Make it engaging, clear, and culturally appropriate.\n"
        f"\nDialogue:\n"
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert in writing natural dialogues for {language} learners."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=600,
            n=1,
        )
        
        dialogue = response.choices[0].message.content.strip()
        
        return {"dialogue": dialogue}
    
    except openai.error.OpenAIError as e:
        return {"error": f"OpenAI API error"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}