#!/usr/bin/env python3
import csv
import re
import sys
import argparse
from pathlib import Path

def extract_column_values(csv_file, column_name):
    """Extract symbol and specified column values from CSV"""
    values = {}
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        if column_name not in reader.fieldnames:
            available_columns = ', '.join(reader.fieldnames)
            raise ValueError(f"Column '{column_name}' not found. Available columns: {available_columns}")
        
        for row in reader:
            symbol = row['symbol']
            try:
                value = float(row[column_name])
                values[symbol] = value
            except (ValueError, KeyError) as e:
                print(f"Warning: Error processing {symbol} for column {column_name}: {e}")
                continue
    
    return values

def generate_pine_map_statements(values):
    """Generate Pine Script map.put statements"""
    pine_statements = []
    
    # Sort by value (ascending - lowest first)
    sorted_values = sorted(values.items(), key=lambda x: x[1])
    
    for symbol, value in sorted_values:
        pine_statements.append(f'    map.put(threshold_map, "{symbol}", {value:.2f})')
    
    return pine_statements

def update_pine_file(pine_file, new_map_statements, column_name, values):
    """Update the threshold map in the Pine Script file"""
    
    # Read the current Pine Script file
    with open(pine_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find the start and end of the map initialization section
    # Look for the pattern: if barstate.isfirst ... map.put statements ... // Get threshold for current symbol
    start_pattern = r'if barstate\.isfirst\s*\n'
    end_pattern = r'\n// Get threshold for current symbol'
    
    start_match = re.search(start_pattern, content)
    if not start_match:
        raise ValueError("Could not find 'if barstate.isfirst' in the Pine Script file")
    
    start_pos = start_match.start()
    
    end_match = re.search(end_pattern, content)
    if not end_match:
        raise ValueError("Could not find '// Get threshold for current symbol' in the Pine Script file")
    
    end_pos = end_match.start()
    
    # Create the new map section
    new_map_section = f"""if barstate.isfirst
    // Updated threshold map using column: {column_name}
    // Total symbols: {len(new_map_statements)}
    // Range: {min(values.values()):.2f} to {max(values.values()):.2f}
"""
    
    # Add all map.put statements
    new_map_section += '\n'.join(new_map_statements)
    
    # Replace the old section with the new one
    before_section = content[:start_pos]
    after_section = content[end_pos:]
    
    updated_content = before_section + new_map_section + after_section
    
    # Write the updated content back to the file
    with open(pine_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    return len(new_map_statements)

def list_available_columns(csv_file):
    """List all available columns in the CSV file"""
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return reader.fieldnames

def main():
    parser = argparse.ArgumentParser(description='Update threshold map in Pine Script file based on CSV column')
    parser.add_argument('--csv', default='bb_width_analysis.csv', help='CSV file path (default: bb_width_analysis.csv)')
    parser.add_argument('--pine', default='volatility_squeeze_indicatpor.pine', help='Pine Script file path (default: volatility_squeeze_indicatpor.pine)')
    parser.add_argument('--column', help='Column name from CSV to use for thresholds')
    parser.add_argument('--list-columns', action='store_true', help='List all available columns in CSV')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be updated without making changes')
    
    args = parser.parse_args()
    
    # Check if files exist
    if not Path(args.csv).exists():
        print(f"Error: CSV file '{args.csv}' not found")
        sys.exit(1)
    
    if not Path(args.pine).exists():
        print(f"Error: Pine Script file '{args.pine}' not found")
        sys.exit(1)
    
    # List available columns if requested
    if args.list_columns:
        columns = list_available_columns(args.csv)
        print("Available columns in CSV:")
        for i, col in enumerate(columns, 1):
            print(f"  {i:2d}. {col}")
        return
    
    # Check if column is provided when not listing columns
    if not args.column:
        print("Error: --column argument is required unless using --list-columns")
        print("Use --list-columns to see available columns")
        sys.exit(1)
    
    try:
        # Extract values from CSV
        print(f"Extracting values from column '{args.column}' in {args.csv}...")
        values = extract_column_values(args.csv, args.column)
        
        if not values:
            print("No valid values found in the specified column")
            sys.exit(1)
        
        print(f"Found {len(values)} symbols with valid values")
        print(f"Range: {min(values.values()):.2f} to {max(values.values()):.2f}")
        
        # Generate Pine Script statements
        pine_statements = generate_pine_map_statements(values)
        
        if args.dry_run:
            print("\n=== DRY RUN - No changes will be made ===")
            print(f"Would update {args.pine} with {len(pine_statements)} map entries")
            print("\nFirst 10 entries that would be added:")
            for i, stmt in enumerate(pine_statements[:10]):
                print(f"  {stmt}")
            if len(pine_statements) > 10:
                print(f"  ... and {len(pine_statements) - 10} more entries")
        else:
            # Update the Pine Script file
            print(f"\nUpdating {args.pine}...")
            updated_count = update_pine_file(args.pine, pine_statements, args.column, values)
            print(f"Successfully updated {args.pine} with {updated_count} threshold entries")
            print(f"Updated using column: {args.column}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
# python update_threshold_map.py --column "lowest_p10_normalized_bb_width_percentage"