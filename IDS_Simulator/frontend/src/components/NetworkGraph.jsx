/* eslint-disable no-unused-vars */
import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

const NetworkGraph = ({ devices, connections, intrusions }) => {
  const svgRef = useRef();

  useEffect(() => {
    if (!devices || !connections) return;

    const width = 800;
    const height = 500;

    // Clear previous graph
    d3.select(svgRef.current).selectAll("*").remove();

    // Create SVG container
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height);

    // Create nodes (devices)
    const nodes = devices.map((device, index) => ({
      id: device,
      x: Math.random() * width,
      y: Math.random() * height,
    }));

    // Create links (connections)
    const links = connections.map((connection) => ({
      source: connection[0],
      target: connection[1],
    }));

    // Draw links
    svg.selectAll("line")
      .data(links)
      .enter()
      .append("line")
      .attr("stroke", "#00ffcc")
      .attr("stroke-width", 2)
      .attr("x1", (d) => nodes.find((n) => n.id === d.source).x)
      .attr("y1", (d) => nodes.find((n) => n.id === d.source).y)
      .attr("x2", (d) => nodes.find((n) => n.id === d.target).x)
      .attr("y2", (d) => nodes.find((n) => n.id === d.target).y);

    // Draw nodes
    const nodeElements = svg.selectAll("circle")
      .data(nodes)
      .enter()
      .append("circle")
      .attr("cx", (d) => d.x)
      .attr("cy", (d) => d.y)
      .attr("r", 10)
      .attr("fill", (d) =>
        intrusions?.includes(d.id) ? "#ff4d4d" : "#00ffcc"
      )
      .attr("stroke", "#ffffff")
      .attr("stroke-width", 2)
      .on("mouseover", function () {
        d3.select(this).attr("fill", "#00b3ff");
      })
      .on("mouseout", function (d) {
        d3.select(this).attr("fill", intrusions?.includes(d.id) ? "#ff4d4d" : "#00ffcc");
      });

    // Add tooltips to nodes
    nodeElements.append("title")
      .text((d) => `Device: ${d.id}`);

    // Add labels
    svg.selectAll("text")
      .data(nodes)
      .enter()
      .append("text")
      .attr("x", (d) => d.x + 15)
      .attr("y", (d) => d.y + 5)
      .text((d) => d.id)
      .attr("font-size", "12px")
      .attr("fill", "#ffffff");
  }, [devices, connections, intrusions]);

  return <svg ref={svgRef}></svg>;
};

export default NetworkGraph;