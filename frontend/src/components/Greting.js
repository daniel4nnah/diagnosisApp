import React from "react";
/* import axios from "axios";
import { API_URL } from "../constants";
import { useForm } from "react-hook-form"; */
import "bootstrap/dist/css/bootstrap.min.css";

/* Registro de usuario */
const Greting = () => {
  return (
    <div class="container-fluid row">
      <div class="container-fluid col-sm" style={{ paddingTop: "20px"}}>
        <div
          class="card text-bg-success mb-3"
          id="card_greetings"
          
          style={{maxWidth:"500px"}}
        >
          <p>
            Buen día, <b style={{color:"#0796d8"}}>Doctor Becerra</b>
          </p>
          <p>Have a nice day at work</p>
        </div>
      </div>
    </div>
  );
};

export default Greting;
