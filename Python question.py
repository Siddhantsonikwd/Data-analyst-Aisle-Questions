from math import ceil
def salesTax(itemList):
    extempGoods = ['book', 'chocolate', 'pills', 'chocolates']
    
    finalOutList = []
    oldSum = 0
    TotalSalesTax = 0
    rnd = 20
    
    for item in itemList:
        
        SalesTax = 0
        
        tempListItem = item.split()
        
        exemptFlag = True
        importFlag = False
        
        for TempItem in tempListItem:
            if TempItem in extempGoods:
                exemptFlag = False
            if str(TempItem) == "imported":
                importFlag = True
                
        if importFlag:
            SalesTax += ceil(round((float(tempListItem[-1]) * 0.05), 2) * rnd) / rnd
        
        if exemptFlag:
            SalesTax += ceil(round((float(tempListItem[-1]) * 0.10), 2) * rnd) / rnd
        
        oldSum += float(tempListItem[-1])
        TotalSalesTax += float(SalesTax)
        
        tempListItem[-1] = str(round(float(tempListItem[-1]) + float(SalesTax),2))
        
        for i in range(len(tempListItem)):
            if tempListItem[i]=='at':
                tempListItem[i]=':'
        finalOutList.append(tempListItem)
    
    for item in finalOutList:
        print(*item, sep = " ")    
        
    print("Sales Taxes:",ceil(round(TotalSalesTax, 2) * rnd) / rnd)   
    print("Total:",round((ceil(round(TotalSalesTax, 2) * rnd) / rnd)+oldSum,2))
           
            
itemlist = ['1 imported bottle of perfume at 27.99','1 bottle of perfume at 18.99','1 packet of headache pills at 9.75','1 box of imported chocolates at 11.25']        

salesTax(itemlist)