###### **Booking.com**

Scenarios collection for testing follow actions:
1. User is able to specify age of each child
2. User is required to specify booking date to see booking price


##### Run all tests:

###### Firefox 
`pytest tests --browser firefox --language ru --alluredir=reports`

###### Chrome
`pytest tests --browser chrome --language ru --alluredir=reports`

##### Test result
run `allure serve reports` in project root  -> open browser with testing result

##### Note
`--browser` and `--language` attributes can be omitted(default - firefox and ru)

