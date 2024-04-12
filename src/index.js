import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import App from './App';
import { ContextProvider } from './contexts/ContextProvider';
/*
// StrictMode is a tool that helps identify issues with the code
// ContextProvider allows us to use props from parent components
// App.js gets executed here
*/
ReactDOM.render(
  <React.StrictMode>
    <ContextProvider>
      <App />
    </ContextProvider>
  </React.StrictMode>,
  document.getElementById('root'),
);
// All the returned html elements will be put in the element tag w/ 'root' ID in ../public/index.html
