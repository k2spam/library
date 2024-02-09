import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

import { MainPage } from './pages/main';
import { AboutPage } from './pages/about';

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path="about" element={<AboutPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
