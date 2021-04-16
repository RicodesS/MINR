1

- False
- False
- True
- True
- False
- True
- False
- True
- False
- False



2.1

- $M_1=D_k(C_1)+IV_1+IV_2$
- $M_2=D_k(C_2)+IV_2+C1$
- $M_{i+2}=D_k(C_{i+2})+C_i+C_{i+1}$, $\forall i>0$

2.2

- Encryption phase: encryption cannot be parallelized since each cipher text block needs two cipher text blocks previously computed, for all the blocks starting from the third. The second block needs the first cipher text block too. No preprocessing can be performed.
- Decryption phase: decryption can be parallelized since to decrypt a block it needs only the i-th cipher text block and after that the xor operations requires Initial Vectors 1 and 2 and previously already obtained cipher text blocks. So since no dependency on plaintext blocks is present, it can be parallelized. Preprocessing is not useful since no operationts before decryption need to be performed.

2.3 In the first block there are two initial vectors. This means that, since they are xored, they need to be different, otherwise we cannot avoid pattern in the first block of the message M. This is due the xor operation which will cancel the random effect brought by the initial vectors. At least one must change for each message, in this way the first block would be different each time the same message is encrypted. Changing the first block means changing also second one, since there is a dedpendency on the first cipher text block. There is no need to keep them secret if at least one change for each message.



3.1 The machine, on which the firewall is implemented, allows (-j ACCEPT) TCP segments with the SYN flag set (-p TCP --syn the first sender's packet in the tcp handshake protocol must have that flag set, i.e. firewall accepts to start a tcp handshake protocol) that come from the interface called eth0 with a rate limit of 5 requests at second.

3.2 The machine, on which the firewall is implemented, is allowed (-j ACCEPT) to contact http/https services (-p tcp --dports 80,443)  if the outgoing interface is eth0, the state of the packet is in {NEW, ESTABLISHED, RELATED} (it can start a connection NEW, it can continue a connection ESTABLISHED, it can perform RELATED requests to a previous connection) if its source port is in the range [1026:65535] (a non admin port).

3.3 The machine, on which the firewall is implemented, allows the forwarding of packets (-j FORWARD) coming from any IP address but through the eth0 interface which are desinated to a local host 192.168.1.58 connected to the eth1 interface, if they use tcp protocol and a non admin source port in the range [1024:65535] in order to access http and https services on that machine (--dports 80,443).



4.1 This is a case of a non confidential service. We can only setup a SA (bilateral) between the Bob's gateway and the corporate's gateway in tunnel mode which exploits ESP with Authentication enabled. In this case ESP will provide confidentiality about the PDF content for the printer and authentication of Bob's gateway for accessing the local corporate network. Moreover, tunnel mode hide the original IP Header preventing third evil party to analyze traffic between two endpoints.

4.2 In this case I would setup two different SAs (bilateral), one in Transport mode and the other in Tunnel mode. The Tunnel will be put between Alice's gateway and corporate's gateway, like the previous example of Bob. Also ESP with Authentication enabled will be used. But since the document that Alice must send has to be confidential also inside the corporate's network I need another SA in trasport mode between Alice's host and Alice's office computer which must guarantee confidentiality. I can use again ESP with authentication enabled since the only person who must be able to connect to Alice's office computer is her. 