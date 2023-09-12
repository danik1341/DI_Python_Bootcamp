import "./App.css";
import Car from "./Components/Car";
import Color from "./Components/Color";
import Events from "./Components/Events";
import Phone from "./Components/Phone";

function App() {
  return (
    <div className="App">
      <Car />
      <Events />
      <Phone />
      <Color />
    </div>
  );
}

export default App;
