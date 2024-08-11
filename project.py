import os

from appium.options.android import UiAutomator2Options


class Config:
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    platformName: str = os.getenv('PLATFORM_NAME')
    platform_version: str = os.getenv('PLATFORM_VERSION')
    deviceName: str = os.getenv('DEVICE_NAME')
    URL: str = os.getenv('URL')
    app: str = os.getenv('APP')

    def to_driver_options(self):
        options = UiAutomator2Options()
        options.set_capability('remote_url', self.URL)
        options.set_capability('deviceName', self.deviceName)
        options.set_capability('platformName', self.platformName)
        options.set_capability('platformVersion', self.platform_version)
        options.set_capability('app', self.app)
        options.set_capability(
            'bstack:options',
            {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": self.USER_NAME,
                "accessKey": self.ACCESS_KEY,
            },
        )

        return options


config_app = Config()
