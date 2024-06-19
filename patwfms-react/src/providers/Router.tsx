import React from 'react';
import { Routes, Route } from 'react-router-dom';

const RouterComponent: React.FC = () => {
    return (
        <Routes>
            <Route path="/" element={<div>US</div>} />
            <Route path="/india" element={<div>India</div>} />
            <Route path="/taiwan" element={<div>Taiwan</div>} />
            <Route path="/japan" element={<div>Japan</div>} />
            <Route path="/argentina" element={<div>Argentina</div>} />
            <Route path="/germany" element={<div>Germany</div>} />
            <Route path="/korea" element={<div>Korea</div>} />
        </Routes>
    );
};

export default RouterComponent;
