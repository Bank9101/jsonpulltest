from django.core.management.base import BaseCommand
from django.conf import settings
from jsonpullshow.models import OTOPProduct
import json
import os

class Command(BaseCommand):
    help = 'Load OTOP data from JSON file into database'

    def handle(self, *args, **options):
        json_file_path = os.path.join(settings.BASE_DIR, 'staticfiles_build', 'static', 'data', 'otop_data.json')
        
        if not os.path.exists(json_file_path):
            self.stdout.write(
                self.style.ERROR(f'JSON file not found at {json_file_path}')
            )
            return
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                otop_data = json.load(f)
            
            # Clear existing data
            OTOPProduct.objects.all().delete()
            self.stdout.write('Cleared existing OTOP data')
            
            # Load new data
            products = []
            for item in otop_data:
                product = OTOPProduct(
                    product_name=item.get('product_name', ''),
                    local_admin=item.get('local_admin', ''),
                    district=item.get('district', ''),
                    province=item.get('province', ''),
                    shop_name=item.get('shop_name', ''),
                    address=item.get('address', ''),
                    phone=item.get('phone', ''),
                    latitude=item.get('latitude'),
                    longitude=item.get('longitude')
                )
                products.append(product)
            
            # Bulk create for better performance
            OTOPProduct.objects.bulk_create(products, batch_size=1000)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully loaded {len(products)} OTOP products into database')
            )
            
            # Show statistics
            total_products = OTOPProduct.objects.count()
            products_with_coords = OTOPProduct.objects.filter(
                latitude__isnull=False, 
                longitude__isnull=False
            ).count()
            
            self.stdout.write(f'Total products in database: {total_products}')
            self.stdout.write(f'Products with coordinates: {products_with_coords}')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error loading OTOP data: {str(e)}')
            )