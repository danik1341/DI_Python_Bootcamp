import React, { Component } from "react";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: "",
      lastName: "",
      age: "",
      gender: "male",
      destination: "Japan",
      lactoseFree: false,
    };
  }

  handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    const newValue = type === "checkbox" ? checked : value;
    this.setState({
      [name]: newValue,
    });
  };

  render() {
    return (
      <div className="App">
        <h1>Form Processing</h1>
        <FormComponent data={this.state} handleChange={this.handleChange} />
        <EnteredInformation data={this.state} />
      </div>
    );
  }
}

function FormComponent(props) {
  const { data, handleChange } = props;
  const { firstName, lastName, age, gender, destination, lactoseFree } = data;

  return (
    <form>
      <input
        type="text"
        name="firstName"
        placeholder="First Name"
        value={firstName}
        onChange={handleChange}
      />
      <br />
      <input
        type="text"
        name="lastName"
        placeholder="Last Name"
        value={lastName}
        onChange={handleChange}
      />
      <br />
      <input
        type="text"
        name="age"
        placeholder="Age"
        value={age}
        onChange={handleChange}
      />
      <br />
      <label>
        Gender:
        <select name="gender" value={gender} onChange={handleChange}>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </label>
      <br />
      <label>
        Destination:
        <select name="destination" value={destination} onChange={handleChange}>
          <option value="Japan">Japan</option>
          <option value="Australia">Australia</option>
          <option value="USA">USA</option>
          <option value="Other">Other</option>
        </select>
      </label>
      <br />
      <label>
        Lactose Free:
        <input
          type="checkbox"
          name="lactoseFree"
          checked={lactoseFree}
          onChange={handleChange}
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

function EnteredInformation(props) {
  const { data } = props;

  return (
    <div>
      <h2>Entered Information:</h2>
      <p>
        Your name: {data.firstName} {data.lastName}
      </p>
      <p>Your age: {data.age}</p>
      <p>Your gender: {data.gender}</p>
      <p>Your destination: {data.destination}</p>
      <p>Lactose Free: {data.lactoseFree ? "Yes" : "No"}</p>
    </div>
  );
}

export default App;
