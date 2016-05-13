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


* Get all messages
    http://localhost:8000/messages/

    JSON Response format:
    [{"id":1,"content":"Hello there","sender":2,"receiver":3,"room":1,"created_at":"2016-05-12T13:42:26.195015Z"}]

   
