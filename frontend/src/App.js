import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
//import Ejemplo from './components/ejemplo'
import "./App.css";
import Login from "./components/Login";
//import Welcome from "./components/welcome";
//import Body from "./components/vtc/body";
//import Header from "./components/Header";
import Header1 from "./components/vtc/Header1";
/* import Cuerpo from "./components/Cuerpo";
import Sidebar from "./components/vtc/Sidebar";
import Greting from "./components/Greting";   */
//import Menu from "./components/Menu";
function App() {
  return (
    <div >
      {/* <Sidebar/>
      <Greting/>
      <Cuerpo/>  */}
      <Header1/>
      <Login/> 
      
      
    </div>
  );

}

export default App;