import "./App.css"
import { BrowserRouter as Router } from "react-router-dom"
import React, { useState } from "react"
import Home from "./components/home"
import AuthContext from "./context/AuthProvider"

export default function App() {
	const [auth, setAuth] = useState({})

	return (
		<Router>
			<AuthContext.Provider value={{ auth, setAuth }}>
				{<Home auth={auth}></Home>}
			</AuthContext.Provider>
		</Router>
	)
}

// class App extends Component {
// 	constructor() {
// 		super()
// 		console.log(this.props)
// 		this.state = { context: this.props.value }
// 	}

// 	render() {
// 		return (
// 			<Router>
// 				<Home />
// 			</Router>
// 		)
// 	}
// }

// export default App
