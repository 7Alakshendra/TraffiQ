function Dashboard() {

  const corridors = [
    { name: "Silk Board", status: "High", congestion: 78, speed: 12 },
    { name: "MG Road", status: "Moderate", congestion: 45, speed: 22 },
    { name: "Hebbal Flyover", status: "Low", congestion: 18, speed: 38 },
    { name: "Marathalli Brg", status: "Moderate", congestion: 52, speed: 19 },
    { name: "Tin Factory", status: "High", congestion: 81, speed: 9 },
  ]

  const alerts = [
    { corridor: "Silk Board", status: "High", time: "10:45 AM" },
    { corridor: "Tin Factory", status: "High", time: "10:32 AM" },
    { corridor: "MG Road", status: "Moderate", time: "10:15 AM" },
  ]

  const agentRecommendation = "Deploy officer to Silk Board immediately. Tin Factory congestion likely to cascade to Koramangala in 12 minutes. Consider extending green phase on Hosur Road."

  return (
    <div className="min-h-screen bg-gray-950 p-6">

      {/* Page header */}
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-white text-2xl font-bold">Overview</h1>
        <p className="text-gray-400 text-sm">Last updated: 10:45 AM</p>
      </div>

      {/* Stat boxes */}
      <div className="grid grid-cols-3 gap-4 mb-8">
        <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
          <p className="text-gray-400 text-sm">Total Corridors</p>
          <p className="text-white text-3xl font-bold mt-1">5</p>
        </div>
        <div className="bg-gray-800 rounded-lg p-4 border border-red-900">
          <p className="text-gray-400 text-sm">High Alert</p>
          <p className="text-red-400 text-3xl font-bold mt-1">2</p>
        </div>
        <div className="bg-gray-800 rounded-lg p-4 border border-green-900">
          <p className="text-gray-400 text-sm">Normal</p>
          <p className="text-green-400 text-3xl font-bold mt-1">3</p>
        </div>
      </div>

      {/* Corridor status table */}
      <h2 className="text-white text-lg font-semibold mb-4">Corridor Status</h2>
      <div className="flex flex-col gap-2 mb-8">
        {corridors.map((corridor) => (
          <div key={corridor.name} className="bg-gray-800 p-4 rounded-lg border border-gray-700 flex justify-between items-center">
            <p className="text-white font-semibold w-40">{corridor.name}</p>
            <p className="text-gray-400">{corridor.congestion}% congestion</p>
            <p className="text-gray-400">{corridor.speed} kmph</p>
            <p className={
              corridor.status === "High" ? "text-red-400 font-semibold" :
              corridor.status === "Moderate" ? "text-yellow-400 font-semibold" :
              "text-green-400 font-semibold"
            }>
              {corridor.status === "High" ? "🔴" : corridor.status === "Moderate" ? "🟡" : "🟢"} {corridor.status}
            </p>
          </div>
        ))}
      </div>

      {/* Bottom row — alerts + agent */}
      <div className="grid grid-cols-2 gap-6">

        {/* Active alerts */}
        <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
          <h2 className="text-white font-semibold mb-4">Active Alerts</h2>
          <div className="flex flex-col gap-3">
            {alerts.map((alert) => (
              <div key={alert.corridor} className="flex justify-between items-center border-b border-gray-700 pb-2">
                <div>
                  <p className="text-white text-sm font-medium">{alert.corridor}</p>
                  <p className="text-gray-400 text-xs">{alert.time}</p>
                </div>
                <p className={
                  alert.status === "High" ? "text-red-400 text-sm" : "text-yellow-400 text-sm"
                }>
                  {alert.status === "High" ? "🔴" : "🟡"} {alert.status}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Agent recommendation */}
        <div className="bg-gray-800 rounded-lg p-4 border border-blue-900">
          <h2 className="text-white font-semibold mb-4"> Agent Recommendation</h2>
          <p className="text-gray-300 text-sm leading-relaxed">{agentRecommendation}</p>
        </div>

      </div>

    </div>
  )
}

export default Dashboard