# http[s]?://\S+ => Refer to urlregex.com for perfect regex
import re

# str1 = "I am at https://hello.com theres"
str1 = "I am at https://hello.com theres http://thankYou.com"

url = re.findall('http[s]?://\S+', str1)
print(url)