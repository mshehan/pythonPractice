####################################################################
# CIS 117 Internet Programming
# Lab #2: "SuperMarket Coupons"
####################################################################
# This program awards discounts to it's users based on
# total amount spent. For users who spend less that 10$
# no discount is awarded. For all other users there is
# a discount awarded based on these specifications:
# 10 <= cost < 60 an 8% discount is awarded
# 60 <= cost < 150 a 10% discount is awarded
# 150 <= cost < 210 a 12% discount is awarded
# 210 <= cost a 14% discount is awarded
####################################################################
# the following are variable discounts awarded by total sale price:
DISCOUNT1 = 0 
DISCOUNT2 = 0.08
DISCOUNT3 = 0.10
DISCOUNT4 = 0.12
DISCOUNT5 = 0.14 

def discount(cost):
  if cost < 10.0:
    cost = cost*DISCOUNT1
  elif cost >= 10.0 and cost < 60.0:
    cost = cost*DISCOUNT2
  elif cost >= 60.0 and cost < 150.0:
    cost = cost*DISCOUNT3
  elif cost >= 150.0 and cost < 210.0:
    cost = cost*DISCOUNT4
  else:
    cost = cost*DISCOUNT5
  return cost

print("Hi, Welcome to Super SuperMarket!")
cost = float(input("\nHow much did you spend today? "))
print("Awesome! You spent: $%.2f" % cost)

if not discount(cost) == 0:
  percent_off = int((discount(cost)/cost)*100)
  print("You win a discount coupon of: $%.2f. (%d%% off your purchase)"
        % (discount(cost),percent_off))
        
print("\nAs always, we appreciate your business! Thank you :)")

##########################################################################
#------
#RUNS
#------
#Hi, Welcome to Super SuperMarket!
#
#How much did you spend today? 9.99
#awesome! you spent: $9.99
#
#As always, we appreciate your business! Thank you :)
#>>> ================================ RESTART ================================
#>>> 
#Hi, Welcome to Super SuperMarket!
#
#How much did you spend today? 10.00
#awesome! you spent: $10.00
#You win a discount coupon of: $0.80. (8% off your purchase)
#
#As always, we appreciate your business! Thank you :)
#>>> ================================ RESTART ================================
#>>> 
#Hi, Welcome to Super SuperMarket!
#
#How much did you spend today? 60.01
#awesome! you spent: $60.01
#You win a discount coupon of: $6.00. (10% off your purchase)
#
#As always, we appreciate your business! Thank you :)
#>>> ================================ RESTART ================================
#>>> 
#Hi, Welcome to Super SuperMarket!
#
#How much did you spend today? 150
#awesome! you spent: $150.00
#You win a discount coupon of: $18.00. (12% off your purchase)
#
#As always, we appreciate your business! Thank you :)
#>>> ================================ RESTART ================================
#>>> 
#Hi, Welcome to Super SuperMarket!
#
#How much did you spend today? 210.34
#awesome! you spent: $210.34
#You win a discount coupon of: $29.45. (14% off your purchase)
#
#As always, we appreciate your business! Thank you :)
#>>> 
##########################################################################
