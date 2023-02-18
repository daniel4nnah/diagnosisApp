import "bootstrap/dist/css/bootstrap.min.css";
//import React, { Component } from "react";
import "../../static/css/estilos.css";
import "../../static/css/ejemplo.css";
import React from "react";
//import axios from "axios";
//import { API_URL } from "../constants";
//import { useForm } from "react-hook-form";
import "../../static/img/avatar.jpg";
import '../../../node_modules/font-awesome/css/font-awesome.min.css';
import { faBook, faCircleInfo, faHome, faMagnifyingGlass, faPlus, faStethoscope, faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";


const Sidebar = () => {
  return (
    <div>
      <header>
        <header class="header" id="header">
          <div class="header_toggle">
            <i class="bx bx-menu" id="header-toggle"></i>
          </div>
          <div
            class="text-black-50 float-end"
            style={{ position: "fixed", top: "10px", right: "80px" }}
          >
            Carlos Becerra
          </div>
          <div
            class="text-black-50 float-end"
            style={{ position: "fixed", top: "30px", right: "80px" }}
          >
            Medico
          </div>
          <div class="header_img">
            <img src="img/avatar.jpg" alt="" />
          </div>
        </header>
      </header>

      <div class="l-navbar" id="nav-bar">
        <nav class="nav">
          <div>
            <a href="#top" class="nav_logo">
              <i class="fa-solid nav_logo-icon"><FontAwesomeIcon icon={faStethoscope} /></i>
              <span class="nav_logo-name">Ultrasonido</span>
            </a>
            <div class="nav_list">
              <a href="#top" class="nav_link active">
              <i class="nav_icon"><FontAwesomeIcon icon={faHome} /></i>

                <span class="nav_name">Home</span>
              </a>
              <a href="#top" class="nav_link">
                <i class="fa-solid nav_icon"><FontAwesomeIcon icon={faPlus} /></i>
                <span class="nav_name">New Case</span>
              </a>
              <a href="#top" class="nav_link">
                <i class="fa-solid nav_icon"><FontAwesomeIcon icon={faUser} /></i>
                <span class="nav_name">Profile</span>
              </a>
              <a href="#top" class="nav_link">
                <i class="fa-solid "><FontAwesomeIcon icon={faBook} /></i>
                <span class="nav_name">User Manual</span>
              </a>
              <a href="#top" class="nav_link">
                <i class="fa-solid nav_icon"><FontAwesomeIcon icon={faCircleInfo} /></i>
                <span class="nav_name">Tech Support</span>
              </a>
              <a href="#top" class="nav_link">
                <i class="fa-solid  nav_icon"><FontAwesomeIcon icon={faMagnifyingGlass} /></i>
                <span class="nav_name">Search</span>
              </a>
            </div>
          </div>
          <a href="#y" class="nav_link">
            <i class="fa-solid nav_icon"><FontAwesomeIcon icon={faBook} /></i>
            <span class="nav_name">Repository</span>
          </a>
        </nav>
      </div>
    </div>
  );
};

export default Sidebar;
