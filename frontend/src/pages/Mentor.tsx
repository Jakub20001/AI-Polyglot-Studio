import React from "react";

const Mentor: React.FC = () => {
    return (
        <section className="px-6 py-12 text-center">
            <h2 className="text-3xl font-bold text-pink-700 mb-4">AI Language Mentor</h2>
            <p className="text-gray-600 mb-6 max-w-xl mx-auto">
                Ask anything about the language you're learning - grammar, expressions, translations - and get personalized AI feedback.
            </p>

            {/* Component: MentorChat.tsx */}
            <div className="border rounded-lg p-6 bg-white shadow-sm">
                <p className="text-gray-500 italic">Mentor chat interface coming soon...</p>
            </div>
        </section>
    );
};

export default Mentor;

