import "../styles/Home.css"
import React, { Component } from "react"
import { Route } from "react-router-dom"
import Welcome from "./welcome"
import Transactions from "./transactions"
import Operations from "./operations"
import Breakdown from "./breakdown"
import NavBar from "./navbar"
import Balance from "./balance"
import Login from "./authentication/login"
import Unauthorized from "./authentication/unauthorized"
import SignUp from "./authentication/signUp"

class Home extends Component {
	constructor() {
		super()
		this.state = {}
	}

	getTransactionsPage = () =>
		this.props.auth.user ? <Transactions></Transactions> : <Unauthorized />
	getOperationsPage = () =>
		this.props.auth.user ? <Operations></Operations> : <Unauthorized />
	getBreakdownPage = () =>
		this.props.auth.user ? <Breakdown></Breakdown> : <Unauthorized />

	getAppRoutes = () => {
		return (
			<div className="routs-container">
				<Route exact path="/" render={() => <Welcome />} />
				<Route exact path="/signup" render={() => <SignUp />} />
				<Route exact path="/login" render={() => <Login />} />
				<Route
					exact
					path="/transactions"
					render={() => this.getTransactionsPage()}
				/>
				<Route
					exact
					path="/operations"
					render={() => this.getOperationsPage()}
				/>
				<Route
					exact
					path="/breakdown"
					render={() => this.getBreakdownPage()}
				/>
			</div>
		)
	}

	render() {
		return (
			<div className="App">
				<div className="footer">
					<NavBar></NavBar>
					{this.props.auth.user ? <Balance></Balance> : null}
				</div>
				<div id="bank-interface">{this.getAppRoutes()}</div>
			</div>
		)
	}
}

export default Home
