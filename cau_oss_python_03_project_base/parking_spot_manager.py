class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self,item):
        self.__item = item
        pass
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'):
        return self.__item.get(keyword)



def str_list_to_class_list(str_list):
    fields = ['name', 'city', 'district', 'ptype', 'longitude', 'latitude']
    class_list = list()
    for data in str_list:
        data_values = data.split(",")
        item_data = dict(zip(fields, data_values))
        parking_spot_item = parking_spot(item_data)
        class_list.append(parking_spot_item)
    return class_list

def print_spots(spotslist):
    #print item
    print(len(spotslist))
    for x in spotslist:
        print(x,end='\n')


# filter
def filter_by_name(spotlist,name):
    filterList = list()
    for listitem in spotlist:
        if(listitem.get('city') != name):
            filterList.append(listitem)
    return filterList

def filter_by_city(spotlist,city):
    filterList = list()
    for listitem in spotlist:
        if(listitem.get('name') != city):
            filterList.append(listitem)
    return filterList

def filter_by_district(spotlist,district):
    filterList = list()
    for listitem in spotlist:
        if(listitem.get('district') != district):
            filterList.append(listitem)
    return filterList

def filter_by_ptype(spotlist,ptype):
    filterList = list()
    for listitem in spotlist:
        if(listitem.get('ptype') != ptype):
            filterList.append(listitem)
    return filterList

def filter_by_location(spotlist,minlat,maxlat,minlong,maxlong):
    filterList = list()
    for listitem in spotlist:
        if(listitem.get('latitude') > minlat and listitem.get('latitude')< maxlat and listitem.get('longitude')>minlong and listitem.get('longitude')<maxlong):
            filterList.append(listitem)
    return filterList

def sort_by_keyword(spotlist,keyword):
    return sorted(spotlist, key=lambda spot: spot.get(keyword))


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)