import rsa
 
publicKey, privateKey = rsa.newkeys(512)
 
message = input( "Enter Message to be encrypted : ")
encMessage = rsa.encrypt(message.encode(),publicKey)
 
print("Original string: ", message)
print("Encrypted string: ", encMessage)
 
decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("Decrypted string: ", decMessage)