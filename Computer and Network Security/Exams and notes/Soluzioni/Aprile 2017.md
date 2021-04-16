1.1 Let's suppose an authentication protocol for mutual authentication base on a shared secret K. Alice and Bob will use this protocol:

- A->B: I'm Alice
- B->A: $N_B$
- A->B: $f(K,N_B), N_A$
- B->A: $f(K,N_A)$

As I specified in the protocol, there is only the need of a function based on the secret K and the challenge sent by one party to the other. The verification algorithm, instead of reverse the output of the function, in the case of a one-way function (like HMAC), will compute again the output starting from the known secret K and the clear text nonce previously received. So yes, it is possible. 

1.2 Let's optimize the previous protocol:

- A->B: I'm Alice, $N_A$
- B->A: $f(K,N_A), N_B$
- A->B: $f(K,N_B)$

This protocol is weak with respect to a reflection attack, because Trudy could exploit two different session with Bob. The second one she will use Bob as a challenge solver:

First session:

Second session:

1.3 The concept of the ticket in an authentication protocol based on a third trusted entity is fundamental. In this scheme each user of the network owns a master key, i.e. a symmetric key between theirself and the key distribution center KDC. When Alice contacts the KDC, saying that she wants to interact with Bob, the KDC must invent a session key between Alice and Bob to be used in a single session. The session key is sent to Alice in an encrypted fashion, through her master key (only her can retrieve from that message). KDC does not directly send the same message to Bob encrypted with his own master key. Instead, the KDC sends, encrypted with the master key of Alice as well, a ticket to Alice which is a message encrypted with the master key of Bob (so not changeable by no one except than Bob), which contains the identity of Alice which asked for the communication, some information about the validity of the ticket and the generation timestamp, but most important the session key previously invented. In this case Bob will receive directly by Alice this ticket which allows this latter to talk confidentially with Bob without store a permanent symmetric key with him. The authentication is another master piece of this scheme. Bob must check the identity of the person/machine who is contacting him, because he is not involved in the first part of the protocol. Alice so, after forwarding the ticket, sends an authenticator message which contains her identity A plus some information to ensure freshness, like a timestamp, and this message is encrypted with the session key. In this way Bob can check if the identity of the initiator of the protocol contained in the ticket matches with the one used in the authenticator. 



2.1

- Given the domain parameters $(p,q,\alpha)$, the public key $\beta$ and the private key $d$, for a new message $x$ firstly it must be chosen an integer between $K_e$ such that $0<K_e<q$. Then two values are computed:

  - $r = (\alpha^{K_e}modp)modq$
  - $s = (SHA(x)+rd)K_e^{-1}modq$

  Then the signature is composed by $(r,d)$.

- The verification algorithm check for $v=r$, where $v$ is computed as follows:

  - $w = s^{-1}modq$
  - $u_1=w*SHA(x)modq$
  - $u_2=w*r\space modq$
  - $v=(\alpha^{u_1}*\beta^{u_2}modp)modq$

2.2 Knowing the ephemeral key for a message x means that: $K_e=(SHA(x)+rd)s^{-1}modq$. Now the only unknown parameter is $d$, which is fundamentally to kept secret since it is the private key. We can retrieve it like: $d=\frac{K_e*s - SHA(x)}{r}modq$.

2.3  If Alice needs to timestamp a document, she can add to the hash of the document the timestamp. So SHA(x) will be (SHA(x)||timestamp). Then she can use this message to produce the signature. To perform the validity of the signature, while Bob needs to compute $u_1$, he needs the timestamp in clear text to append it at the end of SHA(x), so Alice must give it to him. If then r and v will match, Bob is sure about also the timestamp claimed by Alice. 



4.1 There are three properties which must be satisfied:

- One-Wayness: it must be a function which must be hard to revert, i.e. given an output h(x), it must be computational infeasible to retrieve x in a reasonable amount of time. This is also called Primary-Image Resistance.
- Weak Collision Resistance: this property concerns the possibility by an attacker that, given a message x and its hash value h(x), it must be computational infeasible to find another x', different from x, whose hash value h(x')= h(x).
- Strong Collision Resistance: this property concerns the possibility of an attacker to generate two messages x and x' such that their hash values h(x)=h(x').  

4.2 The hash function $f$ takes always two inputs: the current block of the message and another bit string. For the first block it is used an Initial Vector IV, but instead of taking it random for each hash function, it is kept constant. This is because of non randomness needed in hash function. For the following block, the output of the previous block is used instead. This is the Merkle-Damgard concatenation scheme in order to produce a single fixed length output block by a variable length message in input. So in this case the function $f$ takes the block and an IV constant, typically 0.

4.3 The keyed hashing is based not only on the message x, but also on a secret key K which can be used in different ways. A simple hash function can be attacked by a birthday attack always, because the all the message space is valid. In the keyed-hashing instead, using a key, means restricting the message space to the messages which contains the key somehow (it depends on how the key is positioned).

- $K|m$ is the prefix way where to put the key. This way prevents birthday attacks since the attacker cannot generate valid message without knowing the key K. Although, due to the Merkle-Damgard scheme, he can produce a valid hash value by appending whatever plaintext block to the message m. This is way the previously described scheme, takes as input each time the previous computed hash and the new plaintext block. So, the key contribution is discarded. 
- $m|K$ This approach avoids appending block attacks, but still suffer for birthday attack since if attacker finds a collision between m, s.t. h(m)=h(m') with m!=m', also h(m||K)=h(m'||K) is true. So in this case the appended key doesn't increase security wrt birthday attack.
- $K|m|K$ This mixed approach is more secure than the previous ones. First of all no appending blocks attacks are possible due to the presence of the K at the end of the string. Also birthday attacks are prevented due to the key at the beginning of the string. This mixed approach is the basis off HMAC.  