import configparser

relative_path_to_configuration = './HW17/configurations/config_file.ini'
config = configparser.RawConfigParser()
config.read(relative_path_to_configuration)


def get_resource_url():
    return config.get('resource_data', 'resource_url')


def get_valid_user_data():
    return (config.get('user_data', 'valid_username'),
            config.get('user_data', 'valid_user_password'))


def get_invalid_user_data():
    return (config.get('user_data', 'invalid_username'),
            config.get('user_data', 'invalid_user_password'))


def get_blocked_user_data():
    return config.get('user_data', 'blocked_username')


def get_browser_id():
    return config.get('browser_data', 'browser_id')
