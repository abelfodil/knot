from shutil import which
from subprocess import run

bluetoothctl_path = which('bluetoothctl')
bluetoothctl_exists = bluetoothctl_path != None


class BluetoothctlDoesNotExist(Exception):
    pass


class BluetoothCommandError(Exception):
    pass


def execute_bluetoothctl_command(command: list):
    if not bluetoothctl_exists:
        raise BluetoothctlDoesNotExist("Please install bluez-utils package.")

    result = run([bluetoothctl_path, '--', *command], capture_output=True)
    stdout = result.stdout.decode('utf-8')
    if result.returncode != 0:
        raise BluetoothCommandError(stdout)
    else:
        return stdout


def get_device_info(mac_address: str):
    return execute_bluetoothctl_command(['info', mac_address])


def is_device_connected(mac_address: str):
    device_info = get_device_info(mac_address).split('\n')
    connected_info = [info for info in device_info if 'Connected:' in info][0]
    return 'yes' in connected_info
