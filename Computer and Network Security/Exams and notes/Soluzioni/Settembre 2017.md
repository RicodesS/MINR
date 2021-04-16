1.1 In this case we are interested in verifying the compiled application when it wants to interact with the server S via internet. The difference we can exploit to distinguish between official client application and the third party ones is the application itself. We can see at the application as a binary string which can be signed by the official developers in order to be verified. So S will be the server, C an hypothetical client:

- C locally computes the hash value, using a cryptographic secure hash function, of its executable, called $H(EXE_C)$. 



2.1 Well, since they are using symmetric scheme based on a 256-bits key $K_{AB}$, Bob has two ways to verify the message:

- He decrypts the authentication tag sent by Alice, retrieving so the first 128 bits of the message $M$, and checks if they match with the received plaintext message.
- He can encrypt the first 128-bits of the plaintext message $M$ and check if they match with the authentication tag.

2.2 It can be noticed that the check is performed only on the first 128 bit of the message. If the length of the message is less or equal to 128 bit, then the attack cannot be performed straight forward. Otherwise, a third party Trudy could leave untouched the first 128 bits of the message and change as she needs the remaining bits. So, let's call $M=M_{128}||M_{>128}$, she can craft a new message $M'$ such that $M'=M_{128}||M_{TRUDY}$, the verification step will give back a positive response since the first 128 bits are the previous ones.

2.3 A symmetric scheme, like the one used by Alice and Bob, can be exploit to reach integrity and data origin authentication, but it must care of all the message. For example they could use a block cipher in CBC mode, keeping AES-256 and the already chosen key K, and compute the authentication tag of a message maintaining only the last cipher block of the encryption procedure. In this case the verification step will be still based on the encryption step, checking if the last cipher blocks match. Here the fundamental concern of a block cipher is the existential forgery problem: an attacker could exploit the nature of a block cipher in CBC mode which keeps only the last block, producing a valid authentication tag of a new never-exchanged message. This is because of the variable length of a message.
Let's suppose that Alice sent to Bob a message $M=m_1||m_2||m_3$ and its authentication tag called $t_1$. Let's assume another message $N=n_1||n_2||n_3$ and its authentication tag called $t2$. So, an attacker could forge a new message $P$ such that $P=m_1||m_2||m_3||(n_1+t_1)||n_2||n_3$ and the authentication tag of this message will be $t_2$, which is valid! The problem here is that the cycling nature of a block cipher in CBC mode removes the contribution of $M$ in the first part of the message $P$, such that the only part which will be considered is the one related to $N$. To mitigate this problem we can prepend to each message its length, avoiding so the above situation. Another fix could be to generate a different key based on the length of the message and the pre shared secret K: in this case the 3 different authentication tag would be computed using a different key.



3.1 

- Let's suppose the seed $n_0$ is public. An hash function, although it is a cryptographic secure one, doesn't provide any kind of notion of randomness: from an input x we need to obtain the same output y of a fixed size. This means that, knowing $n_0$, we can generate locally the complete sequence of pseudo random numbers.
- Let's suppose $n_0$ is kept secret. In this case reverse a cryptographic secure hash function is not feasible by definition of the one-wayness property. So to break it, an attacker needs a collision of at least one pseudo random term and then he can check it trying to generate the following terms and see if they match. Unless the seed is kept secret, the sequence could be considered secret, but still somehow deterministic.

3.2

- Let's suppose the seed public. No different from the previous case. Double hashing doesn't add any kind of randomness in the sequence. It only skip one term each time.
- Let's suppose the seed private. Same previous considerations, the only change is the skipping of one term each time.

3.3

- Let's suppose the seed public. In this case randomness is guaranteed by the encryption algorithm. The security of the sequence is obviously related to the key which must be kept secret. Knowing the seed doesn't provide any kind of information. It can be considered a good PRNG.
- Let's suppose the seed private. No more security is reached. The security bottleneck is always the secret X. Let's suppose the the secret is stolen, since the scheme is symmetric, the secret seed could be decrypt and then re used.

3.4

- Let's suppose the seed public. In this case a seed public means that the "random" key used to encrypt a secret message X could be deterministically generated. No security at all is ensured. Keeping X secret is not enough, because it can be decrypted using the well known key $H(n_0)$.
- Let's suppose the seed is secret. In this case the random secret could be used for encrypt the secret message X. Now the existence of a secret message is not strictly required to be honest. The problem is still that an hash function generates deterministically following hash values starting from a seed. It must be kept secret! And collision could be found in any moment.



4.1 Meet-ITM vai di double DES

4.2 A Reflection Attack exploits the possibility by an attacker to start different communication sessions with an entity which he want to authenticate with, reusing some messages of one session in the other reaching is goal.
For example, let's suppose that the mutual authentication protocol based on a symmetric key between Alice and Bob is this one:

- A->B: I'm Alice, $N_A$
- B->A: $K_{AB}\{N_A\}, N_B$
- A->B: $K_{AB}\{N_B\}$

A Reflection attack will exploit Bob as an oracle to solve challenges without knowing the key shared between Alice and Bob. So:

First Session:

- T(A)->B: I'm Alice, $N_A$

- B->T(A): $K_{AB}\{N_A\}, N_B$

Now Bob expects Trudy to send the solved answer, but Trudy doesn't know the shared secret. She starts another session with Bob. 

Second Session:

- T(A)->B: I'm Alice, $N_B$

- B->T(A): $K_{AB}\{N_B\}, N_C$

Now Trudy has the solved challenge gently sent by Bob. She will discard the second session and will complete the first one, sending back to Bob the solved challenge $N_B$.

4.3 A Replay Attack exploits the possibility to reuse valid and legal messages exchanged in previous sessions, collected by an attacker. For example let's suppose no kind of freshness notion is inserted in the authentication protocol:

- A->B: $K_{AB}\{"\text{I'm Alice and this is our pre shared secret}"\}$

In this case it is quite intuitive that an attacker Trudy can sniff this packet and reuse it in another session faking Bob claiming she is Alice.



5.1 The Euler's Theorem says that given two integers $a$ and $b$, such that $gcd(a,b)=1$, i.e. they are coprime, so: $a^{\phi(b)}=1modb$, where $\phi(b)$ is the Euler's Totien, i.e. the number of coprimes of $b$ in the set $Z_b=\{0,...,b-1\}$. It is really important since it is used in RSA pub/pvt keys generation.

5.2 Session Filtering is stateful because the firewall itself maintains a lookup table for each connection in which its state is updated. Packets are not analyzed in an unrelated way, but if a packet refers to a connection already present in the lookup table, the packet is linked to it and then analyzed in a more specific context. 