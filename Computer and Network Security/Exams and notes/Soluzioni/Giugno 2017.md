1

- False
- False
- False
- False
- True
- True
- True
- False
- True
- True



2.1 Let's prove the inverse: not weakly collision resistant implies not strongly collision resistant: let A be a polynomial algorithm such that given input x is able to find another x' such that h(x)=h(x'), then let B another algorithm that chooses randomly message x and return (x,x') such that h(x)=h(x'), where x' is find using the algorithm A given x, i.e. (A(x))=x'.

2.2 The birthday attack is an attack that exploits the possibility to find a collision between two random inputs x1 and x2 such that h(x1)=h(x2). To reach a probability of at lesat 50% that this happen reqquires a number of tentative up to the square root of the output space of the hash function itself. So if the hash value space is about $2^n$, the expected complexity to find two message that collides with a probability of at least 50% is $2^{n/2}$. So it depends on how many bits are used to represent the domain space. It is called in this way due its nature: let's suppose to invite people to a party, what is the minimum number of people that I have to invite to have that at least two of them are born in the same day of the year ()day plus month)? The prob that 2 person has the same birthday is $1/365$. The complementary probability is $1-1/365$. With 3 people we do not have a collision with probability of $(1-1/365)(1-2/365)$. So let's continue this reasoning and we obtain that with n people the probability that no collisions happen is that $\prod_i^{n-1}(1-i/365)$. So to have this probability of at least 50% we need about 23 people, which is the square root of 365, the output space. This reasoning can be applied on a custom hash function with the same procedure, just replacing 365 with the output space of the hash function.

2.3 The keyed hashing is based on two different inputs: a secret shared K and the message m. The protection against the birthday attack depends on how the key is used. For exampple let's suppose that the key is prepended to the message. In this case the birthday attack cannot be performed because the attacker doesn't know the key and, because of the iterative nature of the hash functions, it cannot generate valid messages where to find a collision. But this approach suffers of forgery attacks, so must be avoided. Instead if the key is appended we can exploit this: if h(x)=h(x'), with x!=x', then also h(x||k)=h(x'||k). So the birthday attack can be performed taking into account only valid message x. So the correct way is to use a combination of the two approaches like HMAC does, using nested hash function like h(k||h(k||x)). In this case it is being used the prepended version of a keyed hashing which protects against birthday attacks and also protects against forgery attacks due to the concatenation of  another hash value. Nesting hash values avoids possibility to forge easily a new message for MAC purpose.

2.4 Well in this case, soen't matter what kind of keyd hashing is used, protection over birthday attack is gone. Prepended keyed hashing can be attacked, since it boils down to find a collision of messages with a prefix known K. Appended the same approach. For the nested, if the key is known, then the collision must be found for the inner hash value, because then the concatenation of the key will produce a deterministic hash value.



3.1 TLS is a set of cryptographic protocols that provides authentication of entities and confidentiality. It works over the TCP Layers, so it encrypt each segment in an end-to-end fashion. It prevents eavesdropping, i.e. third evil party listening to the communication, tampering, i.e. the ability to manipulate and modify messages on the fly withouth be discovered and message forgery, i.e. producing a valid and legal message to be exploited in a communication session between two entities. Typically, TLS is used to provide single authentication of the server, it also support mutual authentication but this will imply that a client shoud has a valid certificate which is unlikely to happen. Certificates respect the X.509 model and their validity is based on the PKI composed by trusted CAs. Generally, TLS can be divided in 3 main steps:

- Negotiation phase: in this phase the two entities negotiate a cipher suite and key exchange algorithm to be used in the communication. This is required to be compliant to all devices, i.e. some devices (like IoT ones) are not able to support computational expensive cryptographic algorithm, so server will choose the most secure from a client list of supported ones.
- Key exchange phase: in this phase, according to the algorithms chosen in the previous phase, the two entities exchange necessary session keys that are going to be used in the communication session.
- Entities authentication and symmetric encryption phase: in this phase the two entities provides the required information to complete the authentication step (commonly the server's authentication). Then, when entities trust each other, they switch to a symmetric encryption exploiting the keys previously exchanged. 

3.2 A very well-spread example of usage of TLS is web browsing. In this case, clients are users' browsers which want to surf web being sure of who they are talking with and that what they are sending is kept confidential. Web browsers support by default TLS and check automatically the validity of a server's certificate. Another example is mail exchanging. Here TLS is used to authenticate the mail servers and to keep confidential the email content.

3.3 A big problem about TLS is represented by the POODLE attack. Before TLS 1.3, an attacker could downgrade the used protocol tu SSL 3.0 so that, after the negotiation phase, it was able to enstablished a vulnerable cipher suite to attack through a padding oracle attack. Nowadays, TLS 1.3 is able to disable this option, avoiding so the possibility to use SSL 3.0. 

   

4.1 The machine, on which the firewall is implemented, is allowed to contact any dns (using udp protocol and destination port 53), from whatever user source port (from 1024 to 65535) if and only if the request is going out from the interface called eth0.

4.2 The machine, ..., is allowed to forward new connections (state == NEW) coming from interface called eth0 towards interface called eth1 of ssh (protocol tcp and destination port 22) which use an user source port (from 1024 to 65535).

4.3 The machine, ..., is allowd to accept ssh new connections (protocol tcp destination port 22 state==new) coming from interface called eth0 using an user source port (from 1024 to 65535).



5.2 127 is a prime number, so we can exploit Fermat Little's theorem. 200 can be written as 126 + 74. So: $2^{126}=1mod127$. From here we can multiply both memebers with the remaining part $2^{74}$ obtaining so: $2^{200}=2^{74}mod127$. 74 can be simplified as $7*10+4=74$ and so: 

- $2^{7}mod127=128mod127=1mod127$.

- $=1^{10}mod127=1mod127$
- $2^{200}=2^4mod127=16mod127$



