from django.shortcuts import render
import json
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt,name='dispatch')
class BmiView(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get("height")
        w=data.get("weight")
        new_h=h/100
        bmi=w/(new_h**2)
        result={
            "Height" : data.get('height'),
            "Weight" : w,
            "BMI" : round(bmi,2)
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data=json.loads(request.body)
        b_year=data.get("birth_year")
        c_year=data.get("current_year")
        age= c_year - b_year
        return JsonResponse({
            "Age" : age
        }) 
        
@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        data=json.loads(request.body)
        o_marks=data.get("obtained_mark")
        t_marks=data.get("total_mark")
        percent=(o_marks/t_marks)*100
        return JsonResponse({
            "Percentage" : percent
        }) 
        
@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterest(View):
    def post(self,request):
        data=json.loads(request.body)
        p=data.get("principal")
        r=data.get("rate")
        t=data.get("time")
        si=(p*r*t)//100
        return JsonResponse({
            "Principal" : p,
            "Rate" : r,
            "Time" : t,
            "SimpleInterest" : si
        })                   
@method_decorator(csrf_exempt,name='dispatch')
class BillView(View):
    def post(self,request):
        data=json.loads(request.body)
        u=data.get("units")
        r=data.get("rate")
        bill=u*r
        result={
            "Units" : u,
            "Rate" : r,
            "Bill" : bill
        }
        return JsonResponse(result) 
     
@method_decorator(csrf_exempt,name='dispatch')
class Discount(View):
    def post(self,request):
        data=json.loads(request.body)
        p=data.get("price")
        d_p=data.get("discount_percentage")
        D_A=(p * d_p)//100
        F_P=p-D_A
        result={
            "price" : p,
            "discount_percentage" : d_p,
            "discount_amount" : D_A,
            "final_price" : F_P
        }  
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        data=json.loads(request.body)
        c_p=data.get("cost_price")
        s_p=data.get("selling_price")
        profit=s_p - c_p
        result={
            "cost_price" : c_p,
            "selling_price" : s_p,
            "profit" : profit
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        data=json.loads(request.body)  
        b_s=data.get("basic_salary")
        b=data.get("bonus")
        d=data.get("deduction") 
        net_salary=b_s+b-d
        result={
            "basic_salary" :b_s,
            "bonus" : b,
            "deduction" : d,
            "net_salary" : net_salary
        } 
        return JsonResponse(result)    
    
@method_decorator(csrf_exempt,name='dispatch')
class TimeConverter(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get("hours")
        m=h*60
        s=h*3600
        result={
            "hours" : h,
            "minutes" : m,
            "seconds" : s
        } 
        return JsonResponse(result)   
    
@method_decorator(csrf_exempt,name='dispatch')
class FuelCost(View):
    def post(self,request):
        data=json.loads(request.body)
        d=data.get("distance")
        m=data.get("mileage")
        f_price=data.get("fuel_price") 
        fuel_required=d//m
        total_cost=fuel_required*f_price
        result={
            "distance" : d,
            "mileage" : m,
            "fuel_price" : f_price,
            "fuel_required" : fuel_required,
            "total_cost" : total_cost
        } 
        return JsonResponse(result) 
@method_decorator(csrf_exempt,name='dispatch')
class ProductProfit(View):
    def post(self,request):
        data=json.loads(request.body)
        cp=data.get("cost_price")
        sp=data.get("selling_price")
        qty=data.get("quantity")
        tc=cp*qty
        ts=sp*qty
        profit=ts-tc
        result={
            "cost_price" : cp,
            "selling_price" : sp,
            "quantity" : qty,
            "total_cost" : tc,
            "total_sales" : ts,
            "profit" : profit
        }               
        return JsonResponse(result)  
    
@method_decorator(csrf_exempt,name='dispatch')    
class WorkSalary(View):
    def post(self,request):
        data=json.loads(request.body)
        hw=data.get("hours_worked")
        rh=data.get("regular_hours")
        hlr=data.get("hourly_rate")
        ort=data.get("overtime_rate")
        r_pay=rh*hlr
        orh=hw-rh
        ovp=orh*ort
        t_salary=r_pay+ovp
        result={
            "hours_worked" : hw,
            "regular_hours" : rh,
            "hourly_rate" : hlr,
            "overtime_rate" : ort,
            "regular_pay" : r_pay,
            "overtime_hours" : orh,
            "overtime_pay" : ovp,
            "total_salary" : t_salary
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt,name='dispatch')
class AgeDays(View):
    def post(self,request):
        data=json.loads(request.body)
        a=data.get("age")
        m=a*12
        w=a*52
        d=a*365
        result={
            "age" : a,
            "months" : m,
            "weeks" : w,
            "days" : d
        }
        return JsonResponse(result)    
        

# Create your views here.
