import React, { Component } from "react";
import quotes from "../utils/QuotesDatabase";

class QuoteBox extends Component {
  constructor(props) {
    super(props);
    this.state = {
      quoteIndex: this.getRandomIndex(),
      backgroundColor: this.getRandomColor(),
      buttonColor: this.getRandomColor(),
    };
  }

  getRandomIndex() {
    return Math.floor(Math.random() * quotes.length);
  }

  getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  generateNewQuote = () => {
    let newIndex;
    do {
      newIndex = this.getRandomIndex();
    } while (newIndex === this.state.quoteIndex);

    this.setState({
      quoteIndex: newIndex,
      backgroundColor: this.getRandomColor(),
      buttonColor: this.getRandomColor(),
    });
  };

  render() {
    const { quoteIndex, backgroundColor, buttonColor } = this.state;
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
        <button style={buttonStyle} onClick={this.generateNewQuote}>
          Get New Quote
        </button>
      </div>
    );
  }
}

export default QuoteBox;
