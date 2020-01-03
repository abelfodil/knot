import argparse


class SplitAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(SplitAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.split(' '))


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mac-address", help="device's MAC address", required=True)
parser.add_argument("-c", "--command", help="executable and its arguments", required=True, action=SplitAction)
parser.add_argument("-u", "--unknot", help="execute command when device is disconnected", action='store_true', default=False)
parser.add_argument("-i", "--interval", help="polling interval", type=int, default=5)
