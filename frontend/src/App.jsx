import { BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Dashboard from "./pages/Dashboard"
import Navbar from "./components/Navbar"
import CameraMonitor from "./pages/CameraMonitor"
import Alerts from "./pages/Alerts"


function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<><Navbar /><Dashboard /></>}/>
      <Route path="/cameras" element={<><Navbar /><CameraMonitor /></>}/>
      <Route path="/alerts" element={<><Navbar /><Alerts /></>}/>
      
    </Routes>
    </BrowserRouter>
  );
}

export default App;
