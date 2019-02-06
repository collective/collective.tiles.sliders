*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  Selenium2Screenshots/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Variables  plone/app/testing/interfaces.py


*** Variables ***

${FOLDER_ID}  a-folder
${DOCUMENT_ID}  a-document
