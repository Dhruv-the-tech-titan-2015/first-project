import array
import binascii
a = array.array('i', [1,2,3,4,5,6])
print("Original array:")
print('A1:', a)
bytes_array = a.tobytes()#byte representation
print(bytes_array)
print('Array of bytes:', binascii.hexlify(bytes_array))#conversion in machine values