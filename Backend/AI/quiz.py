import os
import openai
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz(topic: str, level: str = "beginner", language: str = "English", num_questions: int = 5) -> List[Dict[str, str]]:
    """
    Generates a language learning quiz with open-ended questions based on a topic and level.
    
    Args:
        topic (str): The topic of the quiz (e.g. "food", "travel).
        level (str): The user's proficiency level (e.g. "beginner", "intermediate", "advanced").
        language (str): The target language to learn.
        num_questions (int): Number of questions to generate.
        
    Returns:
       List[Dict[str, str]]: A list of dictionaries with 'question' and 'answer' keys. 
    """
    
    prompt = (
        f"Generate {num_questions} short open-ended quiz questions in {language} for a language learner at the {level} level.\n"
        f"The topic is: '{topic}'.\n"
        f"Each question should be simple and related to everyday situations. "
        f"Provide the correct answer after each question.\n"
        f"Output format:\n"
        f"Q: <question>\nA: <answer>\n"
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful language tutor who creates short, effective quizzes for {language} learners."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800,
        )
        
        quiz_raw = response.choices[0].message.content.strip()
        lines = quiz_raw.split("\n")
        questions = []
        
        question = ""
        answer = ""
        
        for line in lines:
            if line.startswith("Q:"):
                if question and answer:
                    questions.append({"question": question, "correct_answer": answer})
                question = line[2:].strip()
                answer = ""
            elif line.startswith("A:"):
                answer = line[2:].strip()
                
        if question and answer:
            questions.append({"question": question, "correct_answer": answer})
            
        return questions
    
    except openai.error.OpenAIError as e:
        return [{"error": f"OpenAI API error: {str(e)}"}]
    except Exception as e:
        return [{"error": f"Unexpected error: {str(e)}"}]