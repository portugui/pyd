from playwright.sync_api import sync_playwright
import time

email=input("email:")
senha=input("senha:")
email2=input("palavra chave:")

with sync_playwright() as p:
    browser= p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()    
    page.goto('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=19&ct=1703341828&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f0%252f%253fstate%253d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3de7776b00-97b4-bc3b-ebd2-f37ce8caf0c2&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c')
    ele=page.locator('//*[@id="i0116"]')
    ele.fill(email)
    time.sleep(2)
    bot=page.locator('//*[@id="idSIButton9"]')
    time.sleep(2)
    bot.click()
    ele=page.locator('//*[@id="i0118"]')
    time.sleep(2)
    ele.fill(senha)
    bot2=page.locator('//*[@id="idSIButton9"]')
    time.sleep(3)
    bot2.click()
    bot3=page.locator('//*[@id="acceptButton"]')
    time.sleep(3)
    bot3.click()
    time.sleep(1)
    bot41=page.locator('//*[@id="idSIButton9"]')
    bot41.click()
    time.sleep(2)
    bot44=page.locator('//*[@id="idBtn_Back"]')
    bot44.click()
    bot45=page.locator('//*[@id="idSIButton9"]')
    bot45.click()
    bot5=page.locator('[name=email2]')
    time.sleep(3)
    bot5.click()
    bot6=page.locator('//*[@id="540"]')
    bot6.click
    bot61=page.locator('//*[@id="540"]/span/i[1]/span/i')
    bot61.click()
    bot7=page.locator('//*[@id="Ribbon-540Dropdown"]/div/ul/li[3]/div/ul/li/button/div')
    bot7.click()
    bot8=page.locator('//*[@id="Ribbon-540Dropdown"]/div/ul/li[1]/div/ul/li[9]/button/div/span')
    bot8.click()

    time.sleep(180)

    browser.close()


    
    