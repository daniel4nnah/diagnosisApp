import React from "react";
import "../App.css";

const arriba = 
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
          <img /*src="{% static 'img/avatar.jpg' %}"*/ alt="" />
        </div>
      </header>
    </header>
    <div class="l-navbar" id="nav-bar">
    <nav class="nav">
        <div>
            <a href="#top" class="nav_logo">
                <i class="fa-solid fa-stethoscope nav_logo-icon"></i>
                <span class="nav_logo-name">Ultrasonido</span>
            </a>
            <div class="nav_list">
                <a href="#top" class="nav_link active">
                    <i class="fas fa-home nav_icon"></i>
                    <span class="nav_name">Home</span>
                </a>
                <a href="#top" class="nav_link">
                    <i class="fa-solid fa-plus nav_icon"></i>
                    <span class="nav_name">New Case</span>
                </a>
                <a href="#top" class="nav_link">
                    <i class="fa-solid fa-user nav_icon"></i>
                    <span class="nav_name">Profile</span>
                </a>
                <a href="#top" class="nav_link">
                    <i class="fa-solid fa-book"></i>
                    <span class="nav_name">User Manual</span>
                </a>
                <a href="#top" class="nav_link">
                    <i class="fa-solid fa-circle-info nav_icon"></i>
                    <span class="nav_name">Tech Support</span>
                </a>
                <a href="#top" class="nav_link">
                    <i class="fa-solid fa-magnifying-glass nav_icon"></i>
                    <span class="nav_name">Search</span>
                </a>
            </div>
        </div>
        <a href="#top" class="nav_link">
            <i class="fa-solid fa-book nav_icon"></i>
            <span class="nav_name">Repository</span>
        </a>
    </nav>
</div>
  </div>
;
const body = 
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
        paddingLeft: "200px",
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
        <i class="fas fa-search fa-lg" style={{ backgroundColor: "blue" }}></i>
      </span>
    </div>
    <div class="container-fluid col-sm" style={{ paddingTop: "blue20px" }}>
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
        style={{ paddingTop: "20px", position: "relative" }}
      >
        <button type="button" class="btn btn-success  info">
          Check full Information
        </button>
      </div>
    </div>
  </div>
;


function ejemplo() {
  return (arriba,body);
}

export default ejemplo;
