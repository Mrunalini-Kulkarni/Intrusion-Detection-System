/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import TrafficInput from "./components/TrafficInput";
import Results from "./components/Results";
import NetworkGraph from "./components/NetworkGraph";
import "./App.css";

function App() {
  const [results, setResults] = useState({
    portScanDetected: [],
    ddosDetected: [],
  });

  const [networkData, setNetworkData] = useState({
    devices: ["Router1", "Server1", "User1"],
    connections: [["Router1", "Server1"], ["Server1", "User1"]],
  });

  const [intrusions, setIntrusions] = useState([]);

  const handleSimulate = async (trafficLog) => {
    try {
      console.log("Sending traffic log:", trafficLog);
      const response = await fetch("http://127.0.0.1:5000/api/simulate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ traffic_log: trafficLog }),
      });
      const data = await response.json();
      console.log("Received response:", data);

      // Map API response keys to component prop names
      const mappedResults = {
        portScanDetected: data.port_scan_detected || [],
        ddosDetected: data.ddos_detected || [],
      };

      setResults(mappedResults);

      // Update intrusions (for graph highlighting)
      const intrusionDevices = ["Router1", "Server1"]; // Example: Devices involved in intrusions
      setIntrusions(intrusionDevices);
    } catch (error) {
      console.error("Error simulating traffic:", error);
    }
  };

  return (
    <div className="App">
      <h1>Intrusion Detection System (IDS) Simulator</h1>
      <TrafficInput onSimulate={handleSimulate} />
      <Results
        portScanDetected={results.portScanDetected}
        ddosDetected={results.ddosDetected}
      />
      <NetworkGraph
        devices={networkData.devices}
        connections={networkData.connections}
        intrusions={intrusions}
      />
    </div>
  );
}

export default App;