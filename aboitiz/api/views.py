from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from base.models import AP_Payment
from .serializers import AP_PaymentSerializer


class AP_PaymentView(ListCreateAPIView):
    queryset = AP_Payment.objects.all()
    serializer_class = AP_PaymentSerializer



















# import logging
# from datetime import datetime, timedelta, time, date

# from decimal import Decimal
# import os
# from digiinsurance.models.aboitiz import AP_Payment, gen_accountno, gen_cashamt, gen_collector, gen_or_no
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from django.db.models import Q

# # logger = logging.getLogger('api.views')

# __all__ = ['DailyCollectionReport','populate_aboitiz']


# def post_aboitiz():
#     today = datetime.now().strftime('%Y-%m-%d')
#     today_time = datetime.now().strftime('%H:%M:%S')
#     cash = gen_cashamt()
#     AP_Payment.objects.create(
#         transaction_date = today,
#         collector_code = "100192",
#         account_number = gen_accountno(),
#         cash_amount = cash,
#         check_amount = None,
#         total_amount = cash,
#         check_number = None,
#         or_no = gen_or_no(),#"F314C2C8D159",
#         teller_code = "U292",
#         time = today_time,
#         payment_date = today,
#         biller = 'ECPAY',
#         user_id = 'L676',
#         account_id = '9765434',
#         account_name = '0',
#         remarks = ''
#     )
#     return 200

# class populate_aboitiz(APIView):
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         try:
#             today = datetime.now().strftime('%Y-%m-%d')
#             today_time = datetime.now().strftime('%H:%M:%S')
#             cash = gen_cashamt()
#             AP_Payment.objects.create(
#             transaction_date = today,
#             collector_code = "100192",
#             account_number = gen_accountno(),
#             cash_amount = cash,
#             check_amount = None,
#             total_amount = cash,
#             check_number = None,
#             or_no = gen_or_no(),#"F314C2C8D159",
#             teller_code = "U292",
#             time = today_time,
#             payment_date = today,
#             biller = 'ECPAY',
#             user_id = 'L676',
#             account_id = '9765434',
#             account_name = '0',
#             remarks = ''
#             )
#             return Response(200)
#         except Exception as e:
#             return Response(e)
#     # def get(self,request):
#     #     os.system('python do_smth.py')
#     #     return Response(
#     #         {
#     #             "Status":True
#     #         }
#     #     )

# class DailyCollectionReport(APIView):
    
#     permission_classes = (AllowAny,)
    
    
#     def get(self,request):
#         start = request.GET.get('transaction_date_start') if request.GET.get('transaction_date_start') else ''
#         end = request.GET.get('transaction_date_end') if request.GET.get('transaction_date_end') else ''
#         time_s = request.GET.get('transaction_time_start') if request.GET.get('transaction_time_start') else ''
#         time_e = request.GET.get('transaction_time_end') if request.GET.get('transaction_time_end') else ''
#         print(start)
#         print(end)
#         print(time_s)
#         print(time_e)
#         # if end_date != None or '' or '0': 
#         # x = AP_Payment.objects.filter(time__gte = time_s).values_list('time')
#         # if  x[0][0]== 0:
#         #     print("bkyvk")
#         # else:
#         #     print(x[0][0])
#         #     print("qqqqq")
#         query = AP_Payment.objects.filter(
#             Q(
#                 Q(transaction_date__range = [start,end])#) & Q(transaction_date__lte = end)
#             ) and
#             Q(
#                 Q(time__range=[time_s, time_e])
#             )
#             ).values(
#                 'collector_code',   
#                 'account_number',   
#                 'cash_amount',      
#                 'check_amount',     
#                 'total_amount',     
#                 'check_number',     
#                 'or_no',            
#                 'teller_code',    
#                 'time'         
#                 ).order_by('-created_at')
                
                
                
#         # query = query.filter(
#         #     time__gte = time_s).filter(
#         #         time__lte = time_e).values(
#         #         'collector_code',   
#         #         'account_number',   
#         #         'cash_amount',      
#         #         'check_amount',     
#         #         'total_amount',     
#         #         'check_number',     
#         #         'or_no',            
#         #         'teller_code',    
#         #         'time'         
#         #         ).order_by('-created_at')
                        
#         return Response(query)
        
#             # Q(transaction_date__lte = end) and
#             # Q(time__gte = time_s) and
#             # Q(time__lte = time_e)
#             # .values(
#             # 'payment_date', 
#             # 'biller', 
#             # 'user_id', 
#             # 'id', #transaction_id
#             # 'transaction_date', 
#             # 'account_id', 
#             # 'account_name', 
#             # 'total_amount',
#             # 'remarks' 

#         #     'collector_code',   
#         #     'account_number',   
#         #     'cash_amount',      
#         #     'check_amount',     
#         #     'total_amount',     
#         #     'check_number',     
#         #     'or_no',            
#         #     'teller_code',    
#         #     'time'         
#         # ).order_by('-created_at')
#         # return Response(query)

