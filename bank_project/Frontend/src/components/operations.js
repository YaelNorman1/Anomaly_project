import "../styles/Operations.css"
import React, { Component } from "react"
import axios from "../api/axios"
import profile from "../auth/profile"

const ROUTES_POST_TRANSACTION = "/transactions"

class Operations extends Component {
	constructor() {
		super()
		this.state = {
			amount: "",
			vendor: "",
			category: "",
		}
	}

	handleInput = (e) => {
		let element = e.target.name
		let value = e.target.value
		this.setState({ [element]: value })
	}

	handleButton = (e) => {
		let amount = this.state.amount
		const vendor = this.state.vendor
		const category = this.state.category
		const user = profile.userName
		let element = e.target.name
		if (element === "withdraw") {
			amount = amount * -1
		}
		this._postTransaction(amount, vendor, category, user)
	}

	_postTransaction = (amount, vendor, category, user) => {
		axios
			.post(ROUTES_POST_TRANSACTION, {
				amount: amount,
				vendor: vendor,
				category: category,
				user: user,
			})
			.then((res) => {})
			.catch((error) => {
				console.log(error)
			})
	}

	render() {
		const amount = this.state.amount
		const vendor = this.state.vendor
		const category = this.state.category
		return (
			<div className="operations-container">
				<h1>Insert Transaction</h1>
				<label>Transaction amount</label>
				<input
					name="amount"
					type="text"
					value={amount}
					onChange={this.handleInput}
				></input>
				<label>Transaction vendor</label>
				<input
					name="vendor"
					type="text"
					value={vendor}
					onChange={this.handleInput}
				></input>
				<label>Transaction catagory</label>
				<input
					name="category"
					type="text"
					value={category}
					onChange={this.handleInput}
				></input>
				<button name="deposit" onClick={this.handleButton}>
					Deposit
				</button>
				<button name="withdraw" onClick={this.handleButton}>
					Withdraw
				</button>
			</div>
		)
	}
}

export default Operations
