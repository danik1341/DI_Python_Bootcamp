import React from "react";
import "../App.css";

function SuperheroCard({ superhero, onClick }) {
  return (
    <div className="superhero-card" onClick={() => onClick(superhero.id)}>
      <img src={superhero.image} alt={superhero.name} />
      <p>{superhero.name}</p>
    </div>
  );
}

export default SuperheroCard;
