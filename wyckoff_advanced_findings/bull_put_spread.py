"""
here is my attempt at writing a hypothetical bull put spread in code
"""

# obligatory hello world
print("hello world")

# hypothetical bull put spread
price = 110 # fake price

put_sell_strike = 100 # put we sell at a higher strike
put_buy_strike = 95 # put we buy at a lower strike
put_sell_premium = 2.10 # premium we receive
put_buy_premium = 0.85 # premium we pay

# calculations
credit = put_sell_premium - put_buy_premium # money collected upfront
width = put_sell_strike - put_buy_strike # distance between the strikes
max_loss = width - credit # worst case if price falls below strike
breakeven = put_sell_strike - credit # price where i make $0

print(f"here are the stats of the spread: the credit is ${credit * 100}, the width is {width}, the max loss is ${max_loss * 100}, the breakeven price is ${breakeven}")