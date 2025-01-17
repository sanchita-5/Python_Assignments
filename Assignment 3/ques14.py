# A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent per annum can be earned on alternative investments what would be the minimumlife of the machine to make it a more attractive investment compared to alternative investment?

machine=6000
earn=1000
salvage=2000
rate=0.12
bank=6000
sum=0
for t in range(1,1000):
    total_amount=(1000*t)+salvage
    sum+=total_amount
    amount_bank=bank+(bank*t*rate)
    if (total_amount>amount_bank):
        print(f"Machine becomes more profitable than bank after {t} years")
        print(f"Machine total earning amount in {t} years : ₹ {total_amount} ")
        print(f"bank gave total amount in {t} years : ₹ {amount_bank}")
        break