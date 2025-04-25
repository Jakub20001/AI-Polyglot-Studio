import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const Navbar: React.FC = () => {
    const linkClass = ({ isActive }: { isActive: boolean }) =>
        `px-4 py-2 rounded transition ${
            isActive ? 'bg-blue-600 text-white': 'text-gray-700 hover:bg-gray-200'
        }`;
    
    return (
        <nav className="bg-white shadow-sm border-b sticky top-0 z-50">
            <div className="max-w-6xl mx-auto px-4 flex justify-between items-center h-16">
                <Link to="/" className="text-xl font-bold text-blue-600">AI Polyglot Studio</Link>
                <div className="flex space-x-2">
                    <NavLink to="/" className={linkClass}>Home</NavLink>
                    <NavLink to="/learn" className={linkClass}>Learn</NavLink>
                    <NavLink to="/quiz" className={linkClass}>Quiz</NavLink>
                    <NavLink to="/dialogue" className={linkClass}>Dialogue</NavLink>
                    <NavLink to="/mentor" className={linkClass}>Mentor</NavLink>
                    <NavLink to="/profile" className={linkClass}>Profile</NavLink>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;