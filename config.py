import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from utils import file


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == 'real_device' or context == 'emulator':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv(
            'APP_WAIT_ACTIVITY'))

        options.set_capability('app', file.path_from_project(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        load_dotenv(dotenv_path=file.path_from_project(
            '.env.bstack'))
        options.set_capability(
            'bstack:options', {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('USER_NAME'),
                'accessKey': os.getenv('ACCESS_KEY'),
            },
        )

    return options