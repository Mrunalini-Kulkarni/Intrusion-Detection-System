# Test file for Data Structures and Algorithms
# The test file for the Data Structures and Algorithms (DSA) module contains sample code to demonstrate the functionality of the implemented classes and algorithms. It includes tests for the NetworkGraph, pattern matching algorithms (KMP), and the IntrusionDetectionSystem class.

from graph import NetworkGraph
from pattern_matching import kmp_search
from intrusion_detection import IntrusionDetectionSystem

# Test NetworkGraph
graph = NetworkGraph()
graph.add_device("Device1")
graph.add_device("Device2")
graph.add_connection("Device1", "Device2")
print("Devices:", graph.get_devices())
print("Connections for Device1:", graph.get_connections("Device1"))
print("BFS Traversal:", graph.bfs("Device1"))

# Test KMP Algorithm
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print("KMP Matches:", kmp_search(text, pattern))

# Test Intrusion Detection
ids = IntrusionDetectionSystem()
ids.add_device("Device1")
ids.add_device("Device2")
ids.add_connection("Device1", "Device2")
traffic_log = "PORT_SCAN DDOS_ATTACK PORT_SCAN"
print("Port Scan Detected:", ids.detect_port_scan(traffic_log))
print("DDoS Detected:", ids.detect_ddos(traffic_log))