import React, { useState } from "react";
import Garage from "./Garage";

const Car = () => {
  const carInfo = { name: "Ford", model: "Mustang" };
  const [color, setColor] = useState("red");

  return (
    <div>
      <h1>
        This car is {color} {carInfo.model}
      </h1>
      <Garage size="small" />
    </div>
  );
};

export default Car;
