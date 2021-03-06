from django.shortcuts import render
from django.utils import timezone
"""Importing models"""
from .models import ItemLost
"""Defining our views"""
def item_list(request):
    """Ordering objects by date of creation"""
    lostitems = ItemLost.objects.filter(added_date__lte=timezone.now()).order_by('added_date')
    """Returning our ordered objects to the view"""
    """Request = everything we receive from the user (in a form for example)"""
    return render(request, 'lostitem/item_list.html', {'lostitems': lostitems})
