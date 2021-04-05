import natrix
import os
import csv

natrix.create_threads()
natrix.filter_output()

new_rows = []
with open("loops.txt", "r") as loops:
    for loop in loops:
        loop = loop.strip()
        with open(f"TEMPFILES/clean_file_{loop}", "r") as f:
            fstring=f.read()
            fstring=str(fstring)
            swips = (natrix.output_formater_arp(fstring))
# Debugging
           # print ("-"*50)
           # print("Displaying results for host: ", loop)
           # print(swips)

            try:
                for swip in swips:
                    new_swip = [loop, swip]
                    new_rows.append(new_swip)
            except:
                pass


with open("DBFILE/mng_ip_db.csv", "a", newline="") as ipdb:
    dbwriter = csv.writer(ipdb, quoting=csv.QUOTE_ALL, delimiter=";")
    dbwriter.writerows(new_rows)

os.system("rm TEMPFILES/output_file_*")
os.system("rm TEMPFILES/clean_file_*")

print("-"*50)
print("Ending the program.")
