import "../../styles/Unauthorized.css"
import React, { Component } from "react"
import { Link } from "react-router-dom"

class Unauthorized extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div id="unauthorized">
				<h2>Cant get you there!</h2>
				<h2>Please sign in first:</h2>
				<Link to="/login">Login</Link>
			</div>
		)
	}
}

export default Unauthorized
