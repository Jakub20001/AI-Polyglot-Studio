def mentor_prompt(language: str, query: str) -> str:
    return (
        f"You're a professional language mentor helping a student learn {language}.\n"
        f"The student asked: {query}'.\n"
        "Provide a helpful, clear, and engaging response tailored to their level.\n"
        "Include examples or suggestions if useful.\n"
    )
    
    
def dialogue_prompt(topic: str, level: str) -> str:
    return (
        f"Generate a conversation in {level} difficulty on the topic '{topic}'.\n"
        "Structure it as a natural dialogue between two language learners with appropriate grammar."
    )
    
def quiz_prompt(language: str, topic: str) -> str:
    return (
        f"Create 5 beginner-friendly language quiz questions for learning {language} on the topic '{topic}'\n"
        "Each question should include a correct answer."
    )