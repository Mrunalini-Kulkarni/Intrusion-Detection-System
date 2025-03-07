import React from "react";

const Results = ({ portScanDetected, ddosDetected }) => {
  return (
    <div>
      <h3>Detection Results</h3>
      <p>Port Scan Detected at Indices: {portScanDetected.join(", ")}</p>
      <p>DDoS Detected at Indices: {ddosDetected.join(", ")}</p>
    </div>
  );
};

export default Results;