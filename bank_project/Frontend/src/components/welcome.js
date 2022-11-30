import "../styles/Welcome.css"
import React, { Component } from "react"
import { Link } from "react-router-dom"
import profile from "../auth/profile"

class Welcome extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div id="welcome">
				<h1>Welcome to The Chupidala National Bank!</h1>
				{profile.userName ? (
					<h2>Sign in with a different account:</h2>
				) : (
					<h2>Sign in:</h2>
				)}
				<Link to="/login">Login</Link>
			</div>
		)
	}
}

export default Welcome
