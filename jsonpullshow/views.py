from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.conf import settings

# Create your views here.
def index(request):
    # Load OTOP data from JSON file for initial display
    json_file_path = os.path.join(settings.BASE_DIR, 'staticfiles_build', 'static', 'data', 'otop_data.json')
    otop_data = []
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            otop_data = json.load(f)
    except FileNotFoundError:
        otop_data = []
    
    # Filter only items with coordinates for map display
    map_data = [item for item in otop_data if item.get('latitude') and item.get('longitude')]
    
    context = {
        'total_products': len(otop_data),
        'products_with_coords': len(map_data),
        'map_data': map_data[:100],  # Limit to first 100 for performance
    }
    
    rendered = render(request, 'index.html', context)
    return rendered

def search_otop(request):
    """API endpoint for searching OTOP products"""
    query = request.GET.get('q', '').strip()
    province = request.GET.get('province', '').strip()
    district = request.GET.get('district', '').strip()
    has_coords = request.GET.get('coords', '')  # 'true' or 'false'
    
    # Load data from JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'staticfiles_build', 'static', 'data', 'otop_data.json')
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            otop_data = json.load(f)
    except FileNotFoundError:
        return JsonResponse({'results': [], 'total': 0})
    
    # Filter data based on search criteria
    filtered_data = otop_data
    
    if query:
        filtered_data = [
            item for item in filtered_data 
            if query.lower() in item.get('product_name', '').lower() or
               query.lower() in item.get('shop_name', '').lower() or
               query.lower() in item.get('address', '').lower()
        ]
    
    if province:
        filtered_data = [
            item for item in filtered_data 
            if province.lower() in item.get('province', '').lower()
        ]
    
    if district:
        filtered_data = [
            item for item in filtered_data 
            if district.lower() in item.get('district', '').lower()
        ]
    
    if has_coords == 'true':
        filtered_data = [
            item for item in filtered_data 
            if item.get('latitude') and item.get('longitude')
        ]
    
    # Pagination
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 20))
    
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_data = filtered_data[start_idx:end_idx]
    
    return JsonResponse({
        'results': paginated_data,
        'total': len(filtered_data),
        'page': page,
        'per_page': per_page,
        'total_pages': (len(filtered_data) + per_page - 1) // per_page
    })

def get_provinces(request):
    """Get list of unique provinces"""
    json_file_path = os.path.join(settings.BASE_DIR, 'staticfiles_build', 'static', 'data', 'otop_data.json')
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            otop_data = json.load(f)
        
        provinces = sorted(list(set(item.get('province', '') for item in otop_data if item.get('province'))))
        return JsonResponse({'provinces': provinces})
    except FileNotFoundError:
        return JsonResponse({'provinces': []})

def get_districts(request):
    """Get list of districts for a specific province"""
    province = request.GET.get('province', '')
    json_file_path = os.path.join(settings.BASE_DIR, 'staticfiles_build', 'static', 'data', 'otop_data.json')
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            otop_data = json.load(f)
        
        if province:
            districts = sorted(list(set(
                item.get('district', '') 
                for item in otop_data 
                if item.get('province', '').lower() == province.lower() and item.get('district')
            )))
        else:
            districts = sorted(list(set(item.get('district', '') for item in otop_data if item.get('district'))))
        
        return JsonResponse({'districts': districts})
    except FileNotFoundError:
        return JsonResponse({'districts': []})