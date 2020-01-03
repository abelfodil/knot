# knot

## Description

```txt
usage: knot [-h] -m MAC_ADDRESS -c COMMAND [-u] [-w] [-i INTERVAL]

Execute an arbitrary command when a Bluetooth device is connected or
disconnected to the machine.

optional arguments:
  -h, --help            show this help message and exit
  -m MAC_ADDRESS, --mac-address MAC_ADDRESS
                        device's MAC address (default: None)
  -c COMMAND, --command COMMAND
                        command to execute and its arguments (default: None)
  -u, --unknot          execute command when device is disconnected (default:
                        False)
  -w, --wait            wait for a change in state before proceeding (default:
                        False)
  -i INTERVAL, --interval INTERVAL
                        polling interval (default: 5)

Example usage: knot -uw -c "lockscreen" -m AA:BB:CC:DD:EE:FF
```

## Dependencies

- `bluez-utils`
