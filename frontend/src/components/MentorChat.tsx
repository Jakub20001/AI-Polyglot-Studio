import React, { useState } from 'react';

interface MentorChatProps {
    onAsk: (question: string) => Promise<string>;
}

const MentorChat: React.FC<MentorChatProps> = ({ onAsk }) => {
    const [input, setInput] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);
    
    const handleAsk = async (e: React.FormEvent) => {
        e.preventDefault()
        setLoading(true);
        const result = await onAsk(input);
        setResponse(result);
        setLoading(false);
        setInput('');
    };

    return (
        <div className="max-w-2xl mx-auto bg-white p-6 rounded shadow">
            <form onSubmit={handleAsk}>
                <label className="block font-medium text-gray-700 mb-1">Ask your mentor:</label>
                <input
                  type="text"
                  value="{input}"
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="e.g. How do I say 'good night' in Italian?"
                  className="w-full border border-gray-300 rounded px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-pink-500"
                  required
                  />
                  <button
                    type="submit"
                    className="bg-pink-600 hover:bg-pink-700 text-white font-semibold px-6 py-2 rounded"
                    disabled={loading}
                  >
                    {loading ? 'Asking...' : 'Ask'}
                </button>
            </form>

            {response && (
                <div className="mt-6 p-4 border border-gray-200 rounded bg-gray-50">
                    <p className="text-sm text-gray-600 font-semibold mb-1">Mentor's answer:</p>
                    <p className="text-gray-800">{response}</p>
                </div>
            )}
        </div>
    );
};

export default MentorChat;