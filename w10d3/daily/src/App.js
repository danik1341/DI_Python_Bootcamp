import React, { useState } from "react";
import "./App.css";

function App() {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaSript", votes: 0 },
    { name: "Java", votes: 0 },
  ]);

  const voteForLanguage = (languageName) => {
    setLanguages((prevLanguages) =>
      prevLanguages.map((language) =>
        language.name === languageName
          ? { ...language, votes: language.votes + 1 }
          : language
      )
    );
  };

  return (
    <div>
      <h1>Voting App</h1>
      <ul>
        {languages.map((language) => (
          <li key={language.name}>
            {language.name}: {language.votes} votes
            <button onClick={() => voteForLanguage(language.name)}>Vote</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
