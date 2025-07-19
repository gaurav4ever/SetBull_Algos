#!/usr/bin/env python3
import csv
import sys

def extract_symbols_for_watchlist(csv_file, output_file=None):
    """Extract symbols from CSV and format for TradingView watchlist import"""
    
    symbols = []
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            symbol = row['symbol'].strip()
            if symbol:
                symbols.append(symbol)
    
    # Split into two watchlists (TradingView limit ~400 per watchlist)
    watchlist1 = symbols[:400]
    watchlist2 = symbols[400:]
    
    # Format for TradingView (comma-separated)
    watchlist1_str = ','.join(watchlist1)
    watchlist2_str = ','.join(watchlist2)
    
    print(f"Total symbols: {len(symbols)}")
    print(f"Watchlist 1: {len(watchlist1)} symbols")
    print(f"Watchlist 2: {len(watchlist2)} symbols")
    print("\n" + "="*50)
    
    # Save to files
    with open('watchlist1_symbols.txt', 'w') as f:
        f.write(watchlist1_str)
    
    with open('watchlist2_symbols.txt', 'w') as f:
        f.write(watchlist2_str)
    
    print("Files created:")
    print("- watchlist1_symbols.txt (first 400 symbols)")
    print("- watchlist2_symbols.txt (remaining symbols)")
    print("\nTo import in TradingView:")
    print("1. Create new watchlist")
    print("2. Copy content from watchlist1_symbols.txt")
    print("3. Paste in TradingView watchlist")
    print("4. Repeat for watchlist2_symbols.txt")
    
    return watchlist1, watchlist2

if __name__ == "__main__":
    csv_file = "bb_width_analysis.csv"
    extract_symbols_for_watchlist(csv_file) 