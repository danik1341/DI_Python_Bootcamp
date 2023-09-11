import React from "react";

function UserFavoriteAnimals(props) {
  const { animals } = props;

  return (
    <ul>
      {animals.map((animal, index) => (
        <li key={index}>{animal}</li>
      ))}
    </ul>
  );
}

export default UserFavoriteAnimals;
