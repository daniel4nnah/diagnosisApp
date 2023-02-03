import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import PersonalSalud from "./components/PersonalSalud";

/*import Home from "./components/Home";*/

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <PersonalSalud />
      </Fragment>
    );
  }
}

export default App;