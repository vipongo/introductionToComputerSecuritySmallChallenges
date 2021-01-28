Write a function that implements the following text ecryption scheme (normal text input and output). Remark that these aren't safe encryption schemes.:) 

We have a one-byte key and we encrypt all of the bytes of the plain text by adding the key for every byte and modulo by 256.

If you encrypt a text with a key then the decryption key will be 256-key (e.g. Encryption key 123, Decryption key: 133)

>>> encrypt_by_add_mod('Hello',123)
'Ãàççê'
>>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
'Hello'
>>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
'Cryptography'

https://docs.google.com/drawings/d/1NACFs5A4CspwySfa7Ye0NItR_GDPnpxwAYrORs4vI68/edit?usp=sharing (Links to an external site.)

We have a one byte sized key, xor the first byte of the plaintext and that will be the cipher for the first byte. To encrypt the second byte use the cipher of the message first byte as key and so on. Implement the function that can do encryption and decryption as well based on the third argument (as you can see in the doctest).


>>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
'3V:V9'
>>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
'Hello'
>>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
'Cryptography'

Remark that the encryption of this scheme will not be symmetric.

https://docs.google.com/drawings/d/1LXw_tkZgGJei1aWN8zRdouW6rBs2-xylvfEyZ7uAsFU/edit?usp=sharing