import React, { useState, useEffect } from "react";
import "./App.css";
import SuperheroCard from "./components/SuperheroCard";
import superheroesData from "./utils/superheroes.json";

function App() {
  const [superheroes, setSuperheroes] = useState([]);
  const [clickedSuperheroes, setClickedSuperheroes] = useState([]);
  const [currentScore, setCurrentScore] = useState(0);
  const [topScore, setTopScore] = useState(0);

  useEffect(() => {
    setSuperheroes(superheroesData.superheroes);
  }, []);

  const shuffleSuperheroes = () => {
    const shuffledSuperheroes = [...superheroes];
    for (let i = shuffledSuperheroes.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffledSuperheroes[i], shuffledSuperheroes[j]] = [
        shuffledSuperheroes[j],
        shuffledSuperheroes[i],
      ];
    }
    setSuperheroes(shuffledSuperheroes);
  };

  const handleSuperheroClick = (id) => {
    if (clickedSuperheroes.includes(id)) {
      setClickedSuperheroes([]);
      setCurrentScore(0);
    } else {
      const newClickedSuperheroes = [...clickedSuperheroes, id];
      const newCurrentScore = currentScore + 1;
      const newTopScore =
        newCurrentScore > topScore ? newCurrentScore : topScore;

      setClickedSuperheroes(newClickedSuperheroes);
      setCurrentScore(newCurrentScore);
      setTopScore(newTopScore);

      shuffleSuperheroes();
    }
  };

  return (
    <div className="App">
      <nav>
        <h1>Superhero Shuffle Game</h1>
        <div className="scores">
          <p>Current Score: {currentScore}</p>
          <p>Top Score: {topScore}</p>
        </div>
      </nav>
      <div className="superhero-container">
        {superheroes.map((superhero) => (
          <SuperheroCard
            key={superhero.id}
            superhero={superhero}
            onClick={handleSuperheroClick}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
