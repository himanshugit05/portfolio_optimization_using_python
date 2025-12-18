import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

tickers = [
    'NIFTYBEES.NS',   # NIFTY 50
    'JUNIORBEES.NS',  # NIFTY Next 50
    'BANKBEES.NS',    # Bank Nifty
    'ITBEES.NS',      # IT Index
    'GOLDBEES.NS'     # Gold (diversifier)
]
end_date=datetime.today()
start_date=end_date-timedelta(days=10*365)
print(start_date,end_date)
#download adjusted close prices for the tickers
adj_close_df=pd.DataFrame()
for ticker in tickers:
    data=yf.download(ticker,start=start_date,end=end_date)
    adj_close_df[ticker]=data['Close']
print(adj_close_df.head())

#calculate log normal returns

log_returns=np.log(adj_close_df/adj_close_df.shift(1))
log_returns=log_returns.dropna()

#calculate covariance matrix

cov_matrix=log_returns.cov()*252
print(cov_matrix.head())

#defining portfolio performance metrics

#1.  STANDARD DEVIATION

def standard_deviation(weights,cov_matrix):
    variance=weights.T@cov_matrix@weights       #@ is used for matrix multiplication
    return np.sqrt(variance)


#2.EXPECTED RETURNS ANNUALLY
                  #HERE WE BASICALLY ASSUME THE EXPECTED FUTURE RETURN IS THE SAME AS THE AVERAGE RETURN OF THE PAST

def expected_return(weights,log_returns):
    return np.sum(weights*log_returns.mean())*252


#3.CALCULATE THE SHARPE RATIO

#SR=PORTFOLIO  RETURN - RISK FREE RATE / PORTFOLIO STANDARD DEVIATION

def sharpe_ratio(weights,log_returns,cov_matrix,risk_free_rate):

    return  (expected_return(weights,log_returns)- risk_free_rate)/standard_deviation(weights,cov_matrix)

#usually people assume 2 %    but here Sir told that we can use api from fred and check risk free rate
#but here we will assume 0.0366 directly
risk_free_rate=0.036

print('running perfectly')


#calculating sharpe ratio for the portfolio

def neg_sharpe_ratio(weights,log_returns,cov_matrix,risk_free_rate):
    return -sharpe_ratio(weights,log_returns,cov_matrix,risk_free_rate)
#why? because we want to maximize the sharpe ratio, so we need to minimize the negative of the sharpe ratio
#and we dont have any function to maximize the sharpe ratio so we will minimize the negative one

constraints={'type':'eq','fun':lambda weights:np.sum(weights)-1}
#this is the constraint that the sum of the weights should be 1
bounds=[(0,0.5) for _ in range(len(tickers))]
#setting 0 is because we cant sell the stocks

#here equal weights initially

initial_weights=np.array([1/len(tickers)]*len(tickers))
print(initial_weights)

optimized_results=minimize(neg_sharpe_ratio,initial_weights,args=(log_returns, cov_matrix, risk_free_rate),method='SLSQP',constraints=constraints,bounds=bounds)

print(optimized_results)

optimal_weights=optimized_results.x

print(optimal_weights)
for ticker,weight in zip(tickers,optimal_weights):
    print(f"{ticker}: {weight*100:.2f}%")

print()

optimal_portfolio_return=expected_return(optimal_weights,log_returns)
optimal_portfolio_volatility=standard_deviation(optimal_weights,cov_matrix)
optimal_portfolio_sharpe_ratio=sharpe_ratio(optimal_weights,log_returns,cov_matrix,risk_free_rate)

print(f"Optimal Portfolio Return: {optimal_portfolio_return*100:.2f}%")
print(f"Optimal Portfolio Volatility: {optimal_portfolio_volatility*100:.2f}%")
print(f"Optimal Portfolio Sharpe Ratio: {optimal_portfolio_sharpe_ratio:.2f}")

