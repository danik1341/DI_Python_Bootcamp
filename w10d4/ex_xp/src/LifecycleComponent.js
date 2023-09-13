import React, { Component } from "react";

class LifecycleComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: "red",
      show: true,
    };
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({ favoriteColor: "yellow" });
    }, 2000);
  }

  shouldComponentUpdate() {
    return true;
  }

  componentDidUpdate() {
    console.log("after update");
  }

  componentWillUnmount() {
    alert("Unmounted");
  }

  handleDeleteClick = () => {
    this.setState({ show: false });
  };

  render() {
    return (
      <div>
        <h2>Favorite Color: {this.state.favoriteColor}</h2>
        {this.state.show && <Child />}
        <button onClick={this.handleDeleteClick}>Delete</button>
      </div>
    );
  }
}

class Child extends Component {
  componentWillUnmount() {
    alert("Unmounted");
  }

  render() {
    return <h3>Hello World!</h3>;
  }
}

export default LifecycleComponent;
