import React, { Component } from "react";
import "./Exercise.css";

class Exercise extends Component {
  render() {
    const styles = {
      color: "red",
      backgroundColor: "lightblue",
      padding: "10px",
    };
    const style_header = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial",
    };

    return (
      <div>
        <h1 style={styles}>Hello, HTML Tags in React</h1>
        <h1 style={style_header}>Hello, HTML Tags in React</h1>
        <p className="para">This is a paragraph.</p>
        <a href="https://www.example.com">Visit Example.com</a>
        <form>
          <label>
            Name:
            <input type="text" />
          </label>
          <input type="submit" value="Submit" />
        </form>
        <img
          src="https://via.placeholder.com/150"
          alt="Placeholder"
          width="150"
          height="150"
        />
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
        </ul>
      </div>
    );
  }
}

export default Exercise;
