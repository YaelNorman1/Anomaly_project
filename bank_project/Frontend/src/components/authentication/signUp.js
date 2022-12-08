import "../../styles/Signup.css";
import { useRef, useState, useEffect } from "react";
import { Link } from "react-router-dom";
import React from "react";
import axios from "../../api/axios";
import profile from "../../auth/profile";
const SIGNUP_URL = "/user/signup";

const SignUp = () => {
  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [success, setSuccess] = useState(false);
  const userRef = useRef();
  const errRef = useRef();
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    userRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [user, pwd]);

  const handleSubmit = async e => {
    e.preventDefault();

    try {
      axios.interceptors.request.clear();
      const response = await axios.post(
        SIGNUP_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      setUser("");
      setPwd("");
      setSuccess(true);
    } catch (err) {
      if (!err.response) {
        setErrMsg("No Server Response");
      } else if (err.response.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }
      errRef.current.focus();
    }
  };

  return (
    <div className="signup-container">
      {success ? (
        <section>
          <h1>You are signed up!</h1>
          <br />
          <p>
            <Link to="/login">Login</Link>
          </p>
        </section>
      ) : (
        <section>
          <p
            ref={errRef}
            className={errMsg ? "errmsg" : "offscreen"}
            aria-live="assertive"
          >
            {errMsg}
          </p>
          <h1>Register</h1>
          <form onSubmit={handleSubmit}>
            <div className="input-style">
              <input
                type="text"
                id="username"
                ref={userRef}
                autoComplete="off"
                onChange={e => setUser(e.target.value)}
                value={user}
                required
                placeholder="Username"
              />
            </div>
            <div className="input-style">
              <input
                type="password"
                id="password"
                onChange={e => setPwd(e.target.value)}
                value={pwd}
                required
                placeholder="Password"
              />
            </div>
            <br />
            <button
              className="btn btn-primary"
              style={{ margin: "auto", display: "flex" }}
            >
              Sign up
            </button>
          </form>
        </section>
      )}
    </div>
  );
};
export default SignUp;
