error_dict = {
    'code': '0', 'object': NameError, 'name': 'wrongErrorName', 'message': 'no error with name {}'
    'code': '1', 'object': AttributeError, 'name': 'wrongEventName', 'message': 'no event with name {}'
    'code': '2', 'object': TypeError, 'name': 'tooManyEventFunctionParameters', 'message': '{}() tried subscribing with too many parameters'
}

def raise(error_name, data):
    if error_name in error_dict:
        error_data = error_dict[error_name]
        object = error_data['object']
        code = error_data['code']
        message = f'[{code}] ' + data['message'].format(data)
        raise error_object(message)
    else:
        raise('wrongErrorName', error_name)
