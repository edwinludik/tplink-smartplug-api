import sys
sys.path.append('../')

from tplink_smartplug import SmartPlug

plug = SmartPlug('192.168.xxx.xxx')

print('real data  %s' % plug.real_data)
