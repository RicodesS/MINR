1

- True
- False
- True
- False
- True
- True
- False
- True
- True
- False



2.1 A forgery attack about digital signature concerns the possibility to generate a valid and legal signature of a message m, not yet signed by anyone, without knowing the correct private key of an user. There are three types of forgery attack:

- Universal Forgery: for any message x, the attacker is able to forge the correct signature s. This is the most dangerous forgery attack that an attacker could perform.
- Selective Forgery: for a given message x, the attacker is able to forge the signature s. The message x can be seen as a challenge proposed by a "challenger".
- Existential Forgery: the attacker is able to forge at least one valid and legal signature s of a non-specific message x. The message can be meaningless.

2.2 

RSA signature algorithm is based on the public/private encryption schema. The pair of keys are generated in the same way as for the encryption algorithm. The only change is that they are used in the opposite way: the signer will use his own private key to sign the message, only him could sign that, and the others can verify it through its public key. The RSA signature algorithm based on the textbook version of RSA is insecure too. It suffers also of Existential Forgery, which allows an attacker to choose randomly the signature s and then retrieve the message which the signature correspond to. Standards versions of RSA signature scheme are available, that first of all uses a cryptographic secure hash function to prevent forgery attacks and to speed up signature operations. 

DSA instead, has its own key generation algorithm which requires to choose a big prime p between $2^{1023}$ and $2^{1024}$. Then there is needed a prime divisor of p-1, q which must be between $2^{159}$ and $2^{160}$. Then a generator $\alpha$ is chosen such that $ord(\alpha)=q$. The private key is called $d$ and must be chosen between 1 and $q$. The corresponding public key is $\alpha^dmodp=\beta$. The signature algorithm relies on SHA family of hash functions, like RSA signature standards. For each message, DSA requires an ephimeral key $K_e$ between 1 and q. Then two values are computed which compose the signature of the document x:

-  $r=(\alpha^{K_e}modp)modq$
- $s=(SHA(x)+rd)K_e^{-1}modq$

The verification algorithm will check $r=v$, where $v$ is computed like follows:

- $w=s^{-1}modq$
- $u_1=w*SHA(x)modq$
- $u_2=w*rmodq$
- $(\alpha^{u_1}*\beta^{u_2}modp)modq$

RSA is slower in signing than DSA since the private key of an user $d$ is often really large, so exponentiation is very expensive. DSA is slower in decryption than RSA since it must compute inverse of $s$ and exponentiation modq and modp.

2.3

- The first approach is the more expensive one in term of space. Document D is signed by Alice and not Bob, or it is signed by Bob and not Alice. This means that we have to store two different signatures to verify all the party involved in the contract.
- In this case, instead, Bob signs not only the document D but also the signature of Alice on the document D. We can interprete this approach as an iterative signign scheme. This allows Alice and Bob to store only the last signature, i.e. the Bob's one. In fact to check the party involved we can firstly retrieve D||SignA(D) using the public key of Bob, then retrieve D from SignA(D) using the publick key of Alice and if the obtained D' is equal to D then both Bob and Alice have signed the contract.



3.1The main idea behind IPSec is to encrypt and authenticate each datagram exchange between two network devices. The main advantage about this idea is that we can also decide to encrypt, and so hide, information about IP Headers. The drawback is about the increasing complexity of network hardwares which must cooperate among them and must be able to perform cryptographic operations in order to ensure confidentiality and authentication. Another good point about IPSec is that, since it acts between IP Layer and TCP Layer of the OSI Model, it is trasparent to applications, also to users, indeed it is a really good choice to use it for implementing a VPN between local networks. IPSec is a mechanism that provides three main security features:

- Confidentiality
- Authentication
- Key Management

It offers the possibility to be used in two different modes:

- Transport mode: it is really useful when we are talking about end-to-end secure communication
- Tunnel mode: it is the basis on which a VPN is implemented through IPSec

Notice that also combination of the two modes are supported. To provide Confidentiality and Authentication, IPSec implements two extensions of the IP Header called:

- Authentication Header: which an effective header which is inserted in the original IP packet to ensure authentication and data integrity.
- Encapsulating Secure Payload: which creates an encrypted envelope for the content of the original IP packet which must be kept confidential. Notice that this feature provides also some kind of Authentication withouth the need of using Authentication Header. This is done to let operations be lighter. 

Since IPSec is based on datagram protection, to be used it requires configuration of Security Associations between hops. A security Association provides a one-way cryptographically secure connection between two nodes of the network. It is important to underline that a bi-lateral secure communication is implemented through two different and opposite SAs.

3.2 IPSec could be used to implement for example a VPN between two local networks. In this case the two gateways of the networks would be configured to encrypt and authenticate the traffic between them, avoiding so the possibility to inspect the real local network's hosts involved in the communication and its content. Another usage of IPSec can be the remote access to a machine in a local network. Let's suppose to be in Covid pandemic, smartworking is continously being pushed to avoid aggregation of people in the office. IPSec can help to establish a authenticated and confidential access from a remote machine to the local's one.

3.3 Let's suppose that Alice and Bob work in different companies located in two different place in the world. Let's suppose also that the two companies have enstablished a VPN between their local private network to communicate in a secure fashion through IPSec. This prevent third evil people from the outside to inspect content of messages exchanged between them. But what if Alice doesn't want that other people in both companies could look into the secret message that she wants to send to Bob to the other part of the world? In this case a TLS end-to-end encryption provides the confidentiality to Alice's message inside the companies' networks. Moreover, the message is still protected by IPSec while moving through the VPN Tunnel.  