import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
//import React, { Component } from "react";
//import "../../static/css/estilos.css";
//import "../../static/css/ejemplo.css";
//import axios from "axios";
//import { API_URL } from "../constants";
//import { useForm } from "react-hook-form";
//import "../../static/img/avatar.jpg";
//import "../../static/js/script.js";

/* Registro de usuario */
const Cuerpo = () => {
  return (
    <div>
      <div class="container-fluid row" style={{ paddingTop: "30px" }}>
        <h4 class="mb-4">
          Agregar nuevo caso{" "}
          <a
            class="btn text-white"
            style={{ backgroundColor: "#0796d8" }}
            href="#!"
            role="button"
          >
            <i class="fas fa-plus"></i>
          </a>
        </h4>
      </div>
      <div class="container-fluid row" style={{ paddingTop: "30px" }}>
        <h4 class="mb-4">Buscar registro</h4>
      </div>
      <div
        class="input-group input-group-sm"
        style={{
          paddingTop: "0",
          position: "relative",
          paddingRight: "100px",
          paddingLeft: "20px",
        }}
      >
        <input
          type="text"
          class="form-control form-control-lg rounde bg-transparent text-black-50"
          placeholder="Type Keywords"
          aria-label="Type Keywords"
          aria-describedby="basic-addon2"
        />
        <span class="input-group-text border-0" id="basic-addon2">
          <i class="fas fa-search fa-lg" style={{ color: "blue" }}></i>
        </span>
      </div>
      <div class="container-fluid col-sm" style={{ paddingTop: "20px" }}>
        <div class="container-fluid row">
          <h3 class="mb-4">Ver Reportes</h3>
          <p class="mb-4 pb-2 mb-md-5 pb-md-0">Reportes Mensuales</p>
        </div>
        <div class="row row-cols-1 row-cols-md-3 g-4">
          <div class="col">
            <div class="card h-100 card1">
              <i
                class="fa-solid fa-person"
                style={{ color: "#0796d8", scale: "170%" }}
              ></i>
              <br />
              <div class="card-body">
                <h5 class="card-title">Fetos Sanos</h5>
                <button type="button" class="card-text btn btn-danger">
                  59
                </button>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card h-100 card1">
              <i
                class="fa-solid fa-person"
                style={{ color: "#0796d8", scale: "170%" }}
              ></i>
              <br />
              <div class="card-body">
                <h5 class="card-title">Fetos Sanos</h5>
                <button type="button" class="card-text btn btn-warning">
                  59
                </button>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card h-100 card1">
              <i
                class="fa-solid fa-person"
                style={{ color: "#0796d8", scale: "170%" }}
              ></i>
              <br />
              <div class="card-body">
                <h5 class="card-title">Fetos Sanos</h5>
                <button type="button" class="card-text btn btn-success">
                  59
                </button>
              </div>
            </div>
          </div>
        </div>
        <div
          class="container-fluid row"
          style={{paddingTop:"20px", position:"relative"}}
        >
          <button type="button" class="btn btn-success  info">
            Check full Information
          </button>
        </div>
      </div>
    </div>
  );
};
export default Cuerpo;
