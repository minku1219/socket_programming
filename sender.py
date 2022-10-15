import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

recv_add=("127.0.0.1",9999)

msg=input("Enter Your Message: ")

converted_msg=msg.encode('ascii')

s.sendto(converted_msg,recv_add)

print("Your Message has been sent")
// element.style.display = "none";
