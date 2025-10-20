import sqlite3 as sql



location= r"C:\Users\Owner\Documents\coding\hotel_management_system\Database\HotelManagement.db"

def Create_tables():
    connector = sql.Connection(location)
    cursor = connector.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Client(
                        id INT AUTO INCREMENT,
                        client_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        first_name VARCHAR(30),
                        last_name VARCHAR(30),
                        contact INTEGER NOT NULL,
                        id_no INTEGER NOT NULL UNIQUE,
                        email VARCHAR(100),
                        gender NOT NULL CHECK(gender IN ('Male', 'Female', 'Other')),
                        password VARCHAR(20),
                        code INTEGER UNIQUE NOT NULL 
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Staff(
                        id INT AUTO INCREMENT,
                        staff_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        first_name VARCHAR(30),
                        last_name VARCHAR(30),
                        contact INTEGER NOT NULL,
                        id_no INTEGER NOT NULL UNIQUE,
                        email VARCHAR(100),
                        role VARCHAR(30),
                        salary INTEGER NOT NULL,
                        date_of_joining TEXT NOT NULL,
                        shift_start TEXT NOT NULL,
                        shift_end TEXT NOT NULL,
                        gender TEXT NOT NULL CHECK(gender IN ('Male', 'Female', 'Other')),
                        password VARCHAR(20),
                        code INTEGER UNIQUE NOT NULL, 
                        service_id INTEGER NOT NULL
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Inventory(
                        id INT AUTO INCREMENT,
                        inventory_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        item_name VARCHAR(60),
                        category VARCHAR(20),
                        service_time TEXT,
                        item_description TEXT,
                        quantity INTEGER DEFAULT 0,
                        price_per_unit REAL DEFAULT 0.00
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Room(
                        id INT AUTO INCREMENT,
                        room_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        room_type VARCHAR(50) NOT NULL,
                        bed_type VARCHAR(50) NOT NULL,
                        price_per_night REAL NOT NULL,
                        availabilty_status  INTEGER NOT NULL DEFAULT 1 CHECK(availabilty_status IN (0, 1)),
                        max_occupation INTEGER NOT NULL
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Booking(
                        id INT AUTO INCREMENT,
                        booking_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        client_id INTEGER,
                        room_id INTEGER,
                        check_in_date TEXT DEFAULT (date('now')),
                        check_out_date TEXT,
                        number_of_guests INTEGER DEFAULT 1,
                        total_price REAL,
                        booking_status TEXT NOT NULL DEFAULT 'pending' CHECK(booking_status IN ('pending', 'active', 'complete'))     
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Service(
                        id INT AUTO INCREMENT,
                        service_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        service_name VARCHAR(100) NOT NULL,
                        service_description TEXT,
                        service_price REAL   
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Service_request(
                        id INT AUTO INCREMENT,
                        request_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        booking_id INTEGER,
                        service_id INTEGER,
                        request_time TEXT DEFAULT (time('now')),
                        request_date TEXT DEFAULT (date('now')),
                        request_status TEXT NOT NULL DEFAULT 'pending' CHECK(request_status IN ('pending', 'active'))
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS payment(
                        id INT AUTO INCREMENT,
                        payment_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        booking_id INTEGER,
                        service_id INTEGER,
                        amount REAL,
                        payment_time TEXT DEFAULT (time('now')),
                        payment_date TEXT DEFAULT (date('now')),
                        payment_mode TEXT NOT NULL DEFAULT 'M-pesa' CHECK(payment_mode IN ('M-pesa', 'Bank')),
                        account INTEGER NOT NULL,
                        payment_status TEXT NOT NULL DEFAULT 'not paid' CHECK(payment_status IN ('not paid', 'pending', 'paid'))
                )""")
    
    connector.commit()
    connector.close()


def insert_invent(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO inventory(inventory_id, item_name, category,service_time, item_description, quantity, price_per_unit) VALUES(?,?, ?, ?,?,?,?)", x)
     connector.commit()
     connector.close()

def insert_service(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO Service(service_id, service_name, service_description, service_price) VALUES(?, ?, ?,?)", x)
     connector.commit()
     connector.close()

def insert_Room(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO Room(room_id, room_type, bed_type, price_per_night, availabilty_status, max_occupation) VALUES(?, ?, ?,?,?,?)", x)
     connector.commit()
     connector.close()

data =[
     [1241,'Blake',	'Kimani',	786235516, 628336, 'blakek123@havenhub.com',	'General Manager',100000,'2018-03-07','08:00:00','17:00:00','Male','G%6IRt',1234,4001],
     [1242,'Esther','Mosyoka',722660576	,126350,'esthermosyoka123@havenhub.com','Assistant Manager',90000,'2018-03-07','08:00:00','17:00:00','Female',',68nd',1975,4002],
     [1243,'Taylor','Nyambura',710664144,80184,'taylorn345@havenhub.com','Financial Manager',80000,'2018-03-08','08:00:00','17:00:00','Female','X8u%m$G',1545,4003],
     [1244,'Jordan','Kipchoge',728061354,51848,'jkipchoge@havenhub.com','Sales & Marketing Manager',40000,'2018-03-09','07:00:00','18:00:00','Male','0b9x.',1865,4004],
     [1245,'Mike','Onyango',777620548,756518,'mikeonyango@havenhub.com','IT Manager',40000,'2020-01-11','08:00:00','17:00:00','Male','xp5e9nRM',1743,4005],
     [1246,'Tiffany','Bradly',771174272,835452,'tiffanyb@havenhub.com','Receptionist',20000,'2024-07-12','06:00:00','18:00:00','Female','zOzkhG',1364,4006],
     [1247,'Jamie','Otieno',734061660,418176,'jamieotieno1@havenhub.com','Night Auditor',20000,'2024-02-14','18:00:00','06:00:00','Male','p2vRdllZP',1732,4008],
     [1248,'Casey','Wangari',762071311,446656,'caseyw453@havenhub.com','Front Desk Manager',20000,'2024-01-13','06:00:00','18:00:00','Female','ZM.kns^q',1084,4007],
     [1249,'Riley','Musili',771207876,360754,'rileym@havenhub.com','Housekeeper',12000,'2023-07-15','06:00:00','05:00:00','Female','x1x8$',1542,4009],
     [1250,'Dakota','Donz',716845713,58114,'dakota123@havenhub.com','Electrician & Plumber',20000,'2022-04-16','08:00:00','17:00:00','Male','siDOK8T',1011,4011],
     [1251,'Quinn','Obuor',782628360,36420,'qobuor2@havenhub.com','Laundry Attendant',12000,'2024-04-29','06:00:00','17:00:00','Female','Y@7db&*u',1208,4017],
     [1252,'Logan','Hanz',743150318,177170,'loganhanz@havenhub.com','Maintenance Technician',20000,'2020-07-12','07:00:00','17:00:00','Male','2cYWJ',1376,4011],
     [1253,'Morgan','Wainana',722301847,601887,'wainanam@havenhub.com','Chef',15000,'2019-07-19','07:00:00','17:00:00','Male','eWDmpze',1832,4010],
     [1254,'Charlie','Banet',701252664,503306,'charlieb345@havenhub.com','Waiter',10000,'2024-04-20','07:00:00','17:00:00','Male','!bpz$wN',1811,4010],
     [1255,'Hailey','Anyango',726680276,527501,'haileyan123@havenhub.com','Waitress',10000,'2024-05-21','07:00:00','17:00:00','Female','8hMb^',1200,4010],
     [1256,'Rose','Wanjiru',752172803,765128,'rose253@havenhub.com','waitress',10000,'2024-03-01','07:00:00','17:00:00','Female','c0Uhisj',1111,4010],
     [1257,'Michael','Harris',765417400,28232,'michaelh5@havenhub.com','Bartender',12000,'2019-07-23','07:00:00','17:00:00','Male','fW,PbE7',1762,4010],
     [1258,'Martin','Obonye',723780861,741402,'martin2453@havenhub.com','Restaurant Manager',33000,'2019-07-24','06:00:00','17:00:00','Male','RVpJI',1611,4012],
     [1259,'Janet','Ciku',707518036,437278,'janetk32@havenhub.com','Room Service Attendant',12000,'2024-01-25','07:00:00','17:00:00','Female','wR^o6w',1621,4017],
     [1260,'Bob','Koinange',768682520,148633,'bobK123@havenhub.com','Security Guard',10000,'2023-05-16','06:00:00','18:00:00','Male','qFS5CDw#f',1099,4013],
     [1261,'Jimmy','Kipchebet',712258370,776023,'JimmyK@havenhub.com','Security Guard',10000,'2023-07-16','18:00:00','06:00:00','Male','tSJeq',1777,4013],
     [1262,'Morris','Nganga',747145265,586263,'morisn3433@havenhub.com','Parking Attendant',10000,'2024-07-27','06:00:00','17:00:00','Male','$L.&2D',1321,4014],
     [1263,'Alex','Otieno',755708724,721576,'otienoalex@havenhub.com','Event Coordinator',33000,'2022-07-08','07:00:00','17:00:00','Male','T0M$!az8',1098,4018],
     [1264,'Janet','Atieno',764341422,248600,'janeta322@havenhub.com','Spa & Wellness Staff',20000,'2023-03-29','08:00:00','17:00:00','Female','Fj4%l8',1671,4015],
     [1265,'Teddy','Morris',780603163,25010,'teddym@havenhub.com','Facilities Manager',40000,'2020-07-30','08:00:00','17:00:00','Male','.NsTgs*01',1921,4016]
       ]

services = [
     [4001,'General Management','Oversees all hotel operations, budgeting and staff management',0],
     [4002,'Management Assistance','Supports the general manager, handles daily operations',0],
     [4003,'Finance Management','Manages, hotel accounts, budgeting, financial reporting',0],
     [4004,'Sales & Marketing Management','Promotes the hotel, manages bookings, creates advertisements',0],
     [4005,'IT Management','Maintains hotel management software, WIFI, security system',0],
     [4006,'Guest reception','Handle reservation for',50],
     [4007,'Desk Operations','Handle reservation for',100],
     [4008,'Night Shift Desk Operations','Handle reservation for',100],
     [4009,'House service','perform house service for room',50],
     [4010,'food, & beverage service',  'perform food, & beverage service to',60],
     [4011,'Maintenance Service','Perform Maintainance service to hotel',50],
     [4012,'Restaurant Management','Manage restaurant activities',0],
     [4013,'Security','Protect people and hotel utilites',50	],
     [4014,'Car Parking service','Direct cars to available parking space',40],
     [4015,'Spa & Wellness service','Perform massage to clients',100],
     [4016,'Hotel Facility management','Ensure all hotel facilites are in place',0],
     [4017,'Room service','Perform room service for room',100],
     [4018,'Event Coordinator','Coordinate events in the hotel',400]
     
]

rooms = [
     [101,	'Single',	'Normal',	16.5, 1,   2],
     [102	,    'Single',	'Normal',	16.5, 1,	2],
     [103,	'Single',	'Normal',	16.5, 1,	2],
     [104,     'Single',	'Normal',	16.5, 1,	2],
     [105,	'Single',	'Normal',	16.5, 1,	2],
     [106,	'Single',	'Normal',	16.5, 1,	2],
     [107,	'Single',	'Double Decker', 17, 1,	4],
     [108,	'Single',	'Double Decker', 17, 1,	4],
     [109,	'Single',	'Double Decker', 17, 1,	4],
     [110,	'Single',	'Double Decker', 17, 1,	4],
     [111,	'Single',	'Double Decker', 17, 1,	4],
     [112,	'Single',	'Double Decker', 17, 1,	4],
     [113,	'Bed Sitter',	'Normal',	 21.5, 1,	2],
     [114,	'Bed Sitter',	'Normal',		21.5, 1,	2],
     [115,	'Bed Sitter',	'Normal',		21.5, 1,	2],
     [116,	'Bed Sitter',	'Normal',		21.5, 1,	2],
     [117,	'Bed Sitter',	'Double Decker',		22, 1,	4],
     [118,	'Bed Sitter',	'Double Decker',		22, 1,	4],
     [119,	'Bed Sitter',	'Double Decker',		22, 1,	4],
     [120,	'Bed Sitter',	'Double Decker',		22, 1,	4],
     [121,	'Bed Sitter',	'Kingsize',		22.5, 1,	5],
     [122,	'Bed Sitter',	'Kingsize',		22.5, 1,	5],
     [123,	'Bed Sitter',	'Kingsize',		22.5, 1,	5],
     [124,	'Bed Sitter',	'Kingsize',		22.5, 1,	5],
     [125,	'One bedroom',	'Normal',		24.5, 1,	4],
     [126,	'One bedroom',	'Normal',		24.5, 1,	4],
     [127,	'One bedroom',	'Normal',		24.5, 1,	4],
     [128,	'One bedroom',	'Normal',		24.5, 1,	4],
     [129,	'One bedroom',	'Double Decker',		25, 1,	8],
     [130,	'One bedroom',	'Double Decker',		25, 1,	8],
     [131,	'One bedroom',	'Double Decker',		25, 1,	8],
     [132,     'One bedroom',	'Double Decker',		25, 1,	8],
     [133,	'One bedroom',	'Kingsize',		25.99, 1,	6],
     [134,	'One bedroom',	'Kingsize',		25.99, 1,	6],
     [135,	'One bedroom',	'Kingsize',		25.99, 1,	6],
     [136,	'One bedroom',	'Kingsize',		25.99, 1,	6],
     [137,	'Two Bedroom',	'Normal',		26, 1,	8],
     [138,	'Two Bedroom',	'Normal',		26, 1,	8],
     [139,	'Two Bedroom',	'Normal',		26, 1,	8],
     [140,	'Two Bedroom',	'Normal',		26, 1,	8],
     [141,	'Two Bedroom',	'Double Decker',		26.99, 1,	16],
     [142,	'Two Bedroom',	'Double Decker',		26.99, 1,	16],
     [143,	'Two Bedroom',	'Double Decker',		26.99, 1,	16],
     [144,	'Two Bedroom',	'Double Decker',		26.99, 1,	16],
     [145,	'Two Bedroom',	'Kingsize',		27.5, 1,	9],
     [146,	'Two Bedroom',	'Kingsize',		27.5, 1,	9],
     [147,	'Two Bedroom',	'Kingsize',		27.5, 1,	9],
     [148,	'Two Bedroom',	'Kingsize',		27.5, 1,	9]
     
]

food = [
     [209,	'toast'	,  'food',	 'Breakfast','food offererd in restaurant',					50,	2.99],
     [210,'pancake'	,  'food',	 'Breakfast',	'food offererd in restaurant',				40,	2.33],
     [205,	'Coffee'	,  'food',	 'Breakfast','food offererd in restaurant',					100,	1.99],
     [211,	'Tea'	,  'food',	 'Breakfast',	'food offererd in restaurant',				100,	2],
     [207,	'Tea & Mandazi'	,  'food',	 'Breakfast',	'food offererd in restaurant',				30,	2.5],
     [204,	'Toasted bread & Tea'	,  'food',	 'Breakfast','food offererd in restaurant',					25,	2.8],
     [203,	'Tea & Sandwitch'	,  'food',	 'Breakfast','food offererd in restaurant',					50,	4.33],
     [202,	'Porridge'	,  'food',	 'Breakfast',	'food offererd in restaurant',				40,	1.99],
     [208,	'Chapati'	,  'food',	 'Breakfast',		'food offererd in restaurant',			100,	2.99],
     [206,	'Tea & Cookies'	,  'food',	 'Breakfast',	'food offererd in restaurant',				15,	2.99],
     [201,	'Scramble'	,  'food',	 'Breakfast','food offererd in restaurant',					20,	3.6],
     [212,	'Brown cookies & Tea'	,  'food',	 'Breakfast',	'food offererd in restaurant',				50,	2.99	],							
     [213,	'Beef & Rice'	,  'food',	 'Lunch',		'food offererd in restaurant',			20	,4.5],
     [214,	'Rice, Njahi & Avocado'	,  'food',	 'Lunch',	'food offererd in restaurant',				25,	3.5],
     [215,	'Rice & meat'	,  'food',	 'Lunch',		'food offererd in restaurant',			25,	4],
     [216,	'Rice & Curry'	,  'food',	 'Lunch',		'food offererd in restaurant',			20,	4.2],
     [217,	'Rice & Peas'	,  'food',	 'Lunch',		'food offererd in restaurant',			20,	4.5],
     [219,	'Ugali, Greens & Eggs'	,  'food',	 'Lunch',	'food offererd in restaurant',				20,	4.6],
     [220,	'Ugali, meat & Cabbage'	,  'food',	 'Lunch',	'food offererd in restaurant',				20,	4.5],
     [221,	'Githeri & Avocado'	,  'food',	 'Lunch',	'food offererd in restaurant',				80,	3.7],
     [222,	'Beef Pilau'	,  'food',	 'Lunch',		'food offererd in restaurant',			30,	4.2],
     [223,	'Ugali, Greens & Fish'	,  'food',	 'Lunch',	'food offererd in restaurant',				40,	5.09],
     [224,	'Stew'	,  'food',	 'Lunch',		'food offererd in restaurant',			35,	4.3],
     [218,	'Chapati & Beef'	,  'food',	 'Lunch',	'food offererd in restaurant',				70,	4.5],								
     [225,	'Burger'	,  'food',	 'Dinner',		'food offererd in restaurant',			20,	3.44],
     [226,	'Chapati, meat & Greens'	,  'food',	 'Dinner','food offererd in restaurant',					40,	5.3],
     [227,	'Beef & Salad'	,  'food',	 'Dinner',	'food offererd in restaurant',				35,	4.6],
     [228,	'Mokimo & meat'	,  'food',	 'Dinner','food offererd in restaurant',					30,	4],
     [229,	'Githeri & Meat'	,  'food',	 'Dinner',	'food offererd in restaurant',				20,	4],
     [230,	'Chapati & meat'	,  'food',	 'Dinner',	'food offererd in restaurant',				34,	4.2],
     [231,	'Ugali & Meat'	,  'food',	 'Dinner',		'food offererd in restaurant',			32,	4.5],
     [232,	'Rice'	,  'food',	 'Dinner',			'food offererd in restaurant',		32,	3.99],
     [233,	'Ugali, Greens & meat'	,  'food',	 'Dinner','food offererd in restaurant',					20,	4.99],
     [234,	'Meat'	,  'food',	 'Dinner',			'food offererd in restaurant',		21,	4],
     [235,	'Chips & Chicken'	,  'food',	 'Dinner',	'food offererd in restaurant',				12,	5],
     [236,	'Ugali, Meat & Greens'	,  'food',	 'Dinner',	'food offererd in restaurant',				15,	4.99]

]
Create_tables()
insert_service(services)
insert_Room(rooms)
insert_invent(food)


