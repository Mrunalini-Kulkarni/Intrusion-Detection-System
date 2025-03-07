# This file contains the IntrusionDetectionSystem class, which is responsible for detecting port scanning and DDoS attacks in the network traffic log.
# The class uses the NetworkGraph and pattern matching algorithms to analyze the traffic log and identify suspicious patterns.
# The IntrusionDetectionSystem class provides methods to add devices and connections to the network, as well as detect port scanning and DDoS attacks in the traffic log.

from .graph import NetworkGraph
from .pattern_matching import kmp_search

class IntrusionDetectionSystem:
    def __init__(self):
        self.network = NetworkGraph()

    def add_device(self, device):
        """Add a device to the network."""
        self.network.add_device(device)

    def add_connection(self, device1, device2):
        """Add a connection between two devices."""
        self.network.add_connection(device1, device2)

    def detect_port_scan(self, traffic_log):
        """Detect port scanning activity in the traffic log."""
        # Remove spaces from the traffic log
        traffic_log = traffic_log.replace(" ", "")
        pattern = "PORT_SCAN"
        return kmp_search(traffic_log, pattern)

    def detect_ddos(self, traffic_log):
        """Detect DDoS activity in the traffic log."""
        # Remove spaces from the traffic log
        traffic_log = traffic_log.replace(" ", "")
        pattern = "DDOS_ATTACK"
        return kmp_search(traffic_log, pattern)