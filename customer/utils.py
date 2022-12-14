def gettingimfo(imformation):
        total_items = 0
        total_products = 0
        net_total = 0
        for x in imformation:
            total_items = total_items + x.no_of_items
            net_total = net_total + x.item_total()
            total_products = total_products+1
        result = {'total_items':total_items, 'total_products':total_products, 'net_total':net_total }
        return result