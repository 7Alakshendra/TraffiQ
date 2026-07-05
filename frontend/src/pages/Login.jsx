import { useState } from "react"
import { useNavigate } from "react-router-dom"

function Login(){
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("")
    const navigate = useNavigate()

    function handleLogin(){
        if(email=="admin@traffiq.com" && password === "admin123"){
            navigate('/dashboard')
        }
        else{
            setError("Invalid Credentials")
        }
    }
    return (
        <div>
       <h1> Login Page</h1>
       <input
       type="email"
       placeholder="Enter Your Email"
       value={email}
       onChange={(e)=>setEmail(e.target.value)}
       />

       <br/>
       
       <input
       type="password"
       placeholder="Enter Your Password"
       value={password}
       onChange={(e)=>setPassword(e.target.value)}
       />
       <br />

       <button onClick={handleLogin}>
        Login
      </button>

      {error && <p>{error}</p>}

        </div>
    );
  

}

export default Login;