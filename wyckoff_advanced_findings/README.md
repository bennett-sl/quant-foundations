wyckoff advanced by marco crispino completely changed how i view the market.

the simplest way i can explain this paradigm shift is in automotive terms.

while working at mercedes benz i learned that there are two types of mechanics:
- part swappers
- technicians


    part swappers
see something wrong with a car and instantly just replace it with a new part.

this does not always solve the issue because the part failing could be due to another issue with the car.

if that is the case, then inevitably, the swapped part will fail again because the root cause was never addressed.

    technicians
unlike part swappers, technicians start by first diagnosing the car, exploring every possible cause of failure.

they then make a decision based on all the data from their diagnosis.

this usually leads to better outcomes because they assessed the entire state of the car before making a decision

    wyckoff method
like a technician, wyckoff advanced by marco crispino shows you how to diagnose the market and then make an informed decision.

between the 3 laws (supply and demand, cause and effect, effort vs result), the wyckoff market cycle
(accumulation, markup, distribution, markdown), using the fixed range volume profile to study structures,
and the different value ares within the profile...

wyckoff advanced is truly the step by step guide to gauging the current state of the auction in the market.

(this is an EXTREMELY concise overview of the book, each of these ideas could literally be their own essay)

    options
once you've diagnosed the market you have to actually make a trade to make money(crazy, i know)

this is where options and spreads come into play.

an option is a contract tied to an asset that gives one party the right to buy or sell an asset
at a specific price(strike price) by a certain date (expiration) and the other party an obligation to fulfill that right if exercised.

there are two types of options:
- calls: the right, but not obligation, to buy the asset at the strike price
- puts: the right, but not obligation, to sell the asset at the strike price


a spread is a strategy that involves buying and selling multiple options on the same underlying asset to manage risk
and define potential profit and loss.

now you would think because you already analyzed the state of the market using the wyckoff method
that you're ready to trade options, but no. If it were that easy, everybody would be rich. 

    options part 2

you must first identify the four elements of the option:

- underlying: the asset of the option
- strike: the contractual purchase or sale price
- expiration: the date the contract expires
- premium: the market price of the option

also options usually represent 100 shares of the underlying, so an option quoted at 
$3 will commonly cost 300 per contract.

author note: i believe this is to keep poor and stupid people from trading options

then you must analyze a bunch of metrics like:

- DTE: days to expiration
- ITM(in the money): for a call, this would be a strike below the current underlying price
- ATM(at the money): for a call, this would a strike at the current underlying price
- OTM(out of the money): for a call, this would be a strike above the current underlying price
- Intrinsic Value: the amount by which an option is in the money
- Extrinsic Value: the part of the price representing the possibility of an option hitting
- Breakeven: the stock price at expiration where your P/L(profit/loss) is exactly 0

then you have to analyze a bunch of greek symbols because we(im part greek) invented math and physics.

author note: this is why Jamie Dimon(also greek) is the CEO of chase bank.

    the greeks
- Delta: how much an option moves if the asset moves $1
- Gamma: how fast the delta changes
- Theta: the cost or benefit of time passing
- Vega: how much an option reacts to a change in implied volatility

Implied Volatility or IV is how much the stock will move over the life of the option, expressed as an annualized percentage.

once you understand all this then you can finally look at the option chain where you'll find:

- Bid: the highest price a buyer is currently willing to pay
- Ask: the lowest price a seller is currently willing to accept
- Option Volume: how many contracts have traded during the current session
- Open Interest: the number of contracts that remain open

that's enough terms for now, let's discuss a strategy I like:

    the bull put spread
the idea of the bull put spread is simple, sell a higher strike put and buy a lower strike put.

basically instead of gambling that a stock shoots to the moon, you sell OTM put spreads below market
support and the stock can go up, stay completely flat, or even drop slightly and you still make maximum profit.

I like this because you collect the cash upfront from the OTM put option you sell,
but in exchange if the stock drops below your strike price you are obligated to cover their loss.


the put you buy even lower gives you the right to sell the shares at that price,
so no matter how far the market crashes, your loss is capped.

so you end up making less per trade but you're right more often, you win as long as:

- the stock goes up and both puts expire
- the stock doesn't move and both puts expire
- the stock drops but stays above your strike and both puts expire

so while most trades only have one way to win, the bull put spread as 3.
the catch is your gain is strictly capped at the cash from the put you sold on day one.

to me this is a sick strategy to make an algo out of because you mathematically
have a higher probability of winning. and i love winning.

i will now attempt to code this strategy into an MVP (minimum viable product) using my current python ability.




