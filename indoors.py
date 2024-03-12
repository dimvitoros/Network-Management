#!/usr/bin/python

from mininet.node import Controller, OVSKernelSwitch,  Host
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def myNetwork():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6653)

    info( '*** Add switches/APs\n')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', position='1519.0,460.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', position='789.0,98.0,0')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='377.0,649.0,0')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='386.0,197.0,0')

    info( '*** Add hosts/stations\n')
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='587.0,524.0,0', range=0)
    sta7 = net.addStation('sta7', ip='10.0.0.7',
                           position='898.0,237.0,0', range=0)
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='553.0,191.0,0', range=0)
    sta8 = net.addStation('sta8', ip='10.0.0.8',
                           position='999.0,99.0,0', range=0)
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='531.0,715.0,0', range=0)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='229.0,675.0,0', range=0)
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='367.0,415.0,0', range=0)
    sta10 = net.addStation('sta10', ip='10.0.0.10',
                           position='1582.0,611.0,0', range=0)
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='518.0,98.0,0', range=0)
    sta9 = net.addStation('sta9', ip='10.0.0.9',
                           position='1422.0,331.0,0', range=0)

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(s1, ap2)
    net.addLink(s1, ap3)
    net.addLink(s1, ap4)
    net.addLink(s1, ap1)
    net.addLink(s1, h1)

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('ap4').start([])
    net.get('ap3').start([])
    net.get('ap1').start([])
    net.get('s1').start([c0])
    net.get('ap2').start([])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
