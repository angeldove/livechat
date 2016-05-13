# livechat
Live chat application in django and python

* Get all rooms
    http://localhost:8000/rooms/

    JSON Response format:
    [{"id":1,"name":"General"},{"id":2,"name":"Troubleshooting"}]

* Get a room by id.

  Lets say, room id is 1

  http://localhost:8000/rooms/1

    JSON Response format:
    {"id":1,"name":"General"}

   
