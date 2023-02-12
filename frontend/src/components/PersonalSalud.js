import React from "react";
import axios from "axios";
import { API_URL_MED } from "../constants";
import { useForm } from "react-hook-form";
import 'bootstrap/dist/css/bootstrap.min.css';

const PersonalSalud = () => {

  const createMedico = (data) => {
      console.log("=========??????");
      console.log("data");
      console.log(data);
      console.log("=========??????");
      axios.post(API_URL_MED, data).then(() => {
          console.log('success');
      });
  };

  const { register, handleSubmit } = useForm();


  /*defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };*/

    return (
      /* <Form onSubmit={this.props.user ? this.editStudent : this.createStudent}>  */
      <form onSubmit={handleSubmit(createMedico)}>
        <div>
            <label for="cedulamed">Cédula:</label>
            <input
              type="integer"
              className="form-control" {...register('cedulamed')}
            />
        </div>
        
          <label for="nombresmed">Nombres:</label>
          <input
            type="text"
            className="form-control" {...register('nombresmed')} 
          />
        
          <label for="apellidosmed">Apellidos:</label>
          <input
            type="text"
            className="form-control" {...register('apellidosmed')} 
          />
        
          <label for="telefonomed">Teléfono:</label>
          <input
            type="text"
            className="form-control" {...register('telefonomed')} 
          />
        
          <label for="direccionmed">Dirección:</label>
          <input
            type="text"
            className="form-control" {...register('direccionmed')} 
          />
        
          <label for="userid">Id usuario:</label>
          <input
            type="integer"
            className="form-control" {...register('userid')} 
          />
        
          <label for="hospitalid">Hospital:</label>
          <input
            type="integer"
            className="form-control" {...register('hospitalid')} 
          />
        
        <button type="submit">Send</button>
      </form>
    );
  

}
export default PersonalSalud;