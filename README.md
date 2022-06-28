# Bypass Wordpress Math-Captcha
This script bypass the default Math-Protection Captcha of Wordpress.

## Modifying
You have to modify the script for a successfull bruteforce attack, e.g.:

```
select = Select(driver.find_element(by=By.NAME, value='wpforms[fields][1]'))
select.select_by_visible_text(<value>)
select = Select(driver.find_element(by=By.NAME, value='wpforms[fields][2]'))
select.select_by_visible_text(<value>)
```

This script is multi-threaded.
## Legal Notice:
Do not use this script for illegal activities. You are responsible for your own actions.
