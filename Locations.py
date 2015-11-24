class Location:
    locations = []
    current_id = 0
    def __init__(self, building, room_number):
        Location.current_id += 1
        self.LocationInfo = {}
        self.LocationInfo['location_id'] = Location.current_id
        self.LocationInfo['building'] = building
        self.LocationInfo['room_number'] = room_number

'''def StoreAll(cursor):
       for location in locations:
          placeholders = ', '.join(['%s'] * len(location.LocationInfo))
          columns = ', '.join(location.LocationInfo.keys())
          qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('Instructors', columns, placeholders)
          cursor.execute(qry, instructor.LocationInfo.values())

    def AddLocation(building_and_number):
       location_array = building_and_number.split()
       room_number = location_array[len(location_array) - 1]
       del location_array[len(location) - 1]
       building = ' '.join(location_array)
       for location in locations:
           if location.locationInfo['building'] == building and location.locationInfo['room_number'] == room_number:
             return  location.locationInfo['location_id']
       newlocation = Location(building, room_number)
       locations.append(newlocation)
       return newlocation.LocationInfo['instructor_id']'''

def StoreAllLocations(cursor):
    for location in Location.locations:
        placeholders = ', '.join(['%s'] * len(location.LocationInfo))
        columns = ', '.join(location.LocationInfo.keys())
        qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('Locations', columns, placeholders)
        cursor.execute(qry, location.LocationInfo.values())

def AddLocation(building_and_number):
    location_array = building_and_number.split()
    room_number = location_array[len(location_array) - 1]
    del location_array[len(location_array) - 1]
    building = ' '.join(location_array)
    for location in Location.locations:
        if location.LocationInfo['building'] == building and location.LocationInfo['room_number'] == room_number:
            return  location.LocationInfo['location_id']
    newlocation = Location(building, room_number)
    Location.locations.append(newlocation)
    return newlocation.LocationInfo['location_id']
