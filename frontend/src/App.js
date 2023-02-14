import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
//import Ejemplo from './components/ejemplo'
import "./App.css";
import Login from "./components/Login";
//import Welcome from "./components/welcome";
//import Body from "./components/vtc/body";
//import Header from "./components/Header";
import Header1 from "./components/vtc/Header1";
//import Sidebar from "./components/vtc/sidebar";

function App() {
  return (
    <div >
      <Header1/>
      <Login/>
    </div>
  );

}

export default App;