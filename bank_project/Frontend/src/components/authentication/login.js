import "../../styles/Login.css";
import { useRef, useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import React from "react";
import AuthContext from "../../context/AuthProvider";
import axios from "../../api/axios";
import profile from "../../auth/profile";
const LOGIN_URL = "/user/login";

const Login = () => {
  const { setAuth } = useContext(AuthContext);
  const userRef = useRef();
  const errRef = useRef();

  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

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
        LOGIN_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );

      const accessToken = response.data.accessToken;
      const roles = response.data.roles;

      axios.interceptors.request.use(function (config) {
        config.headers.Authorization = accessToken
          ? `Bearer ${accessToken}`
          : "";
        config.headers.user = accessToken ? `${user}` : "";
        return config;
      });

      profile.userName = user;

      setAuth({ user, pwd, roles, accessToken });
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
    <div className="login-container">
      {success ? (
        <section>
          <h1>You are logged in!</h1>
          <br />
          <p>
            <Link to="/transactions">Go to Home</Link>
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
          <h1>Login</h1>
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
              Login
            </button>
          </form>
          <br />
          <br />
          <hr style={{ margin: "auto" }} />
          <br />
          <div className="center">
            <p>
              Need an Account?
              <br />
              <br />
              <span className="line center">
                <Link to="/signup" style={{ fontSize: "25px" }}>
                  SignUp
                </Link>
              </span>
            </p>
          </div>
        </section>
      )}
    </div>
  );
};
export default Login;
