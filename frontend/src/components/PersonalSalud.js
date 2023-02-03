import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewMedicoForm extends React.Component {
  state = {
    cedulamed: "",
    nombresmed: "",
    apellidosmed: "",
    telefonomed: "",
    direccionmed: "",
    userid: "",
    hospitalid: ""
  };

  componentDidMount() {
    if (this.props.medico) {
      const { cedulamed, nombresmed, apellidosmed, telefonomed, direccionmed, userid, hospitalid } = this.props.medico;
      this.setState({ cedulamed, nombresmed, apellidosmed, telefonomed, direccionmed, userid, hospitalid  });
    }
  }

  onChange = e => {
    this.setState({ [e.target.cedulamed]: e.target.value });
  };

  createMedico = e => {
    console.log("antes", this.state);
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/medico/', this.state).then(() => {
        console.log("despues", this.state);
      this.props.resetState();
      this.props.toggle();
    });
  };

  /*editStudent = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };*/

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      
      /* <Form onSubmit={this.props.user ? this.editStudent : this.createStudent}>  */
      <Form onSubmit={this.createMedico}>
        <FormGroup>
          <Label for="cedulamed">Cédula:</Label>
          <Input
            type="integer"
            name="cedulamed"
            onChange={this.onChange}
            value={this.props.cedulamed}
          />
        </FormGroup>
        <FormGroup>
          <Label for="nombresmed">Nombres:</Label>
          <Input
            type="text"
            name="nombresmed"
            onChange={this.onChange}
            value={this.props.nombresmed}
          />
        </FormGroup>
        <FormGroup>
          <Label for="apellidosmed">Apellidos:</Label>
          <Input
            type="text"
            name="apellidosmed"
            onChange={this.onChange}
            value={this.props.apellidosmed}
          />
        </FormGroup>
        <FormGroup>
          <Label for="telefonomed">Teléfono:</Label>
          <Input
            type="text"
            name="telefonomed"
            onChange={this.onChange}
            value={this.props.telefonomed}
          />
        </FormGroup>
        <FormGroup>
          <Label for="direccionmed">Dirección:</Label>
          <Input
            type="text"
            name="direccionmed"
            onChange={this.onChange}
            value={this.props.direccionmed}
          />
        </FormGroup>
        <FormGroup>
          <Label for="userid">Id usuario:</Label>
          <Input
            type="integer"
            name="userid"
            onChange={this.onChange}
            value={this.props.userid}
          />
        </FormGroup>
        <FormGroup>
          <Label for="hospitalid">Hospital:</Label>
          <Input
            type="integer"
            name="hospitalid"
            onChange={this.onChange}
            value={this.props.hospitalid}
          />
        </FormGroup>
        <Button type="submit">Send</Button>
      </Form>
    );
  }
}

export default NewMedicoForm;