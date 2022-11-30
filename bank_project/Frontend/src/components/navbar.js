import "../styles/Navbar.css"
import React, { Component } from "react"
import { Link } from "react-router-dom"

class NavBar extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div id="main-links">
				<Link to="/">Home</Link>
				<Link to="/transactions">Transactions</Link>
				<Link to="/operations">Operations</Link>
				<Link to="/breakdown">Breakdown</Link>
			</div>
		)
	}
}

export default NavBar
