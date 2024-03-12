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
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', position='1079.0,125.0,0')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='193.0,139.0,0')
    ap6 = net.addAccessPoint('ap6', cls=OVSKernelAP, ssid='ap6-ssid',
                             channel='1', mode='g', position='925.0,582.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='678.0,74.0,0')
    ap7 = net.addAccessPoint('ap7', cls=OVSKernelAP, ssid='ap7-ssid',
                             channel='1', mode='g', position='129.0,682.0,0')
    ap5 = net.addAccessPoint('ap5', cls=OVSKernelAP, ssid='ap5-ssid',
                             channel='1', mode='g', position='1555.0,550.0,0')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', position='1507.0,163.0,0')

    info( '*** Add hosts/stations\n')
    sta8 = net.addStation('sta8', ip='10.0.0.8',
                           position='1695.0,729.0,0', range=0)
    sta10 = net.addStation('sta10', ip='10.0.0.10',
                           position='1084.0,573.0,0', range=0)
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='1704.0,151.0,0', range=0)
    sta11 = net.addStation('sta11', ip='10.0.0.11',
                           position='172.0,584.0,0', range=0)
    sta9 = net.addStation('sta9', ip='10.0.0.9',
                           position='738.0,654.0,0', range=0)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='103.0,238.0,0', range=0)
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='304.0,75.0,0', range=0)
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='1246.0,174.0,0', range=0)
    sta7 = net.addStation('sta7', ip='10.0.0.7',
                           position='1677.0,571.0,0', range=0)
    sta12 = net.addStation('sta12', ip='10.0.0.12',
                           position='253.0,747.0,0', range=0)
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='1056.0,370.0,0', range=0)
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='693.0,230.0,0', range=0)

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(ap7, s1)
    net.addLink(h1, s1)
    net.addLink(s1, ap6)
    net.addLink(s1, ap5)
    net.addLink(s1, ap1)
    net.addLink(s1, ap2)
    net.addLink(s1, ap3)
    net.addLink(s1, ap4)

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('s1').start([c0])
    net.get('ap3').start([])
    net.get('ap1').start([])
    net.get('ap6').start([])
    net.get('ap2').start([])
    net.get('ap7').start([])
    net.get('ap5').start([])
    net.get('ap4').start([])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

