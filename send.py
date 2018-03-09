import yagmail

yag = yagmail.SMTP(user='137246907@qq.com',password='fhkkznpylzirbhfa',host='smtp.qq.com')

contents = ['看看能否发送成功asdgsagagag']

yag.send('qianye@outlook.com','这是来自Q的a',contents)
