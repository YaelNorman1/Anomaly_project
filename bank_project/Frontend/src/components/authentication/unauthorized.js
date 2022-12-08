import "../../styles/Unauthorized.css";
import React, { Component } from "react";
import { Link } from "react-router-dom";

class Unauthorized extends Component {
  constructor() {
    super();
    this.state = {};
  }

  render() {
    return (
      <div id="unauthorized">
        <h1>Can't get you there!</h1>
        <p>Please sign in first</p>
        <Link to="/login" className="center" style={{ fontSize: "25px" }}>
          Login
        </Link>
      </div>
    );
  }
}

export default Unauthorized;
