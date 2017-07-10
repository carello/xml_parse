import untangle

template = '{0:6} {1:18} {2:14} {3}'


def get_data():
    obj = untangle.parse('abbott_devs.xml')
    tot_rows = obj.imdata['totalCount']
    tot_rows = int(tot_rows)
    return tot_rows, obj

def headers():
    print '\n' + (template.format('NODE', 'MODEL', 'SERIAL', 'STATUS'))
    print (template.format('----', '-----', '------', '------'))

    return

def output(nd_list, serial_items, node_items):
    nd_list.sort()
    for x in nd_list:
        print (template.format(*x))

    print "\nDevice count by Serial_num: {0}".format(len(serial_items))
    print "Device count by Node_id: {0}\n".format(len(node_items))


def main():
    t_row, obj = get_data()
    serial_items = set()
    node_items = set()
    nd_list = []
    count = 0
    headers()
    while count < t_row:
        if obj.imdata.dhcpClient[count]['model'] != "N9K-C9508":
            dev_serial = obj.imdata.dhcpClient[count]['id']
            node_id = obj.imdata.dhcpClient[count]['nodeId']
            client_event = obj.imdata.dhcpClient[count]['clientEvent']
            model_type = obj.imdata.dhcpClient[count]['model']
            tmp_list = node_id, model_type, dev_serial, client_event
            nd_list.append(tmp_list)
            serial_items.add(dev_serial)
            node_items.add(node_id)
        count += 1
    output(nd_list, serial_items, node_items)
    return


if __name__ == '__main__':
    main()
