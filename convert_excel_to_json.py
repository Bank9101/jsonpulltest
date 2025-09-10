import pandas as pd
import json
import os

def convert_excel_to_json():
    """Convert OTOP Excel file to JSON format"""
    try:
        # Read the Excel file
        df = pd.read_excel('otop.xlsx')
        
        # Clean the data - handle NaN values
        df = df.fillna('')
        
        # Convert to dictionary format
        otop_data = []
        for index, row in df.iterrows():
            otop_item = {
                'id': index + 1,
                'product_name': str(row['ชื่อสินค้า OTOP']),
                'local_admin': str(row['อปท.']),
                'district': str(row['อำเภอ']),
                'province': str(row['จังหวัด']),
                'shop_name': str(row['ชื่อสถานที่จัดจำหน่าย']),
                'address': str(row['ที่อยู่']),
                'phone': str(row['เบอร์โทรศัพท์']),
                'latitude': float(row['LAT']) if pd.notna(row['LAT']) and row['LAT'] != '' else None,
                'longitude': float(row['LONG']) if pd.notna(row['LONG']) and row['LONG'] != '' else None
            }
            otop_data.append(otop_item)
        
        # Create static directory if it doesn't exist
        static_dir = os.path.join('staticfiles_build', 'static', 'data')
        os.makedirs(static_dir, exist_ok=True)
        
        # Save as JSON file
        json_file_path = os.path.join(static_dir, 'otop_data.json')
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(otop_data, f, ensure_ascii=False, indent=2)
        
        print(f"Successfully converted {len(otop_data)} OTOP records to JSON")
        print(f"JSON file saved to: {json_file_path}")
        
        # Show some statistics
        valid_coords = sum(1 for item in otop_data if item['latitude'] and item['longitude'])
        print(f"Records with valid coordinates: {valid_coords}")
        
        return json_file_path
        
    except Exception as e:
        print(f"Error converting Excel to JSON: {e}")
        return None

if __name__ == "__main__":
    convert_excel_to_json()