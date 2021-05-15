import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i" ,"--ipaddress" ,dest="ip_address" ,help="ip address")

    (user_input ,arguments) = parse_object.parse_args()

    if user_input.ip_address:
        print("Enter ip address")

    return user_input

def network_scanner(ip_address):
    
    arp_request_packet = scapy.ARP(pdst=ip_address)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet/arp_request_packet

    (answerd_list ,unanswerd_list) = scapy.srp(combined_packet, timeout=1)

    answerd_list.summary()

user_ip_address = get_user_input()

network_scanner(user_ip_address.ip_address)