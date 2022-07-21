#สินค้าโครงยิงเบอร์
import os
import time
import threading
from request import get
from re import search
from request import Session
from threading import Thread
import colorama
os.system("clear") #ในวงเล็ปคือคําสั่งในแอพเทอมัก
print("เครดิต : ของคุณ") #printคือการแสดงอ่ะไรก็ได้
print (" ฉายยาของคุณ ")
phone = input("เบอร์ : ") #inputการรับข้อมูลเข้ามา แต่ข้อมูลที่รับเข้ามาจะเป็นเบอร์ก็คือphone
print("")
NUM = int(input ("จํานวน : ")) #input NUMเข้ามา NUMในที่นี้คือจํานวนหรือนัมเบอร์(number)
time.sleep(1) #ก็คือดีเลย์ยิ่งรัว

def api (): #apiที่1
    requests.post("https://api.segment.io/v1/m") #ในวงเล็ปคําว่า api ให้ใส่ api ที่มี
print ("ยิงแล้ว ") #ใช้คําสั่งprintให้มันแสดงผลว่ายิงแล้ว

for i in range(NUM): #ให้มันรันตามจํานวนที่เรากําหนด
    threading.Thread(target=api1).start()
    
#จบถ้าจะทํายิงเบอร์แจกแนะนําให้ใส่เครดิตของคุณ