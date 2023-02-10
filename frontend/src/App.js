import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import PersonalSalud from "./components/PersonalSalud";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';


/*import Home from "./components/Home";*/

class App extends Component {
  render() {
    return (
      <Fragment>
      <div>
        <header className="App-header">
          <h1> Hola! </h1>
          <button type="button" class="btn btn-primary">Primary</button>
        </header>
      </div>
        <Header />
        <PersonalSalud />
      </Fragment>
    );
  }
}

export default App;