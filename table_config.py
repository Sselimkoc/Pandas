def pd_config():
    options = {
        'display': {
            'max_colwidth': 25,
            'expand_frame_repr': False, 
            'max_rows': 14,
            'max_seq_items': 50, 
            'precision': 4,
            'show_dimensions': False
        },
        'mode': {
            'chained_assignment': None
        }
    }

    for category, option in options.items():
        for op, value in option.items():
            pd.set_option(f'{category}.{op}', value)
