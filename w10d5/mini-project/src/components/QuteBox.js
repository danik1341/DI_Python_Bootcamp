import React, { useState, useEffect } from "react";
import quotes from "../utils/QuotesDatabase";

function QuoteBox() {
  const [quoteIndex, setQuoteIndex] = useState(getRandomIndex());
  const [backgroundColor, setBackgroundColor] = useState(getRandomColor());
  const [buttonColor, setButtonColor] = useState(getRandomColor());

  useEffect(() => {
    setBackgroundColor(getRandomColor());
    setButtonColor(getRandomColor());
  }, [quoteIndex]);

  function getRandomIndex() {
    return Math.floor(Math.random() * quotes.length);
  }

  function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function generateNewQuote() {
    let newIndex;
    do {
      newIndex = getRandomIndex();
    } while (newIndex === quoteIndex);

    setQuoteIndex(newIndex);
  }

  const { quote, author } = quotes[quoteIndex];

  const quoteStyle = {
    backgroundColor,
    color: "white",
    padding: "20px",
    textAlign: "center",
  };

  const buttonStyle = {
    backgroundColor: buttonColor,
    color: "white",
    padding: "10px 20px",
    border: "none",
    cursor: "pointer",
  };

  return (
    <div style={quoteStyle}>
      <h1>{quote}</h1>
      <p>{author}</p>
      <button style={buttonStyle} onClick={generateNewQuote}>
        Get New Quote
      </button>
    </div>
  );
}

export default QuoteBox;
