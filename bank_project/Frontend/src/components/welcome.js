import "../styles/Welcome.css";
import React, { Component } from "react";
import { Link } from "react-router-dom";
import profile from "../auth/profile";

class Welcome extends Component {
  constructor() {
    super();
    this.state = {};
  }

  render() {
    return (
      <div id="welcome">
        <img
          src="https://media.istockphoto.com/id/1215256045/vector/safe-payment-logo-template-designs-vector-illustration.jpg?s=612x612&w=0&k=20&c=22EA9Y3-gToqirb3PlgCqjnoprrgXyPAvO4_CZmT2Jc="
          alt="bank"
          className="bank-logo"
        />
        <h1 className="center">Modern Banking. Lasting Relationships.</h1>
        <p style={{ marginBottom: "30px" }}>
          From cultivating relationships, to thoughtful client services, to
          offering advanced products and services, we’re driven by one thing:
          you.
        </p>
        <div className="login">
          {profile.userName ? (
            <p className="center">Sign in with a different account:</p>
          ) : (
            <p className="center">Please login to your account</p>
          )}
          <Link to="/login" className="center" style={{ fontSize: "25px" }}>
            {profile.userName ? "Logout" : "Login"}
          </Link>
        </div>
      </div>
    );
  }
}

export default Welcome;
