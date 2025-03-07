# backend/routes/ids_routes.py

from flask import Blueprint, jsonify, request
from simulation.intrusion_detection import IntrusionDetectionSystem  # Correct import

# Create a Blueprint for IDS routes
ids_bp = Blueprint("ids", __name__)

# Initialize the IDS
ids = IntrusionDetectionSystem()

# Add some devices and connections (for simulation)
ids.add_device("Device1")
ids.add_device("Device2")
ids.add_connection("Device1", "Device2")

@ids_bp.route("/simulate", methods=["POST"])
def simulate_traffic():
    """Simulate network traffic and detect intrusions."""
    data = request.json
    traffic_log = data.get("traffic_log", "")

    # Detect intrusions
    port_scan_indices = ids.detect_port_scan(traffic_log)
    ddos_indices = ids.detect_ddos(traffic_log)

    return jsonify({
        "port_scan_detected": port_scan_indices,
        "ddos_detected": ddos_indices
    })