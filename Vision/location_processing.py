def get_location_dummy(battery_type) -> list[str]:
    batteries_and_locations: list[list[str]]
    locations: list[str] = ['None']

    batteries_and_locations = [['li-ion', 'li-ion polymer'],
                               ['Batteries Plus: 621 Johnnie Dodds Blvd Plaza at East Cooper, Mount Pleasant, SC 29464',
                                'Staples #0826 - 845 Houston Northcutt Boulevard, Mount Pleasant, SC 29464',
                                'Lowes - 1104 Market Center Blvd, Mount Pleasant, SC 20464-7467',
                                'The Home Depot - 2008 Magwood Dr, Charleston, SC 29414-5747',
                                'Charleston County Landfill - 1344 Bees Ferry Rd, Charleston, SC 29414-7908']
                               ]
    for battery in batteries_and_locations[0]:
        if "Battery type: " + battery == battery_type:
            locations = batteries_and_locations[1]
    return locations


def get_instructions(battery_type) -> str:
    locations: str = 'None'
    batteries_and_instructions : list[list[str]] = [['li-ion', 'li-ion polymer'],
                                     ['Li-ion batteries may pose fire risks! Do not plave batteries or devices '
                                      'containing the batteries into household garbages or recycling bins!\nFor safe '
                                      'disposal...\n1. Remove the battery from its device. \n2. Use non-conductive '
                                      'tape to cover any ports or exposed connections to reduce the risk of shorting. '
                                      '\n3. Place the battery in a plastic bag. \nPuncturing or damaging the battery '
                                      'raises a fire risk. If the battery is swollen, leaking, or damaged, '
                                      'protect the battery by placing it in a non-conductive container (plastic, '
                                      'cardboard), and into a second fire-proof container, if possible. Contact the '
                                      'nearest hazardout waste location at a certified convenience center near you: ']]
    for battery in batteries_and_instructions[0]:
        if "Battery type: " + battery == battery_type:
            locations = batteries_and_instructions[1][0]

    return locations