import os
import openai
from dotenv import load_dotenv
from typing import Dict

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_mentor_response(language: str, query: str, level: str = "beginner") -> Dict[str, str]:
    """
    Generates a contextual response from the AI Language Mentor.
    
    Args:
        language (str): The target language the user is learning.
        query (str): User's input/question.
        level (str): User's proficiency level (e.g, beginner, intermediate, advanced).
        
    Returns:
        Dict[str, str]: Dictionary containing either a 'response' or 'error' message.
    """
    prompt = (
        f"You are a friendly and expert language mentor helping a student learn {language} at the {level} level.\n"
        f"Your responses should include clear explanations, examples, and tips relevant to that language.\n"
        f"Query: {query}\n\nMentor:"
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a helpful and friendly mentor for learning {language}."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=700,
            n=1,
        )
        
        answer = response.choices[0].message.content.strip()
        
        return {"response": answer}
    
    except openai.error.OpenAIError as e:
        return {"error": f"OpenAI API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
    
    
