import React, { useState } from 'react';

interface QuizInputProps {
    question: string,
    onSubmit: (answer: string) => void;
}

const QuizInput: React.FC<QuizInputProps> = ({ question, onSubmit }) => {
    const [answer, setAnswer] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit(answer.trim())
        setAnswer('');   
    };

    return (
        <form onSubmit={handleSubmit} className="max-w-lg mx-auto text-left bg-white p-6 rounded shadow">
            <label className="block text-gray-800 font-semibold mb-2">{question}</label>
            <input
            type="text"
            value={answer} 
            onChange={(e) => setAnswer(e.target.value)}
            className="w-full border border-gray-300 rounded px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500" 
            placeholder="Your answer..."
            required
            />
            <button type="submit" className="bg-blue-600 hover:bg-blue-700 text-white font-semibold">
                Submit
            </button>
        </form>
    );
};

export default QuizInput;

