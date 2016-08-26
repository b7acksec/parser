from django.shortcuts import render, redirect
from parsxlx.models import Workbook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#Create your views here.
import xlrd

def index(request):
    return render(request, 'main/home.html')

def parsxlx(request):
    rb = xlrd.open_workbook('/Users/timonefm/Downloads/link_price.xls', encoding_override="cp1252")
    sheet = rb.sheet_by_index(0)
    for rownum in range(400, sheet.nrows, 499):
        row = sheet.row_values(rownum)[0]
        row1 = sheet.row_values(rownum)[1]
        row3 = row1 * 68
        #print row3
    #for c_el in row:
        #print row
        create = Workbook.objects.get_or_create(title=row, price=row1, som=row3)
    #return render(request, 'main/home.html', {})
    dannie = Workbook.objects.all()
    paginator = Paginator(dannie, 50) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'main/parsdata.html', {'contacts': contacts, 'dannie': dannie})
