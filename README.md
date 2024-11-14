# SetBull Turtle Trading Strategy

A custom TradingView indicator that combines multiple technical analysis components to identify potential trading opportunities. This strategy is implemented in Pine Script v5.

## Overview

The strategy consists of two main components:
1. 15-Minute Range vs. ATR Analysis (1:2 Ratio)
2. Buy & Sell Candidate Identification System

## Features

### Component 1: 15-Minute Range Analysis
- Calculates the previous day's ATR (Average True Range)
- Monitors the first 15 minutes of trading (three 5-minute candles)
- Plots horizontal lines for the high and low of the 15-minute range
- Compares the range with ATR to identify potential trading opportunities
- Displays a label indicating if the range meets the criteria (YES/NO with ratio)

### Component 2: Buy/Sell Signal System
- Utilizes multiple EMAs (5, 9, and 50 periods)
- Incorporates RSI (14 periods) for confirmation
- Generates signals based on specific conditions:

#### Buy Signals
- Last 5 candles must close above 5 EMA
- Last 9 candles must close above 9 EMA
- 9th previous candle must be above 50 EMA
- RSI must be above 60
- Only triggers after the 9th 5-minute candle of the day

#### Sell Signals
- Last 5 candles must close below 5 EMA
- Last 9 candles must close below 9 EMA
- 9th previous candle must be below 50 EMA
- RSI must be below 30
- Only triggers after the 9th 5-minute candle of the day

## Visual Indicators
- Green horizontal line: Upper range of the first 15 minutes
- Red horizontal line: Lower range of the first 15 minutes
- Green triangles: Buy signals
- Red triangles: Sell signals
- Labels: Range ratio indicators

## Usage
1. Add the indicator to your TradingView chart
2. The indicator will automatically start monitoring the first 15 minutes of trading
3. Watch for buy/sell signals that appear as triangles above/below the candles
4. Use the range ratio labels to confirm potential trading opportunities

## Requirements
- TradingView account
- Market data for the desired symbol
- 5-minute timeframe charts

## Disclaimer
This indicator is for informational purposes only. Always conduct your own analysis and use proper risk management techniques when trading.
