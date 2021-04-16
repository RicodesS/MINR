1 

- False
- False
- False
- False
- True
- True
- False
- True
- False
- False



2.1 The problem is that, since $Z_i$ is only 7 bits, Bob can pre compute quickly all the possible hash values by taking the nonce of Alice $n_B$, check what number Alice has chosen $Z_A$ and then find a value $Z_B$ such that the bet contained in $p$ is false, so Bob will win always.

2.2 If only hash functions can be used to hide the Alice choices, Alice must keep secretr the nonce $n_B$ until Bob will choose its own value $Z_B$:

- A->B: (p, h(Z_A || n_B)), where n_B is random and large enough to avoid brute force attack in a feasible time
- B->A: Z_B, now Bob can change is choice
- A->B: Z_A, n_B, now Bob can check the winner by computing the hash and check if it matches with the received one

A problem could be if the nonce $n_B$ and the choice $Z_A$ would be the same, but it is unlikely to happen due the random nature of $n_B$. Moreover, Alice cannot change $Z_A$ since Bob verifies that. 



4.1

- iptables -A INPUT -i eth1-p tcp --dport 22 -j ACCEPT
- iptables -A OUTPUT -o eth1 -p --sport 22 -j ACCEPT

4.2

- iptables -A FORWARD -i eth1 -o eth0 -j DROP

4.3

- iptables -A FORWARD -i eth0 -o eht1 -j DROP

