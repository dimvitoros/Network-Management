#!/bin/bash

# List of IP addresses of all stations except station 1
ip_addresses=("10.0.0.1" "10.0.0.2" "10.0.0.3" "10.0.0.4" "10.0.0.5" "10.0.0.6" "10.0.0.7" "10.0.0.8" "10.0.0.9" "10.0.0.10")

# Send ping requests to each station
for ip in "${ip_addresses[@]}"; do
    ping -c 5 $ip &
done

