import "../styles/CatagoryItem.css"
import React, { Component } from "react"

class CatagoryItem extends Component {
	constructor() {
		super()
		this.state = {}
	}

	_capitalize = (s) => s[0].toUpperCase() + s.slice(1)

	render() {
		let details = this.props.details
		let category = details.TransactionCategory
		category = this._capitalize(category)
		let sum = details.categorySum
		return (
			<label className="catagoryItem">
				{category}: {sum}
			</label>
		)
	}
}

export default CatagoryItem
