# Bypass Wordpress Math Captcha
![alt-text](https://github.com/FabianOnSecurity/bypass-math-captcha/blob/main/images/math_bypass.jpg)
This script bypass the default Math-Protection Captcha of Wordpress. There is no fix in any Captcha-Version to prevent this attack.
## Important notice
This script needs an all-encompassing modification referring to different structures of websites. This script can give you the idea how to bypass.
For example:
```
select = Select(driver.find_element(by=By.NAME, value='wpforms[fields][1]'))
select.select_by_visible_text(<value>)
select = Select(driver.find_element(by=By.NAME, value='wpforms[fields][2]'))
select.select_by_visible_text(<value>)
```

This script is multi-threaded.
## How to use
Install "Selenium" (Firefox Engine) library in your python environment.
```
pip install selenium
```
Modify the Python-Script for automating the Spam-Attack. You can use the example above and fill the Select with a Selector-Program like "CSS-Selector" for Firefox. If File-Upload is necessary, you can mostly return the path to file directly (depends on the website).
## Legal Notice:
Do not use this script for illegal activities. You are responsible for your own actions.
