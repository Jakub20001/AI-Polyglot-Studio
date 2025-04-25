import React from 'react';
import {BrowserRouter as  Router, Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import Learn from './pages/Learn.tsx'; 
import Quiz from './pages/Quiz.tsx';
import Dialogue from './pages/Dialogue.tsx';
import Mentor from './pages/mentor';
import Profile from './pages/Profile.tsx';

import Navbar from './components/Navbar.tsx';

import './styles/global.css';

const App: React.FC = () => {
    return (
        <Router>
            <div className="min-h-screen bg-gray-50 text-gray-800 flex flex-col">
                <Navbar/>
                <main className="flex-grow p-4 sm:p-8">
                    <Routes>
                        <Route path="/" element={<Home/>} />
                        <Route path="/learn" element={<Learn/>} />
                        <Route path="/quiz" element={<Quiz/>}/>
                        <Route path="/dialogue" element={<Dialogue/>}/>
                        <Route path="/mentor" element={<Mentor/>}/>
                        <Route path="/profile" element={<Profile/>}/>
                    </Routes>
                </main>
                <footer className="text-center text-xs text-gray-400 pb-4">
                © 2025 AI Polyglot Studio - All rights reserved
                </footer>
            </div>
        </Router>
    );
};

export default App;

