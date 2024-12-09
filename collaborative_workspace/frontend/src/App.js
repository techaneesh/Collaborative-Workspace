import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/documents/')
      .then(response => {
        setDocuments(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the documents!', error);
      });
  }, []);

  return (
    <div>
      <h1>Documents</h1>
      <ul>
        {documents.map(doc => (
          <li key={doc.id}>{doc.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
