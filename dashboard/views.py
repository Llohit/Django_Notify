from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Data
from django.forms.models import model_to_dict
# Create your views here.
@csrf_exempt
def func(request):
    if request.method == 'POST':
        #print(request.method)
        data_dict = json.loads(request.body)
        try:
            data_object = Data.objects.get(device_id=data_dict['device_id'])
            # If the record exists, update its fields
            data_object.tenant_id = data_dict['tenant_id']
            data_object.account_id = data_dict['account_id']
            data_object.device_name = data_dict['device_name']
            data_object.rule_id = data_dict['rule_id']
            data_object.alarm_id = data_dict['alarm_id']
            data_object.alarm_name = data_dict['alarm_name']
            data_object.description = data_dict['description']
            data_object.state = data_dict['state']
            data_object.duration = data_dict.get('duration', "-")
            data_object.created_at = data_dict['created_at']
            data_object.finalized_at = data_dict.get('finalized_at', "-")
            data_object.severity = data_dict['severity']
            # Save the updated record
            data_object.save()
        except Data.DoesNotExist:
            # If the record doesn't exist, create a new one
            data_object = Data.objects.create(
                tenant_id=data_dict['tenant_id'],
                account_id=data_dict['account_id'],
                device_id=data_dict['device_id'],
                device_name=data_dict['device_name'],
                rule_id=data_dict['rule_id'],
                alarm_id=data_dict['alarm_id'],
                alarm_name=data_dict['alarm_name'],
                description=data_dict['description'],
                state=data_dict['state'],
                duration= data_dict.get('duration', "-"),
                created_at=data_dict['created_at'],
                finalized_at= data_dict.get('finalized_at', "-"),
                severity=data_dict['severity']
            )

        return HttpResponse('Ok')
    if(request.method=='GET'):
        records = Data.objects.all()
        account = list(records.values_list('account_id', flat=True))
        print(account)
        data = {}
        for i in account:
            data[i] = Data.objects.filter(account_id=i)
            # print(i+" "+data[i])
        print(data)
        context = {
            #'accounts': account,
            'data': data
        }
        return render(request, 'index.html',context)
    
