import React from 'react';
import { Routes, Route } from 'react-router-dom';

const RouterComponent: React.FC = () => {
    return (
        <Routes>
            <Route path="/" />
            <Route path="/india" />
            <Route path="/taiwan" />
            <Route path="/japan" />
            <Route path="/argentina" />
            <Route path="/germany" />
            <Route path="/korea" />
        </Routes>
    );
};

export default RouterComponent;
