def list_to_dict(_list):
    errors = {}
    for field in _list:
        errors.update(field)
    html_errors = ''
    for field, error in errors.items():
        html_errors += '%s' % error
    print(html_errors)
    return html_errors
    
    