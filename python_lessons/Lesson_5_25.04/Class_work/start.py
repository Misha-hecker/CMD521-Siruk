# DISCLAIMER: This script is for educational purposes only.
# Do not use it for illegal activities. The author is not 
# responsible for any damage caused by this tool.

from scapy.all import IP, ICMP, sr1, Raw
import argparse
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--destination", required=True, help="Destination IP address")
parser.add_argument("-c", "--count", type=int, default=4, help="Number of echo requests to send")
parser.add_argument("-t", "--timeout", type=int, default=1, help="Timeout in seconds")
parser.add_argument("-s", "--source", help="Spoofed Source IP address (Optional)")
args = parser.parse_args()

dstIP = args.destination
count = args.count
timeout = args.timeout
srcIP = args.source

def ping(host: str, seq: int, timeout: int, src_host: str = None):
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

print(f"\nPinging {dstIP} " + (f"from {srcIP} " if srcIP else "") + "with 32 bytes of data:\n")

sent = 0
received = 0
rtts = []

for i in range(count):
    sent += 1
    result = ping(dstIP, seq=i, timeout=timeout, src_host=srcIP)

    if result:
        received += 1
        rtts.append(result["rtt"])
        
        if result["rtt"] < 1:
            time_str = "time<1ms"
        else:
            time_str = f"time={int(result['rtt'])}ms"

        print(f"Reply from {result['src']}: bytes=32 {time_str} TTL={result['ttl']}")
    else:
        print("Request timed out.")


lost = sent - received
loss_percent = int((lost / sent) * 100) if sent > 0 else 0

print(f"\nPing statistics for {dstIP}:")
print(f"    Packets: Sent = {sent}, Received = {received}, Lost = {lost} ({loss_percent}% loss),")

if rtts:
    print(f"Approximate round trip times in milli-seconds:")
    print(f"    Minimum = {int(min(rtts))}ms, Maximum = {int(max(rtts))}ms, Average = {int(sum(rtts)/len(rtts))}ms")
