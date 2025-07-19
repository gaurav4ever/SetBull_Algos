# Watchlist Alert Setup Guide - Monitor All Stocks with One Alert

## **Step 1: Create Watchlists**

### **Option A: Manual Creation**
1. Go to **Watchlists** tab in TradingView
2. Click **"Create Watchlist"**
3. Name it: "Volatility Squeeze Stocks 1"
4. Add your first ~400 stocks
5. Repeat for "Volatility Squeeze Stocks 2" (remaining ~338 stocks)

### **Option B: Import from CSV**
1. Export your stock symbols from `bb_width_analysis.csv`
2. Use TradingView's import feature
3. Upload the symbol list directly

## **Step 2: Set Up Watchlist Alert**

### **In Alert Dialog:**
1. **Symbols**: Click dropdown → Select **"Watchlist"**
2. **Choose Watchlist**: Select "Volatility Squeeze Stocks 1"
3. **Condition**: "Volatility Squeeze Alert v4.0"
4. **Alert Type**: "Any alert() function call"
5. **Interval**: "Same as chart" (or your preferred timeframe)

### **Alert Settings:**
- **Trigger**: "Once Per Bar" (recommended)
- **Expiration**: Set to your preference
- **Message**: Will use your script's dynamic message

## **Step 3: Repeat for Second Watchlist**
- Create identical alert for "Volatility Squeeze Stocks 2"
- Now you have 2 alerts monitoring all 738 stocks

## **Benefits of This Method:**

✅ **Efficiency**: 2 alerts instead of 738 individual alerts
✅ **Dynamic**: Automatically includes new stocks added to watchlist
✅ **Cost-Effective**: Uses minimal alert quota
✅ **Maintenance**: Easy to manage and update
✅ **Scalable**: Can easily add/remove stocks from watchlists

## **Alert Quota Usage:**
- **Premium Plan**: 400 alerts → You use only 2 (0.5% usage)
- **Expert Plan**: 600 alerts → You use only 2 (0.3% usage)
- **Ultimate Plan**: 1000 alerts → You use only 2 (0.2% usage)

## **Alternative: Screener Method**

If watchlist alerts don't work as expected, you can also:
1. Use TradingView's **Stock Screener**
2. Apply your volatility squeeze conditions
3. Set up screener alerts
4. This will scan all stocks automatically

## **Troubleshooting:**

### **If Watchlist Option Not Available:**
- Ensure you have Premium+ subscription
- Update TradingView to latest version
- Try using screener alerts instead

### **If Too Many Alerts:**
- Adjust your `alert_on_intensity` parameter to be more selective
- Use higher intensity thresholds (1.5+ instead of 1.2)
- Consider time-based filters in your script

## **Pro Tips:**

1. **Test First**: Start with a small watchlist (10-20 stocks) to test
2. **Timeframe Sync**: Ensure all charts use same timeframe
3. **Market Hours**: Consider setting alerts only during market hours
4. **Volume Filter**: Add volume conditions to reduce false signals
5. **Sector Grouping**: Create separate watchlists by sector for better organization 