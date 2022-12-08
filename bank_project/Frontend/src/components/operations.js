import "../styles/Operations.css";
import React, { Component } from "react";
import axios from "../api/axios";
import profile from "../auth/profile";

const ROUTES_POST_TRANSACTION = "/transactions";

class Operations extends Component {
  constructor() {
    super();
    this.state = {
      amount: "",
      vendor: "",
      category: "",
    };
  }

  handleInput = e => {
    let element = e.target.name;
    let value = e.target.value;
    this.setState({ [element]: value });
  };

  handleButton = e => {
    let amount = this.state.amount;
    const vendor = this.state.vendor;
    const category = this.state.category;
    const user = profile.userName;
    let element = e.target.name;
    if (element === "withdraw") {
      amount = amount * -1;
    }
    this._postTransaction(amount, vendor, category, user);
  };

  _postTransaction = (amount, vendor, category, user) => {
    axios
      .post(ROUTES_POST_TRANSACTION, {
        amount: amount,
        vendor: vendor,
        category: category,
        user: user,
      })
      .then(res => {})
      .catch(error => {
        console.log(error);
      });
  };

  render() {
    const amount = this.state.amount;
    const vendor = this.state.vendor;
    const category = this.state.category;
    return (
      <div className="operations-container">
        <h1>Insert Transaction</h1>
        <input
          name="amount"
          type="text"
          value={amount}
          onChange={this.handleInput}
          style={{ paddingLeft: "10px" }}
          placeholder="Amount"
        ></input>
        <input
          name="vendor"
          type="text"
          value={vendor}
          onChange={this.handleInput}
          placeholder="Vendor"
          style={{ paddingLeft: "10px" }}
        ></input>
        <input
          name="category"
          type="text"
          value={category}
          onChange={this.handleInput}
          placeholder="Catagory"
          style={{ paddingLeft: "10px" }}
        ></input>
        <div style={{ margin: "20px" }}>
          <button
            name="withdraw"
            className="btn btn-danger"
            onClick={this.handleButton}
          >
            Withdraw
          </button>
          <button
            name="deposit"
            className="btn btn-success"
            style={{ float: "right" }}
            onClick={this.handleButton}
          >
            Deposit
          </button>
        </div>
      </div>
    );
  }
}

export default Operations;
