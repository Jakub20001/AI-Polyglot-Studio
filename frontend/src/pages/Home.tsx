import React from "react";
import { Link } from "react-router-dom";

const Home: React.FC = () => {
    return (
        <section className="flex flex-col items-center justify-center text-center px-6 py-20 bg-gradient-to-b from-blue-50 to-white">
            <h1 className="text-4xl sm:text-5xl font-extrabold text-gray-800 leading-tight mb-4">
                Welcome to <span className="text-blue-600">AI Polyglot Studio</span>
            </h1>
            <p className="text-lg sm:text-xl text-gray-600 max-w-2xl mb-6">
                Master foreign languages through personalized quizzes, AI dialogues, and interactive language mentorship - powered by artificial intelligence.
            </p>

            <div className="flex flex-wrap justify-center gap-4">
              <Link to="/learn" className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg shadow transition duration-300">Start Learning</Link>
              <Link to="/quiz" className="bg-white border border-blue-600 text-blue-600 hover: bg-blue-50 font-semibold px-6 py-3 rounded-lg shadow transition duration-300">Take a Quiz</Link>
            </div>

            <img src="/illustrations/language-ai.svg" alt="AI Language Illustration" className="w-full max-w-md mt-12"></img>
                   
        </section>
    );
};

export default Home;
