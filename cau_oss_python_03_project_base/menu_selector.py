import file_manager
import parking_spot_manager


def start_process(path):
    strs = file_manager.read_file(path)
    class_list = parking_spot_manager.str_list_to_class_list(strs)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(class_list)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                class_list = parking_spot_manager.filter_by_name(class_list,keyword)
                parking_spot_manager.print_spots(class_list)
                
            elif select == 2:
                keyword = input('type city:')
                class_list = parking_spot_manager.filter_by_city(class_list,keyword)
                parking_spot_manager.print_spots(class_list)
            elif select == 3:
                keyword = input('type district:')
                class_list = parking_spot_manager.filter_by_district(class_list,keyword)
                parking_spot_manager.print_spots(class_list)
            elif select == 4:
                keyword = input('type ptype:')
                class_list = parking_spot_manager.filter_by_ptype(class_list,keyword)
                parking_spot_manager.print_spots(class_list)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                class_list = parking_spot_manager.filter_by_location(class_list,min_lat,max_lat,min_lon,max_lon)
                parking_spot_manager.print_spots(class_list)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                class_list = parking_spot_manager.sort_by_keyword(class_list,keyword)
                parking_spot_manager.print_spots(class_list)
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")