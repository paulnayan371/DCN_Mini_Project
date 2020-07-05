#HEAD Method to implement client side HTTP Protocol.
      
import http.client

#Example of a valid request
conn = http.client.HTTPConnection("www.nits.ac.in")
conn.request("HEAD", "/aboutus/visionandmission.php")
r1 = conn.getresponse()
print("Request Status is ",r1.status,
      " which means the request is ", r1.reason)
print("Thus the connection request is successful")

print("\n")

# Example of an invalid request
conn = http.client.HTTPConnection("www.nits.ac.in")
conn.request("HEAD", "/nothing.spam")
r2 = conn.getresponse()
print("Request Status is ",r2.status,
      " which means the request is ", r2.reason)
print("The server can not find the requested page.")
conn.close()


