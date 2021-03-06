#!/usr/bin/env python

# Monitoring the CPU usage of a Cisco ACE load balancer
# Herward Cooper <coops@fawk.eu> - 2012

# Uses OID .1.3.6.1.4.1.9.9.109.1.1.1.1.8.1

cisco_ace_cpu_default_values = (35, 40)

def inventory_cisco_ace_cpu(checkname, info):
    inventory=[]
    status = int(info[0][0])
    if status < 11:
        inventory.append( (None, None, "cisco_ace_cpu_default_values") )
    return inventory


def check_cisco_ace_cpu(item, params, info):
    warn, crit = params
    state = int(info[0][0])
    perfdata = [ ( "cpu", state, warn, crit ) ]
    if state > crit:
        return (2, "CRITICAL - CPU is %s percent" % state, perfdata)
    elif state > warn:
        return (1, "WARNING - CPU is %s percent" % state, perfdata)
    else:
        return (0, "OK - CPU is %s percent" % state, perfdata)

check_info["cisco_ace_cpu"] = (check_cisco_ace_cpu, "Cisco ACE CPU 5min Avg", 1, inventory_cisco_ace_cpu)

snmp_info["cisco_ace_cpu"] = ( ".1.3.6.1.4.1.9.9.109.1.1.1.1.8", [ "1" ] )