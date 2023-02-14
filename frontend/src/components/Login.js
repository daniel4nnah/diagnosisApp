//import React, {Component} from "react";
import React from "react";
import axios from "axios";
import { API_URL } from "../constants";
import { useForm } from "react-hook-form";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

import "../../src/static/css/ejemplo.css";

const Login = () => {
  const createUser = (data) => {
    console.log("=========??????");
    console.log("data");
    console.log(data);
    console.log("=========??????");
    axios.post(API_URL, data).then(() => {
      console.log("success");
    });
  };

  const { register, handleSubmit } = useForm();

  return (
    <div>
      <div id="columna1">
        <form onSubmit={handleSubmit(createUser)}>
          <div class="imgcontainer">
            <b>Ingresar</b>
          </div>

          <div class="container">
            <label for="uname">
              <b>Email</b>
            </label>
            <input
              placeholder="Enter Username"
              name="uname"
              type="email"
              className="form-control"
              {...register("useremail")}
              required
            />

            <label for="psw">
              <b>Contraseña</b>
            </label>
            <input
              placeholder="Enter Password"
              name="psw"
              type="text"
              className="form-control"
              {...register("password")}
              required
            />
            <div>
              <label>Rol:</label>
              <input
                type="text"
                className="form-control"
                {...register("userroleid")}
              />
            </div>
            <button type="submit">Login</button>
            <label>
              <input type="checkbox" checked="checked" name="remember" />
              Recordarme
            </label>
          </div>

          <div class="container" style={{ backgroundColor: "#f1f1f1" }}>
            <span class="psw1">
              No tienes una cuenta aún? <a href="#top">Registrate</a>
            </span>
          </div>

          <div class="container" style={{ backgroundColor: "#f1f1f1" }}>
            <span class="psw">
              Olvidaste tu <a href="#top">contraseña?</a>
            </span>
          </div>
        </form>
      </div>
      <div id="columna2">
        <img
          src="https://s1.significados.com/foto/medicina_sm.jpg"
          class="img-fluid"
          alt="..."
        />
      </div>
    </div>
  );
};

export default Login;
