# Threshold Map Updater

This script allows you to quickly update the threshold map in the volatility squeeze indicator based on any column from your CSV analysis.

## Usage

### 1. List Available Columns
First, see what columns are available in your CSV:

```bash
python3 update_threshold_map.py --list-columns
```

### 2. Update with a Specific Column
Update the Pine Script file using a specific column:

```bash
python3 update_threshold_map.py --column "lowest_p10_normalized_bb_width_percentage"
```

### 3. Dry Run (Preview Changes)
See what would be updated without making changes:

```bash
python3 update_threshold_map.py --column "lowest_p10_normalized_bb_width_percentage" --dry-run
```

### 4. Use Different Files
If your files have different names:

```bash
python3 update_threshold_map.py --csv "my_analysis.csv" --pine "my_indicator.pine" --column "my_column"
```

## Available Columns

Based on your CSV structure, you can use any of these columns:

- `lowest_p10_bb_width` - Raw BB width values
- `lowest_p15_bb_width` - 15th percentile BB width
- `lowest_p20_bb_width` - 20th percentile BB width
- `lowest_p25_bb_width` - 25th percentile BB width
- `lowest_p50_bb_width` - 50th percentile BB width
- `lowest_mean_bb_width` - Mean BB width
- `lowest_min_bb_width` - Minimum BB width
- `lowest_max_bb_width` - Maximum BB width
- `lowest_p10_normalized_bb_width_percentage` - **Recommended** - Normalized percentage
- `lowest_p15_normalized_bb_width_percentage` - Normalized 15th percentile
- `lowest_p20_normalized_bb_width_percentage` - Normalized 20th percentile
- `lowest_p25_normalized_bb_width_percentage` - Normalized 25th percentile
- `lowest_p50_normalized_bb_width_percentage` - Normalized 50th percentile
- `lowest_mean_normalized_bb_width_percentage` - Normalized mean
- `lowest_min_normalized_bb_width_percentage` - Normalized minimum
- `lowest_max_normalized_bb_width_percentage` - Normalized maximum

## Recommended Usage

For the best results with your updated indicator (which now uses normalized BB width percentages), use:

```bash
python3 update_threshold_map.py --column "lowest_p10_normalized_bb_width_percentage"
```

This will:
1. Extract the normalized BB width percentages from your CSV
2. Update the threshold map in the Pine Script file
3. Sort stocks by their squeeze potential (lowest values first)
4. Add a comment showing which column was used and the data range

## Examples

### Example 1: Update with normalized percentages
```bash
python3 update_threshold_map.py --column "lowest_p10_normalized_bb_width_percentage"
```

### Example 2: Preview changes first
```bash
python3 update_threshold_map.py --column "lowest_p15_normalized_bb_width_percentage" --dry-run
```

### Example 3: Use raw BB width values
```bash
python3 update_threshold_map.py --column "lowest_p10_bb_width"
```

## What the Script Does

1. **Reads the CSV**: Extracts symbol and specified column values
2. **Validates data**: Ensures all values are valid numbers
3. **Sorts by value**: Orders stocks from lowest to highest threshold
4. **Updates Pine Script**: Replaces the existing map.put statements
5. **Adds metadata**: Includes comments about the update

## Safety Features

- **Dry-run mode**: Preview changes before applying
- **File validation**: Checks if files exist before processing
- **Error handling**: Gracefully handles invalid data
- **Backup recommendation**: Always backup your Pine Script file before updates

## Troubleshooting

### "Column not found" error
Use `--list-columns` to see available columns in your CSV.

### "File not found" error
Check that your CSV and Pine Script files are in the same directory as the script.

### No values found
The specified column might contain non-numeric data. Check your CSV format. 