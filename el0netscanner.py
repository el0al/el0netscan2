import scapy.all as scapy
import optparse

def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip_range",help="give ip range")
    return parse_object.parse_args()

def combine(input_ip_range,modem_mac):

    arp_request_packet = scapy.ARP(pdst=input_ip_range)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst=modem_mac)

    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswerd_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

(user_input,args) = get_input()
if not user_input.ip_range:
    print("you must give a range")

combine(user_input.ip_range,"ff:ff:ff:ff:ff:ff")