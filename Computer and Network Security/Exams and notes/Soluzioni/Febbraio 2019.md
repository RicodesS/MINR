1.1 The shown protocol has a big flaw: Bob can be used as an oracle which solves challenges by Alice without somehow binding the solved challenge with concepts of initiator and respondent entities of the protocol. Let's suppose Trudy is able to start two different sessions with Bob:

First Session:

- T(A)->B (A, a)

- B->T(A) (B, b, HMAC(X, a))

Now Bob is waiting for the response of its own random challenge b.

Second Session:

- T(A)->B (A, b)
- B->T(A) (B, c, HMAC(X, b))

Now Trudy obtains the HMAC of the nonce b which is required by Bob in the first session. So Trudy can complete mutual authentication with Bob in the first session and discard the second one.
This problem is because of the first message by Alice which immediately ask for an answer and Bob doesn't customize somehow the response such that it cannot be reused in another session.

1.2  To fix the protocol Bob can customize the HMAC, adding also the notion of its own nonce each time. In this time the attack will be prevented due to the fact that we can assume that, since Bob is not compromised, it will choose two different nonces each time:

First Session:

- T(A)->B (A, a)

- B->T(A) (B, b, HMAC(X, a, b))

Second Session:

- T(A)->B (A, b)
- B->T(A) (B, c, HMAC(X, b, c))

To succeed, Trudy would receive HMAC(X, b, a), but Bob sends back HMAC(X, b, c) and it is likely to happen that c will be different to a. Notice that the last two input of HMAC have to be concatenated.



2.1 A stream cipher is based on the notion of keystream. It exploits the bitwise XOR operation between message x and keystream s for encrypting and decrypting operations. Since messages could be vary large, it is infeasible to generate for each message a key which has the same length to perform a bitwise XOR operation. So, a stream cipher must provide a Key Schedule Algorithm (KSA) which generates from a secret key of fixed-length (much less than a common message x), a key stream s. For example the Rivest Cipher 4 (RC4), provides the KSA which, from an array of 256 bytes and a K of predefined length, computes the starting bytes array from which the cipher will take the keystream's bytes. The bytes array is computed swapping 2 bytes at each iteration (initially KSA makes 256 iterations), whose indexes are chosen based on the iteration itself (i-th index) and on the retrieved byte plus a specific key's byte. Then, the cipher algorithm will choose again two pseudo-random bytes, will swap them, and from them it will retrieve a third byte in the bytes array which will be the one xored with the n-th byte of the message. 

A block cipher, instead, doesn't compute any keystream. It is based on a fixed length secret key K and splits the message into fixed length blocks (no need to have the same length). Then, taking in input a block of the message x and the key k it produces an output block, computed by a secure encryption algorithm (like AES). For a block cipher it is fundamental to choose also an operation mode and a padding scheme. The first one is needed due to the block nature of the cipher itself: the naive approach is to encrypt each block separately (ECB mode), but it is well known to be a bad practice due to some possible attacks. So an operation mode is the way in which cipher's outputs are combined together in order to reach some really good property like the hiding plaintext patterns which could be really problematic. The padding scheme is another concern of a block cipher due to the fact that a message x could have a length which is not a multiple of the cipher block and a scheme which is not secure could reveal some information about plaintext.    

2.2 A perfect cipher is based on the bitwise XOR operation between the message x and the key k which must have the same length of a message. In this case the encryption and the decryption operations are really simple to perform, but the real problem is that messages could be very large and finding a random key K with that length is sometime infeasible. Moreover, since messages' length can vary a lot, we cannot store a key for each possible length. So the condition is that the key space must be equal to the message space, otherwise if the key space is less than it, the complexity of a brute force attack is reduced to the key space itself. A stream cipher tries to exploits this idea as I explained before, starting from a fixed length key K. Through a Key Schedule Algorithm, it produces a key stream s with the same length of the message which is being encrypted such that bitwise XOR is performed. 

2.3 Let's try to analyze a stream cipher dividing message and keystream in fixed length blocks: each time it performs a XOR operation between a block of the message and a DIFFERENT block of the keystream, which is unlikely to be the same, assuming the keystream being produced by a secret random key K. Let's now analyze a block cipher using a CFB operation mode in which the encryption algorithm takes as input a key K and a random initial vector IV, then it xores its output with the plaintext block, producing so a cipher text block. After that the cipher text block is used like a randomizer in input to the next encryption block. As it can be noticed, the output is plaintext block xor something, which can be assumed random, as a block of the key used in the stream cipher. So a block cipher, used for example in the CFB mode can be seen as a stream cipher, specifically a asynchronous stream cipher, since the keystream depends also on the previous ciphertext block.    



4.1

- iptables -A FORWARD -i eth2 -j DROP
- iptables -A FORWARD -i eth1 !-d 192.168.0.0/25 -j DROP
- iptables -A INPUT -i eth2 -j DROP
- iptables -A OUTPUT !-d 192.168.0.0/25 -j DROP

4.2 

- iptables -A FORWARD -s 151.100.0.0/16 -d 192.168.0.16/28 -j DROP
- iptables -A FORWARD -d 151.100.0.0/16 -s 192.168.0.16/28 -j DROP

4.3

- The iptables command regards the outgoing packet from the machine where the firewall is installed (OUTPUT chain). The table is the default one, i.e. FILTER. So the firewall is preventing the machine to let go out some packets, dropping them (DROP target at the end of the command). No interfaces, no IPs specified, which means that this rules concern all the network adapters and all the reachable hosts/subnets. It is related to a specific protocol specified by the -p parameter which is tcp. Moreover, for the protocol module, the source ports are specified in the range format which are from 0 to 1023, the ones related to kernel/administrator. So lowest ports are blocked by the kernel and for example no www service can be hosted on that machine, since www uses port 80 as source.
- The second command is pretty similar to the first one. The only change concerns the specified protocol which now is udp. So also administrator ports as sources ([0:1023]) are blocked by the firewall.



5 

- TLS provides only an end-to-end encryption, which is really needed in a client/server secure communication. IPsec can be used in two different modes: Transport (end-to-end encryption) and in Tunnel mode (network-to-network encryption, VPN implementation). 
- Moreover, TLS requires to adapt application protocol to be configured to use TLS protocol, instead IPSec is totally hidden by the applications but requires network adapters to be configured. 
- TLS is well known documented and supported during its lifetime, IPSec is quite complicated since it relies on a lot of standards and also documentation is quite confused and not so clear.
- TLS is already supported by the current browsers, IPSec requires a third party application/software which implements it. 

