import "../styles/Balance.css"
import React from "react"
import { useState, useEffect } from "react"
import axios from "../api/axios"
const ROUTES_BALANCE = "/balance"

const Balance = () => {
	const [balance, setBalance] = useState("")

	const getBalance = async () => {
		return await axios.get(ROUTES_BALANCE).then((res) => {
			const balance = res.data.balance
			setBalance(balance)
		})
	}

	useEffect(() => {
		getBalance()
	})

	return <div id="balance">balance: {balance}$</div>
}

export default Balance
