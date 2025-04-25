import React from "react";

const Learn: React.FC = () => {
    return (
        <section className="px-6 py-12 text-center">
            <h2 className="text-3xl font-bold text-blue-700 mb-4">Learn</h2>
            <p className="text-gray-600 mb-6 max-w-xl mx-auto">
                Choose your language, topic, and level. Practice vocabulary, grammar and speaking with AI-powered learning tools.
            </p>
            
            {/*Future components: language selection, level selection, learning plan*/}
            <div className="border rounded-lg p-6 bg-white shadow-sm">
                <p className="text-gray-500 italic">Learning modules coming soon...</p>
            </div>
        </section>
    );
};

export default Learn;