import {useState , useEffect} from "react"

function CameraMonitor() {
// 1. state to hold the fetched data
  const [cvResult, setCvResult] = useState(null)

  // 2. fetch data when page loads
  useEffect(() => {
    fetch("http://localhost:8000/analyze-frame")
      .then(res => res.json())       // convert response to JavaScript object
      .then(data => setCvResult(data)) // store in state
  }, [])

const corridors = [
    { name: "Silk Board", status: "High", congestion: 78, speed: 12 },
    { name: "MG Road", status: "Moderate", congestion: 45, speed: 22 },
    { name: "Hebbal Flyover", status: "Low", congestion: 18, speed: 38 },
    { name: "Marathalli Brg", status: "Moderate", congestion: 52, speed: 19 },
    { name: "Tin Factory", status: "High", congestion: 81, speed: 9 },
  ]

  return (
     <div className="min-h-screen bg-gray-950 p-6">
    <h1 className="text-white text-2xl font-bold mb-6">Camera Monitor</h1>

    <div className="grid grid-cols-2 gap-4 mt-6">
  {corridors.map((corridor) => (
    <div key={corridor.name} className="bg-gray-800 rounded-lg p-4 border border-gray-700">
      
      {/* Location name */}
      <p className="text-white font-semibold mb-2">{corridor.name}</p>
      
      {/* Video */}
      <video className="w-full rounded" autoPlay muted loop>
        <source src="/annotated.mp4" type="video/mp4" />
      </video>
      
      {/* Status badge */}
      <p className={
        corridor.status === "High" ? "text-red-400 mt-2" :
        corridor.status === "Moderate" ? "text-yellow-400 mt-2" :
        "text-green-400 mt-2"
      }>
        {corridor.status === "High" ? "🔴" : corridor.status === "Moderate" ? "🟡" : "🟢"} {corridor.status}
      </p>
      <div>
      {cvResult ? (
        <p>Density: {cvResult.density}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
    </div>
  ))}
</div>
</div>
  )
}

export default CameraMonitor