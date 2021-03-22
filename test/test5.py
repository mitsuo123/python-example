#!/usr/bin/python
# -*- coding: utf-8 -*-

apple_price = 200
# 変数moneyに数値1000を代入してください
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# moneyとtotal_priceの比較結果によって条件を分岐してください
if money > total_price:
    print('りんごを'+str(count)+'個買いました')
    print('残額は'+str(money-total_price)+'円です')

elif money == total_price:
    print('りんごを'+str(count)+'個買いました')
    print('残額はなくなりました')
    
else: 
    print('買えませんでした')