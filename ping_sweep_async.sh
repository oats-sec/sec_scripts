#!/bin/bash
static_ip="10.10.10."
ping_reps=3

pingit() {
    local host=$1
    local target=$static_ip$host
    local result=$(ping $target -c $ping_reps -n -q)
    local packet_loss=$(echo $result | cut -d "," -f 3)
    if [[ $packet_loss == " 100%"* ]]
    then
        echo "[DOWN] $target $packet_loss"
    else
        echo "[UP] $target $packet_loss"
    fi
}

for i in {0..255}; do pingit $i & done
