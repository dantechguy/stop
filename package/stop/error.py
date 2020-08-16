error_dict = {
    'wrongErrorName': {'code': '0', 'object': NameError, 'message': 'no error with name {}'},
    'wrongEventName': {'code': '1', 'object': AttributeError, 'message': 'no event with name {}'},
    'tooManyEventFunctionParameters': {'code': '2', 'object': TypeError, 'message': '{}() was added to an event but had too many parameters'},
}

def throw(error_name, data):
    if error_name in error_dict:
        error_data = error_dict[error_name]
        error_object = error_data['object']
        error_code = error_data['code']
        error_message = f'[{error_code}] ' + error_data['message'].format(data)
        raise error_object(error_message)
    else:
        throw('wrongErrorName', error_name)
