#!/bin/bash
echo "Building and running traffic generator container..."
docker build -t traffic-generator containers/
docker run -d --name traffic-gen traffic-generator
echo "Traffic generator running."
