import json
import logging
import os

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response
from selene import browser


def bstack_video():
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{browser.driver.session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY')),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def bstack_page_source_xml():
    allure.attach(
        browser.driver.page_source,
        name='page_source_xml',
        attachment_type=allure.attachment_type.XML
    )


def bstack_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


def web_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def web_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def web_video(browser):
    video_url = f'https://{os.getenv('SELENOID_URL')}video/' + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        try:
            logging.info("INFO Request body: " + json.dumps(json.loads(response.request.body), indent=4))
        except json.JSONDecodeError:
            logging.info("INFO Request body: " + str(response.request.body))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    body = response.request.body
    if isinstance(body, bytes):
        body = json.loads(body.decode('utf-8'))
    allure.attach(
        body=json.dumps(body, indent=4, ensure_ascii=True),
        name="Request body",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )
