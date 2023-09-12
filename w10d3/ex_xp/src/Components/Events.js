import React, { useState } from "react";

const Events = () => {
  const [inputText, setInputText] = useState("");
  const [isToggleOn, setIsToggleOn] = useState(true);

  const clickMe = () => {
    alert("I was clicked");
  };

  const handleKeyDown = (e) => {
    if (e.keyCode === 13) {
      alert(`keyEnter: ${inputText}`);
    }
  };

  const toggleState = () => {
    setIsToggleOn(!isToggleOn);
  };

  return (
    <div>
      <div>
        <button onClick={clickMe}>Click Me</button>
      </div>

      <div>
        <input
          type="text"
          placeholder="Type something..."
          onKeyDown={handleKeyDown}
          onChange={(e) => setInputText(e.target.value)}
        />
      </div>

      <div>
        <button onClick={toggleState}>{isToggleOn ? "ON" : "OFF"}</button>
      </div>
    </div>
  );
};

export default Events;
