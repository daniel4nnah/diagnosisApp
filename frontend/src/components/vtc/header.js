import React, {Component} from "react";
import "../../static/css/navbar.css";

const header= <div>
<div class="topnav">
      <div class="topnav-right">
        <a href="#manual">Inicio</a>
        <a href="#contactanos">Contactanos</a>
        <a href="#registrase">Registrarse</a>
        <a class="active" href="#ingresar">Ingresar</a>
      </div>
</div>

</div>


class Header extends Component{
    render(){
        return (header)
    }

}

export default Header


