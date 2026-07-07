import { useState } from "react"
import { useNavigate } from "react-router-dom"

function Login() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("")
    const navigate = useNavigate()

    function handleLogin() {
    if (email === import.meta.env.VITE_DUMMY_EMAIL && password === import.meta.env.VITE_DUMMY_PASSWORD) {
        navigate('/dashboard')
    } else {
        setError("Invalid Credentials")
    }
}

    return (
        <div className="flex min-h-screen items-center justify-center bg-[#f4f1de] p-4 dark:bg-slate-900">
            
            <div className="flex w-full max-w-sm flex-col gap-4 rounded-xl bg-[#3d405b] p-6 shadow-lg border border-slate-200 dark:bg-slate-800 dark:border-slate-700">
                
                <h1 className="text-2xl font-bold text-center text-[#fefae0] dark:text-white">
                    Login
                </h1>

                <input
                    type="email"
                    placeholder="Enter Your Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full rounded-md border border-[#f1faee] p-2 text-sm text-[#f8edeb] placeholder-[#a8dadc] focus:outline-sky-500 dark:bg-[#f4f1de] dark:text-white dark:border-slate-600 dark:placeholder-[#606c38]"
                />

                <input
                    type="password"
                    placeholder="Enter Your Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full rounded-md border border-[#f1faee] p-2 text-sm text-[#f8edeb] placeholder-[#a8dadc] focus:outline-sky-500 dark:bg-[#f4f1de] dark:text-white dark:border-slate-600 dark:placeholder-[#606c38]"
                />

                <button
                    onClick={handleLogin}
                    className="w-full bg-[#f5cac3] text-[#003049] font-medium p-2 rounded-md hover:bg-[#fdf0d5] transition-colors"
                >
                    Login
                </button>

                {/* Error Message */}
                {error && (
                    <p className="text-sm text-red-500 text-center font-medium">
                        {error}
                    </p>
                )}
            </div>
        </div>
    );
}

export default Login;