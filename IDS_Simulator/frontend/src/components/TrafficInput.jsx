import React, { useState } from "react";

const TrafficInput = ({ onSimulate }) => {
  const [trafficLog, setTrafficLog] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent page refresh
    onSimulate(trafficLog);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={trafficLog}
        onChange={(e) => setTrafficLog(e.target.value)}
        placeholder="Enter traffic log (e.g., PORT_SCAN DDOS_ATTACK PORT_SCAN)"
        rows={5}
        cols={50}
      />
      <br />
      <button type="submit">Simulate</button>
    </form>
  );
};

export default TrafficInput;