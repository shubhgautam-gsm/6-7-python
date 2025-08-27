data = ["Rajkot", "Surat", "Baroda", "Bhuj", "Jamnagar", "Ahamdabad", "Morbi"]

print(data + ["Rajkot"]) #add original data not change =data[7]  
print(data)


data =data + ["Mumbai"]
print(data) #add new data to the list

# second method
 
data = ["Rajkot", "Surat", "Baroda", "Bhuj", "Jamnagar", "Ahamdabad", "Morbi"]


data.append("Rajkot")
print(data) #add original data not change =data[7]  
