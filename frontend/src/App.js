import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Register from './pages/Register';
import Login from './pages/Login';
import Catalog from './pages/Catalog';

function App() {
  return (
    <Router>
      <nav style={{ margin: 20, textAlign: 'center' }}>
        <Link to="/catalog" style={{ marginRight: 16 }}>Каталог</Link>
        <Link to="/login" style={{ marginRight: 16 }}>Вход</Link>
        <Link to="/register">Регистрация</Link>
      </nav>
      <Routes>
        <Route path="/catalog" element={<Catalog />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="*" element={<Catalog />} />
      </Routes>
    </Router>
  );
}

export default App;
