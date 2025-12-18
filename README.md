# portfolio_optimization_using_python
#  Portfolio Optimization Using Python


This project implements **Mean-Variance Portfolio optimization** using Python.It helps to optimize the asset allocation by checking correlation with different asset class and maximizing the Sharpe Ratio which is one of the key features when one tries to diversify or even optimize the portfolio.

---

The objective of this project is to construct an optimal investment portfolio using historical market data by applying the mean–variance optimization framework. The portfolio is designed to achieve the best possible trade-off between return and risk by minimizing volatility for a given level of expected return. By incorporating multiple exchange-traded funds (ETFs) representing different market segments and asset classes, the study also aims to demonstrate the role of diversification in improving risk-adjusted performance, as measured by the Sharpe ratio.

---

##  Methodology
- Data source: **Yahoo Finance (yfinance)**
- Returns: **Log returns**
- Risk measure: **Annualized covariance matrix**
- Optimization: **Sharpe Ratio maximization**
- Solver: **Sequential Least Squares Programming (SLSQP)**

---

##  Assets Used
| Asset | Description |
|-----|------------|
| NIFTYBEES.NS | NIFTY 50 ETF |
| JUNIORBEES.NS | NIFTY Next 50 ETF |
| BANKBEES.NS | Bank NIFTY ETF |
| ITBEES.NS | IT Sector ETF |
| GOLDBEES.NS | Gold ETF (diversifier) |

---

##  Constraints
- Fully invested portfolio (weights sum to 1)
- No short selling
- Maximum allocation per asset: 50%  (This helps to diversify the portfolio because in short term one asset can give higher return than other but to average out a good return in long run we need asset or sectoral etfs which have negative correlation with each other which will help portfolio to retain its capital health even in a bearish market.)

---

##  Results
**Optimal Portfolio Allocation**
NIFTYBEES.NS: 43.44%
JUNIORBEES.NS: 8.68%
BANKBEES.NS: 1.09%
ITBEES.NS: 0.00%
GOLDBEES.NS: 46.79%



**Performance Metrics**
- Expected Annual Return: **18.02%**
- Volatility: **9.34%**
- Sharpe Ratio: **1.54**

---

##  Key Insights
- Gold significantly improves risk-adjusted returns due to low correlation with equities
- Broad market exposure dominates sectoral bets
- Sector ETFs with high volatility are penalized

---

##  Limitations
- Assumes historical returns repeat in the future
- No transaction costs or rebalancing
- Static covariance assumption

---

##  Technologies Used
- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- yfinance

---

##  How to Run
```bash
pip install yfinance numpy pandas scipy matplotlib
python portfolio.py

