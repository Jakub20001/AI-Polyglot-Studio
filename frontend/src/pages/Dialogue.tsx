import React from "react";

const Dialogue: React.FC = () => {
    return (
        <section className="px-6 py-12 text-center">
            <h2 className="text-3xl font-bold text-purple-700 mb-4">AI Dialogues</h2>
            <p className="text-gray-600 mb-6 max-w-xl mx-auto">
                Engage in thematic conversations with AI to improve your fluency and comprehension in real-world scenarios.
            </p>

            {/* Component: Topic selection + dialogue interface */}
            <div className="border rounded-lg p-6 bg-white shadow-sm">
                <p className="text-gray-500 italic">Dialogue generator coming soon...</p>
            </div>
        </section>
    );
};

export default Dialogue;
