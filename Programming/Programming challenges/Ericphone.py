print('Welcome to the phone bill calculator')


land_mins = int(input('How many minutes have you used in the last month to landlines?:'))
mob_mins = int(input('How many minutes have you used in the last month to mobile phones?:'))
sms = int(input('How many text messages have you sent this month?:'))
mms = int(input('How many media messages have you sent this month?:'))
data = int(input('How many MB of data hove you downloaded over mobile data?:'))

#Price calculator
land_price = land_mins*10
mob_price = mob_mins*20
sms_price = sms*10
mms_price = mms*20
data_price = data*2

price = land_price+mob_price+sms_price+mms_price+data_price
int(price)
pound_price = price/100

#Print prices

print('You owe:',price,'p Whitch converts to £',pound_price)