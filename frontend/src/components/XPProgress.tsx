import React from 'react';

interface XPProgressProps {
    points: number;
    maxPoints?: number;
}

const XPProgress: React.FC<XPProgressProps> = ({ points, maxPoints = 100 }) => {
    const percentage = Math.min((points / maxPoints) * 100, 100);

    return (
        <div className="w-full max-w-md mx-auto">
            <p className="text-sm text-gray-700 mb-1">XP Progress: {points} / {maxPoints}</p>
            <div className="w-full bg-gray-200 rounded-full h-4 shadow-inner">
                <div>
                    className="bg-green-500 h-4 rounded-full transition-all duration-500 ease-in-out"
                    style={{ width: `$(percentage)%`}}
                </div>
            </div>
        </div>
    );
};

export default XPProgress;
