# Write a 500-word explanation of Bitcoin stock-to-flow model and make an argument for why it is a bad model?

The Bitcoin stock-to-flow (BTC S2F) model was first published by a bitcoin quant analyst called "planB" in march 2019, the model predicted that the price of BTC will reach $51000 by 2021. Later planB released the BTC Stock-to-Flow Cross Asset Model(BTC-S2FX), a modified version of the original S2F model which also predicted that by 2024 the price of BTC will reach $288,000.

The Bitcoin stock-to-flow is the amount of the current stock of bitcoin divided by the amount produced yearly, which is its flow. It tells us the number of years it will take at the current production rate to produce its available stock.

>SF = stock / flow


The bitcoin halving event which Satoshi implemented as a way of controlling inflation plays a very crucial in the BTC S2F model. The halving takes place after every 210,000 blocks approximately 4 years and cuts the production of new bitcoins by half. This doubles the the BTC S2F, thereby increasing the scarcity of bitcoin which drives it price/value. This makes sense in a traditional economic way, where less supply(scarcity) and more demand drives up prices. Both the S2F and S2FX models are very similiar. In the S2FX model time is removed and other assets like silver and gold are added. The model introduces phase transitions where in each phase BTC is seen as a totally different asset with different properties. 


As optimistic as the BS2F model may seem, it is not a sound model as it is built on the basis of assumptions. 

According to the S2F model BTC will continue to increase with time and assumes that its scarcity will drive price/value. In economics, the value of a commodity is influenced by demand and supply. Therefore in reality there has to be a correspondent increase in demand of bitcoin, which cannot be guaranteed. This model fails if bitcoin doesn't have any characteristics that can increase demand other than its scarcity. 
There are some crypto-currencies whose SF ratio are higher than the BTC S2F but the SF model is not able to predict their prices. If the S2F holds true, it means anyone can create a digital currency and implement the halving event everyday to increase scarcity. This re-echoes the fact that scarcity or limited supply alone cannot increase the value of bitcoin.

Using a simple analogy by Francis Tapon a well known critic of the BTC S2F model, the current world economy is nearly $100 trillion. If one bitcoin will be worth $1 trillion according to S2F, then just 10 bitcoins would be equal to the 2020 global economy.This means that in 2050, there will be about 20 million bitcoins. Therefore, in 2050, if the stock-to-flow prediction is correct, then the bitcoin's market cap would be:
$1 trillion x 20 million coins = 20 x 10^18
If we make the rosy assumption that the world economy grows 10-fold between 2020 and 2050, then we will have a $1,000 trillion economy or a $1015 world economy.Therefore, the bitcoin market cap would be 1,000 times more than the total global economy - which is impossible. From this analogy it can be seen that the BTC S2F method is doomed to fail.

One of the challenges bitcoin has faced in the past and is still experiencing today is slow adoption. This in part has being caused by nonacceptance from traditional financial institutions, the government and large corporations. The BS2F model ignores the fact that as the bitcoin market cap continues to grow, it would be a threat to government issued fiat currencies and CBDCs(Central bank digital currency) and digital assets like gold. If powerful institutions feel threatened by bitcoin's growth according to the S2F model they will try to stop it. Although these powerful organizations cannot destroy bitcoin, they will slow down bitcoin's adoption rate; reducing its demand.

Though the BS2F model may not be able to predict the future of bitcon, but like any other technological innovation bitcoin is here to stay and will definitely disrupt the financial industry.



# (Please show your workings). Yara Inc is listed on the NYSE with a stock price of $40 - the company is not known to pay dividends. We need to price a call option with a strike of $45 maturing in 4 months. The continuously-compounded risk-free rate is 3%/year, the mean return on the stock is 7%/year, and the standard deviation of the stock return is 40%/year. What is the Black-Scholes call price?

**C = [SN(d1)] - [(E/e^rt)N(d2)]**

**d1 = {(ln(S/E) + (r+(σ^2/2)t))/σ*sqrt(t)}**

**d2 = d1 - σ*sqrt(t)**

*C, call_price = ?*

*S, security_price = $40*

*E, strike_price = $45*

*r, risk_free_interest_rate = 3% or 0.03*

*t, date_of_expiration - current_date  = 1/3*

*σ, volatity(std_of_underlying_asset) = 40% or 0.4*  

*N(d), value_of_the_cummulative_density_func* 



>d1 = [ln(40/45) + (0.03 + ((0.4^2)/2)1/3)/(0.4 * sqrt(1/3)]

>d1 = -0.3512

>d2 = -0.3512 - (0.4 * sqrt(1/3))

>d2 = -0.5821



__N(d) from the cummulative normal density table;__



>N(d1) = 0.3632

>N(d2) = 0.2810

>C = [(40 * 0.3632) - (45/( e^(0.03/3) ) * 0.2810)]


>C = 2.01
Therefore the call price = $2.01