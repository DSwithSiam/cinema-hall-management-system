class Star_Cinema:
    __hall_list  = []
    
    def entry_hall(self, hall):
        self.__hall_list.append(hall)



class Hall(Star_Cinema):
    def __init__(self, seats, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_lists = {}
        self.__idList = []

        def __init__(self):
            super(Star_Cinema, self).__init__({ hall_no : {"seats" : self.__seats, "rows": self.__rows, "cols": self.__cols, "Show":self.__show_lists, "idList": self.__idList }})
        
        
    def entry_show(self, id, movieName, time):
        self.__id = id
        self.__movieName = movieName
        self.__time = time
        
        self.__idList.append(id)
        a = f"MOVIE NAME: {self.__movieName} ({self.__id}) SHOW ID: {self.__id} TIME:{self.__time}"
        self.__show_lists[self.__id] = a
        
        __list_seats = []
        for i in range (self.__rows ):
            list_n = []
            for j in range (self.__cols):
                list_n.append(0)
            __list_seats.append(list_n)
        self.__seats[self.__id] = __list_seats
    
    
    def book_seats(self, id, row, col):
        
        if id not in self.__idList:
            print("**** Invalid ID ****")
            return 0
        
        if 0 > row > self.__rows and 0 > col > self.__cols:
            print("**** Invalid Row, Column ****")
            return 0
        if self.__seats[id][row-1][col-1] == 1:
            print(f"**** Already ({row}, {col}) Seat Booked ****")
            
        else:
            self.__seats[id][row-1][col-1]= 1
            print(f"**** Seat ({row}, {col}) booked for show {id} ****")
    
    def view_show_list(self):
        print("-------------------")
        for val in self.__show_lists.values():
            print(val)
        print("-------------------\n")
    
    def view_available_seats(self, ID):
        if ID not in self.__idList:
            print("**** Invalid ID ****")
            return
            
        print("**** All Seats: ****")
        for i in range(self.__rows+1):
            for j in range(self.__cols+1):
                print(f"Seat: ({i}, {j}) ")
        
        print("\n**** Updated Seats: ****")
        for i in self.__seats[ID]:
            print(i)
        print('\n')  

            
ab = Hall(200, 5, 5, 1)


ab.entry_show(111, "Pagla Haoya", "08/10/2023 11:00 AM")
ab.entry_show(222, "Poran Pakhe", "08/10/2023 2:00 PM")



while True:
    
    print("""
            1. VIEW ALL SHOW TODAY
            2. VIEW AVAILABLE SEATS
            3. BOOK TICKET
            4. Exit
            
            """)
    n = int(input("INTER OPTION: "))
    
    if 4 < n or n < 1:
        print("****Invalid Number****")
        
    elif n == 1:
        ab.view_show_list()
        
    elif n == 2:
        id_number = int(input("ENTER SHOW ID: "))
        ab.view_available_seats(id_number)
        
    elif n == 3:
        id_number = int(input("Show ID: "))
        Ticket = int(input("Number of Ticket: "))
        
        if Ticket <= 0:
            print("****At least 1 ticket must be purchased****")
            continue
        
        if Ticket > 1:
            for i in range(1, Ticket+1):
                print(f"TICKET {i} ")
                Row = int(input("Enter Seat Row: "))
                Col = int(input("Enter Seat Column: "))
                ans =  ab.book_seats(id_number, Row, Col)
                if ans == 0:
                    break
        else:
            Row = int(input("Enter Seat Row: "))
            Col = int(input("Enter Seat Column: "))
            ab.book_seats(111, Row, Col)
        
    elif n == 4:
        break
        