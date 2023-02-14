//import React, {Component} from "react";
import "../../static/css/navbar.css";
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const Header1 = () => {
  return (
    <div>
      <div class="topnav">
        <div class="topnav-right">
          <a href="#manual">Inicio</a>
          <a href="#contactanos">Contactanos</a>
          <a href="#registrase">Registrarse</a>
          <a class="active" href="#ingresar">
            Ingresar
          </a>
        </div>
      </div>
    </div>
  );
};

export default Header1;
