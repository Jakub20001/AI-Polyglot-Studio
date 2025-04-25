import React from "react";

const Profile: React.FC = () => {
    return (
        <section className="px-6 py-12 text-center">
            <h2 className="text-3xl font-bold text-gray-800 mb-4">Your Profile</h2>
            <p className="text-gray-600 mb-6 max-w-xl mx-auto">
                View your XP, progress history, language's you're learning, and your saved quizzes.
            </p>

            {/* Component: XPProgress, Userdata, statistics */}
            <div className="border rounded-lg p-6 bg-white shadow-sm">
                <p className="text-gray-500 italic">Profile details coming soon...</p>
            </div>
        </section>
    );
};

export default Profile;