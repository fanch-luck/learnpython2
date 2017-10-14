#!/usr/bin/python
# _*_ coding:utf-8 _*_

import subprocess, os, time, datetime
import threading
import thread
import codecs

global ip_addresses, flag
ip_addresses = []
flag = False
nowtime = datetime.datetime.now

def find_ips(ip_prefix='192.168.22'):
    # get ip addresses with ip_prefix and save 
    # to ip_addresses

    
    def scan_ip(ip_str):
        # quik ping ips

        cmd = ['ping', '-c', '1', ip_str]
        output = os.popen(' '.join(cmd)).readlines()
        for line in list(output):
            if line:
                if str(line).find('ttl') >= 0:
                    ip_addresses.append(ip_str)
                    print 'find {}'.format(ip_str)
                    break
                else:
                    continue

    for i in xrange(200, 202):
        ip = ip_prefix + '.{}'.format(i)
        thread.start_new_thread(scan_ip, (ip,))

    
def monitor(ipstr):
    filename = ipstr+'.txt'
    file = codecs.open(filename, 'a+', 'utf-8')
    time.sleep(0.1)
    file.write("""\
    ------------------------------------------------
    start ping {0} at {1}
	(if one adress is reachable, 
	a response time(ms) would be recorld)
    ------------------------------------------------
    """.format(ipstr, nowtime().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(0.1)
    cmd = ['ping', ipstr, '-s', '1400']
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    while True:
        ctime = nowtime()
        line = popen.stdout.readline()
        if line:
            reline = line[:-1].decode('utf-8')
            towrite = ''
            temp = ''
            if reline.find('PING') >= 0:
                towrite = '{} '.format(ctime.strftime('%Y-%m-%d %H:%M:%S ')) + reline
            if reline.find('ttl') >= 0:
                retime = ' '.join(reline.split(' ')[-2:])
                towrite = ctime.strftime('%M:%S ') + '{}'.format(retime[6:-3])
            if reline.find('Unreachable') >= 0:
                towrite = ctime.strftime('%Y-%m-%d %H:%M:%S ') + 'no response'
            file.write(towrite+'\n')
        else:
            pass
        if nowtime().strftime('%Y%m%d%H%M%S')[-1:] != '0':
            continue
        else:
            file.write(ctime.strftime('%Y-%m-%d %H:%M:%S ') + 'data saved\n')
            file.close()
            time.sleep(1)
            file = codecs.open(filename, 'a', 'utf-8')
            time.sleep(.1)


def main():
    threads = []
    addrs = ip_addresses
    for addr in addrs:
        threads.append(threading.Thread(target=monitor, args=(addr,)))
    print threads
    starttime = datetime.datetime.now()
    print 'start at ', starttime.strftime('%Y-%m-%d %H:%M:%S')
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    
    endtime = datetime.datetime.now()
    print 'end at ', endtime.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    find_ips()
    time.sleep(10)
    print '\n', len(ip_addresses), 'ip/web addresses are found here:'
    for ip in ip_addresses:
        print ip
    main()

