import React, { useState } from "react";

const Phone = () => {
  const [brand, setBrand] = useState("Samsung");
  const [model, setModel] = useState("Galaxy S20");
  const [color, setColor] = useState("black");
  const [year, setYear] = useState(2020);

  const changeColor = () => {
    setColor("blue");
  };

  return (
    <div>
      <p>Brand: {brand}</p>
      <p>Model: {model}</p>
      <p>Color: {color}</p>
      <p>Year: {year}</p>
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default Phone;
