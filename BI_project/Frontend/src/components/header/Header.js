import '../header/Header.css'

function Header() {
    return (
      <div className="Header">
        <img src={require("../header/Anomaly-logo1.png")} className="logo"/>
        {/* <h1>Anomaly Dashboard</h1> */}
      </div>
    );
  }
  
  export default Header;
  