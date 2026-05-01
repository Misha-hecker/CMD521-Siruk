# DISCLAIMER: This script is for educational purposes only.
# Do not use it for illegal activities. The author is not 
# responsible for any damage caused by this tool.

from scapy.all import IP, ICMP, TCP, sr1, Raw
import argparse
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--destination", required=True, help="Destination IP address")
parser.add_argument("-c", "--count", type=int, default=4, help="Number of echo requests to send")
parser.add_argument("-t", "--timeout", type=int, default=1, help="Timeout in seconds")
parser.add_argument("-s", "--source", help="Spoofed Source IP address (Optional)")
parser.add_argument("--tcp", action="store_true", help="Use TCP SYN ping instead of ICMP")
parser.add_argument("--port", type=int, default=80, help="Port for TCP SYN ping (default: 80)")
parser.add_argument("--random-src", action="store_true", help="Use random source IP")
args = parser.parse_args()

dstIP = args.destination
count = args.count
timeout = args.timeout
srcIP = args.source
use_tcp = args.tcp
port = args.port
random_src = args.random_src

def ping(host: str, seq: int, timeout: int, src_host: str = None):
    """ICMP Echo Request ping"""
    payload = b'abcdefghijklmnopqrstuvwabcdefghi'
    
    packet = IP(dst=host, src=src_host) / ICMP(
        id=os.getpid() & 0xFFFF,
        seq=seq
    ) / Raw(load=payload)

    start = time.time()
    reply = sr1(packet, timeout=timeout, verbose=False)
    rtt = (time.time() - start) * 1000

    if reply is None:
        return None

    return {
        "bytes": len(payload),
        "src": reply[IP].src,
        "ttl": reply[IP].ttl,
        "rtt": rtt
    }

def tcp_syn_ping(host: str, port: int, timeout: int, src_host: str = None, use_random: bool = False):
    """TCP SYN ping"""
    from scapy.all import RandIP
    
    if use_random:
        src = str(RandIP())
    elif src_host:
        src = src_host
    else:
        src = None

    packet = IP(dst=host, src=src) / TCP(dport=port, flags="S")

    start = time.time()
    reply = sr1(packet, timeout=timeout, verbose=False)
    rtt = (time.time() - start) * 1000

    if reply is None:
        return None

    # SYN-ACK (0x12) — порт відкритий, RST (0x04) — порт закритий
    tcp_flags = reply[TCP].flags if reply.haslayer(TCP) else None
    
    return {
        "bytes": 0,
        "src": reply[IP].src,
        "dst": reply[IP].dst,
        "ttl": reply[IP].ttl,
        "rtt": rtt,
        "tcp_flags": tcp_flags
    }

# Вибираємо яку функцію використовувати
ping_func = tcp_syn_ping if use_tcp else ping

print(f"\n{'TCP SYN Ping' if use_tcp else 'ICMP Ping'} to {dstIP}", end="")
if srcIP:
    print(f" from spoofed IP {srcIP}", end="")
elif random_src:
    print(" with random source IPs", end="")
if use_tcp:
    print(f" on port {port}", end="")
print()

print(f"Sending {count} packets with timeout {timeout}s:\n")

sent = 0
received = 0
rtts = []

for i in range(count):
    sent += 1
    
    if use_tcp:
        result = tcp_syn_ping(
            host=dstIP,
            port=port,
            timeout=timeout,
            src_host=srcIP if srcIP else None,
            use_random=random_src
        )
    else:
        result = ping(dstIP, seq=i, timeout=timeout, src_host=srcIP)

    if result:
        received += 1
        rtts.append(result["rtt"])
        
        if result["rtt"] < 1:
            time_str = "time<1ms"
        else:
            time_str = f"time={result['rtt']:.0f}ms"

        if use_tcp:
            flags_str = {0x12: "SYN-ACK (open)", 0x04: "RST (closed)"}.get(
                result.get("tcp_flags"), f"flags={result.get('tcp_flags')}"
            )
            print(f"Reply from {result['src']}: {time_str} TTL={result['ttl']} | {flags_str}")
        else:
            print(f"Reply from {result['src']}: bytes={result['bytes']} {time_str} TTL={result['ttl']}")
    else:
        print("Request timed out.")

lost = sent - received
loss_percent = int((lost / sent) * 100) if sent > 0 else 0

print(f"\nStatistics for {dstIP}:")
print(f"    Packets: Sent = {sent}, Received = {received}, Lost = {lost} ({loss_percent}% loss)")
if rtts:
    print(f"Round Trip Times (RTT):")
    print(f"    Minimum = {min(rtts):.0f}ms")
    print(f"    Maximum = {max(rtts):.0f}ms")
    print(f"    Average = {sum(rtts)/len(rtts):.0f}ms")
else:
    print("    No RTT data available.")
