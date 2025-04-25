import React from "react";

const Quiz: React.FC = () => {
    return (
        <section className="px-6 py-12 text-center">
            <h2 className="text-3xl font-bold text-green-700 mb-4">Language Quiz</h2>
            <p className="text-gray-600 mb-6 max-w-xl mx-auto">
                Test your knowledge with smart, AI-generated open-ended quizzes tailored to your level.
            </p>

            {/* Component: QuizInput / questions and answers */}
            <div className="border rounded-lg p-6 bg-white shadow-sm">
                <p className="text-gray-500 italic">Quiz interface coming soon...</p>
            </div>
        </section>
    );
};

export default Quiz;