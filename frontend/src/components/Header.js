import React from "react";
import axios from "axios";
import { API_URL } from "../constants";
import { useForm } from "react-hook-form";


  const Header = () => {

    const createUser = (data) => {
        console.log("=========??????");
        console.log("data");
        console.log(data);
        console.log("=========??????");
        axios.post(API_URL, data).then(() => {
            console.log('success');
        });
    };

    const { register, handleSubmit } = useForm();

    return (
        <form onSubmit={handleSubmit(createUser)}>
            <div>
                <label >Correo:</label>
                <input type="email" className="form-control" {...register('useremail')} />
            </div>
            <div>
                <label >Contraseña:</label>
                <input type="text" className="form-control" {...register('userpassword')} />
            </div>
            <label>Fecha de creación:</label>
            <input type="text" className="form-control" {...register('savedate')} />
            <div>
                <label >Fecha cambio contraseña:</label>
                <input type="text" className="form-control" {...register('changepassworddate')} />
            </div>
            <div>
                <label>Rol:</label>
                <input type="text" className="form-control" {...register('userroleid')} />
            </div>
            <button type="submit" className="btn btn-outline-primary" >
                Send
            </button>

        </form >
    );
}
export default Header;
