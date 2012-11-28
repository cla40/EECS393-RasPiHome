from django.template import Context, loader
from piServer.models import UserProfile, Building, Outlet, Alarm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404

@login_required
def index(request):
    print request.user
    building_list = get_list_or_404(Building, owner=request.user)
    return render_to_response('index.html', {'building_list': building_list})

def building(request, building_id):
    print building_id
    building = get_object_or_404(Building, pk=building_id)
    outlets = get_list_or_404(Outlet, buildingID=building_id)
    return render_to_response('building.html', {'building': building, 'outlets': outlets})

def outlet(request, building_id, outlet_id):
    print outlet_id
    building = get_object_or_404(Building, pk=building_id)
    outlet = get_object_or_404(Outlet, pk=outlet_id)
    alarms = get_list_or_404(Alarm, outletID=outlet_id)
    return render_to_response('outlet.html', {'building': building, 'outlet': outlet, 'alarms': alarms})