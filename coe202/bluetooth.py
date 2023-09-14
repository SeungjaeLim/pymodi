import modi

if __name__ == "__main__":
    bundle = modi.MODI(
        conn_type = 'ble',
        network_uuid='6B9F29CB'
    )
    ir1 = bundle.irs[0]
    ir2 = bundle.irs[1]
    bundle.print_topology_map(print_id=True)

