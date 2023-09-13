import React from "react";
import "./App.css";
import BuggyCounter from "./BuggyCounter";
import ErrorBoundary from "./ErrorBoundary";
import LifecycleComponent from "./LifecycleComponent";

function App() {
  return (
    <div className="App">
      <div>
        <h1>React Error Boundary Simulation</h1>

        {/* Simulation 1 */}
        <ErrorBoundary>
          <BuggyCounter />
          <BuggyCounter />
        </ErrorBoundary>

        {/* Simulation 2 */}
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>

        {/* Simulation 3 */}
        <BuggyCounter />
      </div>

      <div className="ex2">
        <h1>React Lifecycle Exercise</h1>
        <LifecycleComponent />
      </div>
    </div>
  );
}

export default App;
