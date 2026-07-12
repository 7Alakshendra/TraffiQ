import { Link } from "react-router-dom"

function Navbar() {
  return (
    <nav className="bg-[#0052CC] text-white px-6 py-4 flex items-center justify-between border-b border-gray-800">
      
      {/* Left — brand */}
      <h1 className="text-xl font-bold text-[#E5F0FF]">TraffiQ</h1>

      {/* Right — nav links */}
      <div className="flex gap-6">
        <Link to="/dashboard" className="hover:text-blue-400 transition">Dashboard</Link>
        <Link to="/cameras" className="hover:text-blue-400 transition">Cameras</Link>
        <Link to="/alerts" className="hover:text-blue-400 transition">Alerts</Link>
      </div>

    </nav>
  )
}

export default Navbar