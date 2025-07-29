### **COMP6453: Applied Cryptography — Week 2 Lecture Notes**

**Topic: Symmetric-Key Encryption**

These notes synthesise the lecture slides and the accompanying verbal transcript, providing a comprehensive and detailed account of the concepts discussed.

### **1.0 Introduction and Recap**

The lecture begins with a recap of foundational concepts from the previous week, setting the stage for a deeper exploration of symmetric-key encryption.

*   **Encryption vs. Authentication:** A distinction is drawn between the two core goals of cryptography. Encryption is concerned with providing **confidentiality** by hiding the content of messages. Authentication, conversely, focuses on **verifying identity**, such as the source of a message (source authentication) or that the message has not been altered (integrity).
*   **Classical Ciphers:** The lecture references classical systems like substitution ciphers (e.g., the Caesar cipher) and the vulnerability of such systems to statistical attacks like frequency analysis.
*   **XOR and the One-Time Pad (OTP):** The simple yet powerful XOR operation is reintroduced as a fundamental building block for encryption, leading directly to the concept of the One-Time Pad.

### **2.0 Fundamental Concepts of Symmetric-Key Encryption**

This section formally defines the components and properties of a symmetric-key encryption scheme.

#### **2.1 Formal Definition of a Symmetric Cipher**

A symmetric-key cipher, also known as a Shannon Cipher, is a cryptographic system where the same key is used for both encryption and decryption.

*   **Key Concept:** A cipher is defined over three distinct sets: a message space `ℳ` (all possible plaintexts), a key space `𝒦` (all possible keys), and a ciphertext space `𝒞` (all possible encrypted messages). It consists of a pair of efficient algorithms, Encryption (`E`) and Decryption (`D`).
*   **Formal Definition (Slide 3):**
    *   Encryption Function: `E : ℳ × 𝒦 → 𝒞`
    *   Decryption Function: `D : 𝒞 × 𝒦 → ℳ`
    *   **Correctness Property:** For any message `m ∈ ℳ` and any key `k ∈ 𝒦`, the following must hold true:
        `D(E(m, k), k) = m`
        This ensures that a message encrypted with a key can be correctly decrypted using the same key.
*   **Algorithmic Properties (Slide 3 & Transcript):**
    *   The encryption algorithm `E` is often **randomised**. This is a crucial property to prevent an attacker from observing that the same message has been encrypted multiple times. If encryption were deterministic, encrypting the same plaintext would always produce the same ciphertext, leaking valuable information.
    *   The decryption algorithm `D` is always **deterministic**. Given a specific ciphertext and key, there must be only one possible plaintext output.

#### **2.2 The One-Time Pad (OTP)**

The One-Time Pad is a theoretically perfect, yet often impractical, symmetric encryption scheme. It was first described by Gilbert Vernam in 1917.

*   **Key Concept:** The OTP encrypts a plaintext message by performing a bitwise XOR operation with a secret key of the same length.
*   **Formalism (Slides 4 & 5):**
    *   Let the message space, key space, and ciphertext space be the set of all n-bit binary strings: `ℳ = 𝒦 = 𝒞 = {0,1}ⁿ`.
    *   Encryption: `C = E(M, K) = M ⊕ K`
    *   Decryption: `D(C, K) = C ⊕ K = (M ⊕ K) ⊕ K = M`
*   **Example (Slide 4):**
    *   Message `M`: `0111100101`
    *   Key `K`: `1100100100`
    *   Ciphertext `C`: `1011000001`
*   **Advantages & Disadvantages (Slide 5):**
    *   **Advantages:** It is conceptually simple and computationally very fast.
    *   **Disadvantages:** The key must be at least as long as the message, which is impractical for large messages (e.g., a 1 GB message requires a 1 GB key). Secure generation and distribution of such long keys is a significant logistical challenge.
*   **Caveat: The "One-Time" Rule:** The most critical security requirement of the OTP is that a key must be used **only once**. Reusing a key is catastrophic to security.
    *   **Mechanism of Failure:** If two messages, `m₁` and `m₂`, are encrypted with the same key `k`, an adversary who intercepts both ciphertexts (`c₁ = m₁ ⊕ k` and `c₂ = m₂ ⊕ k`) can compute their XOR:
        `c₁ ⊕ c₂ = (m₁ ⊕ k) ⊕ (m₂ ⊕ k) = m₁ ⊕ m₂`
    *   **Information Leakage:** This leaks the XOR sum of the two plaintexts. While this may not reveal the plaintexts directly, it provides significant information. For instance, if parts of one message are known, the corresponding parts of the other message can be deduced. An attacker with control over one plaintext (a chosen-plaintext scenario) could set `m₂` to a string of zeros, thereby recovering `m₁` completely (`c₁ ⊕ c₂ = m₁ ⊕ 0 = m₁`).

### **3.0 Security Models and Definitions**

To reason about the security of a cipher, we must first define the capabilities of the adversary and the goals of security.

#### **3.1 Attacker Capabilities (Attack Models)**

These models formalise what information and access an adversary is assumed to have. The lecturer clarifies these using the concept of a cryptographic **oracle**—a black-box entity that performs a cryptographic operation (e.g., encryption or decryption) on demand.

*   **Ciphertext-Only Attack (COA):** The adversary possesses one or more ciphertexts and has no other information. This is the weakest adversarial model, representing a passive eavesdropper.
*   **Known-Plaintext Attack (KPA):** The adversary possesses one or more plaintext-ciphertext pairs `(x, y)`. This model assumes the adversary has somehow obtained plaintext corresponding to some intercepted ciphertexts.
*   **Chosen-Plaintext Attack (CPA):** The adversary can obtain the ciphertext for any plaintext of their choosing. This is modelled as the adversary having access to an **encryption oracle**. The adversary can repeatedly query this oracle with chosen plaintexts `xᵢ` to receive corresponding ciphertexts `yᵢ`. This is a more powerful model than KPA because the adversary actively selects plaintexts that might reveal the most information.
*   **Chosen-Ciphertext Attack (CCA):** The adversary can obtain the plaintext for any ciphertext of their choosing (with the potential exception of the target ciphertext to be broken). This is modelled as the adversary having access to a **decryption oracle**. This is generally the strongest and most realistic model for many modern applications.

#### **3.2 Defining Security: Perfect Secrecy**

Claude Shannon, the father of information theory, provided the first formal, mathematical definition of perfect security in 1949.

*   **Key Concept:** A ciphertext should reveal absolutely no information about the plaintext from which it was generated.
*   **Formal Definition (Information Theoretic Security) (Slide 8):** A cipher `(E, D)` over `(ℳ, 𝒦, 𝒞)` has **perfect secrecy** if for all messages `m₀, m₁ ∈ ℳ` of the same length, and for all ciphertexts `c ∈ 𝒞`, the following holds:
    `P[E(k, m₀) = c] = P[E(k, m₁) = c]`
    where the key `k` is chosen uniformly at random from the key space `𝒦`.
*   **Interpretation (Indistinguishability):** This definition means that given a ciphertext `c`, an adversary cannot distinguish whether the original plaintext was `m₀` or `m₁`. The probability of `c` being the encryption of `m₀` is identical to the probability of it being the encryption of `m₁`. Therefore, observing the ciphertext provides no additional information to help the adversary guess the plaintext.

#### **3.3 Security Analysis of the One-Time Pad**

The One-Time Pad is the canonical example of a cipher that achieves perfect secrecy.

*   **Proof of Perfect Secrecy (Slide 9):**
    1.  For any plaintext `m` and ciphertext `c`, the encryption equation `E(m, k) = c` implies `m ⊕ k = c`.
    2.  This means the key `k` must be `k = m ⊕ c`.
    3.  For a given `m` and `c`, there is exactly **one** key `k` in the key space `𝒦` that satisfies this relationship.
    4.  Therefore, the number of keys that map `m` to `c` is exactly 1.
    5.  The probability of a randomly chosen key `k` mapping `m` to `c` is:
        `P[E(m, k) = c] = |{k ∈ 𝒦 : E(m, k) = c}| / |𝒦| = 1 / |𝒦|`
    6.  Since this probability is independent of the message `m`, it holds that for any `m₀, m₁`:
        `P[E(m₀, k) = c] = 1 / |𝒦| = P[E(m₁, k) = c]`
    7.  This satisfies the definition of perfect secrecy.
*   **Property of Perfect Secrecy (Slide 10):** A fundamental theorem proven by Shannon states that for any cipher with perfect secrecy, the size of the key space must be greater than or equal to the size of the message space: `|𝒦| ≥ |ℳ|`. This confirms the impracticality of perfect secrecy for general-purpose encryption. (Reference: Boneh-Shoup, Section 2.1.3).

### **4.0 Practical Stream Ciphers and Pseudorandomness**

To overcome the key-length limitation of OTP, practical systems use **stream ciphers**, which rely on Pseudo-Random Generators (PRGs).

#### **4.1 The Stream Cipher Construction**

*   **Key Concept:** Instead of a long, truly random key, a stream cipher uses a short, truly random key (called a **seed**, `s`) as input to a deterministic algorithm called a **Pseudo-Random Generator (PRG)**. The PRG expands this short seed into a long **keystream**, which *looks* random. This keystream is then XORed with the plaintext, mimicking the OTP.
*   **Diagram and Process (Slide 12):**
    1.  Start with a short, secret key (seed) `s`.
    2.  Use a PRG `G` to generate a long keystream: `K = G(s)`. The length of `K` is equal to the length of the message `M`.
    3.  Encryption: `C = M ⊕ K = M ⊕ G(s)`
    4.  Decryption: `M = C ⊕ K = C ⊕ G(s)`
*   **Security Implication:** This construction does not have perfect secrecy. Because the PRG `G` is a deterministic function, the resulting keystream `K` is not truly random; it is **pseudo-random**. The security of the cipher now depends entirely on the quality of the PRG. A weaker notion of security, known as **semantic security**, is used to analyse such systems.

#### **4.2 Pseudo-Random Generators (PRGs)**

A PRG is a deterministic function `G: {0,1}ˢ → {0,1}ᴸ` that stretches a short random seed of length `s` into a much longer pseudo-random output of length `L` (where `s ≪ L`).

*   **Core Security Goal:** An adversary should not be able to distinguish the output of the PRG from a truly random string of the same length.
*   **Security Requirement 1: Passing Statistical Tests (Slide 13):** The output of a PRG should have good statistical properties, similar to a truly random string.
    *   **Simple Tests:** Count the occurrences of `1`s (should be `≈ L/2`), pairs like `00, 01, 10, 11` (each should be `≈ L/4`), triplets (each `≈ L/8`), etc.
    *   **Caveat:** Passing a set of simple statistical tests is necessary but not sufficient for security.
*   **Security Requirement 2: Unpredictability (The Next-Bit Test) (Slide 14):** This is a stronger, more formal requirement.
    *   **Concept:** Given the first `i` bits of a PRG's output, it should be computationally infeasible to predict the `(i+1)`-th bit with a probability significantly better than 50% (random guessing).
    *   **Formal Definition:** A PRG `G` is considered **predictable** (and thus insecure) if there exists an efficient algorithm `A` and an index `i` such that:
        `Pr[ A(G(k)|₁...ᵢ) = G(k)|ᵢ₊₁ ] > 1/2 + ε`
        where `k` is a random seed, `G(k)|₁...ᵢ` denotes the first `i` bits of the output, and `ε` is a "non-negligible" advantage. In theoretical cryptography, any advantage `ε > 0`, no matter how small, is considered a break.
    *   **Consequence of Predictability:** If an adversary can predict a bit of the keystream, they can decrypt the corresponding bit of the plaintext.
*   **Examples of Insecure PRGs (Slide 15):**
    *   **Linear Congruential Generators (LCG):** `r[i] ← (a * r[i-1] + b) mod p`. These are predictable and not suitable for cryptographic use.
    *   **Glibc `random()`:** `r[i] ← (r[i-3] + r[i-31]) mod 2³²`. This is also predictable. Kerberos v4 used a similar construction and was successfully attacked.
*   **Caveat:** The existence of a provably secure PRG (one that can be formally proven to be unpredictable against all efficient adversaries) is an open problem in computer science and is conjectured to be equivalent to the existence of one-way functions.

### **5.0 Attacks on Stream Ciphers in Practice**

Theoretical weaknesses in stream cipher design have led to famous real-world attacks.

#### **5.1 Attack 1: Key Reuse**

This attack, identical to the OTP key reuse attack, is the most common and severe mistake when using stream ciphers.

*   **Real-World Example 1: Project Venona (1940s):** Soviet intelligence agencies reused OTP keys, allowing US and UK codebreakers to decrypt thousands of messages.
*   **Real-World Example 2: MS-PPTP:** The Point-to-Point Tunneling Protocol in early Windows versions used the same key for both directions of a bidirectional channel, enabling key reuse attacks. Best practice dictates using separate keys for each direction (`k_client→server` and `k_server→client`).
*   **Real-World Example 3: 802.11b WEP (Slide 20):**
    *   **Vulnerability:** WEP combines a long-term secret key `k` with a 24-bit **Initialization Vector (IV)** to form the per-frame key for the PRG (RC4). The keystream is `PRG(IV || k)`.
    *   **Key Reuse:** Since the IV is only 24 bits long, it is guaranteed to repeat after 2²⁴ (≈16.7 million) frames (the "Birthday Problem" makes collisions likely even sooner). This reuse of `(IV || k)` leads to a reuse of the entire keystream. Furthermore, some devices would reset the IV to 0 on power cycle, making collisions immediate.
    *   **Related-Key Attack:** The keys for consecutive frames (e.g., `(IV || k)` and `(IV+1 || k)`) are highly related, not independent. This relationship can be exploited in attacks against certain PRGs like RC4.
    *   **Better Construction (Slide 21):** A much better approach is to use the master key `k` to generate one very long keystream via a PRG, and then use different, non-overlapping chunks of this keystream (`K₁, K₂, K₃, ...`) to encrypt each frame.

#### **5.2 Attack 2: Malleability (Lack of Integrity)**

Stream ciphers, like OTP, are highly **malleable**, meaning an attacker can systematically modify a ciphertext to induce a predictable change in the corresponding plaintext upon decryption, without being detected.

*   **Mechanism (Slide 22):**
    1.  A legitimate ciphertext is `C = M ⊕ K`.
    2.  An attacker intercepts `C` and flips some bits by XORing it with a chosen value `p`. The new ciphertext is `C' = C ⊕ p = (M ⊕ K) ⊕ p`.
    3.  When the receiver decrypts `C'`, they compute:
        `D(C', K) = C' ⊕ K = (M ⊕ K ⊕ p) ⊕ K = M ⊕ p`.
    4.  The result is the original plaintext with the same bit-flips applied (`M ⊕ p`).
*   **Example (Transcript):** An attacker wants to change the recipient in a message from "Bob" to "Eve".
    1.  The attacker computes `p = "Bob" ⊕ "Eve"` using their ASCII values.
    2.  Let `C_bob` be the ciphertext part corresponding to "Bob". The attacker creates `C'_eve = C_bob ⊕ p`.
    3.  When the receiver decrypts this modified part of the ciphertext, they will recover "Eve" instead of "Bob". This breaks the **integrity** of the message.

### **6.0 A Brief Survey of Stream Cipher Constructions**

#### **6.1 RC4 (Rivest Cipher 4)**

*   **History:** Designed in 1987, RC4 was widely used in protocols like SSL/TLS and WEP. It is now considered broken and deprecated.
*   **Weaknesses (Slides 24 & 25):**
    *   **Biased Output:** The initial bytes of the RC4 keystream are not uniformly random. For example, the second byte has a significantly higher probability of being zero (`Pr[z₂ = 0] ≈ 2/256`).
    *   **Related-Key Vulnerabilities:** It is weak when used with keys that are related to each other, as was the case in the WEP protocol.

#### **6.2 Linear Feedback Shift Registers (LFSRs)**

*   **Concept (Slide 26):** An LFSR is a simple hardware mechanism for generating bit sequences. It consists of a register of bits that are shifted at each step, with a new bit being generated by XORing the values at specific "tap" positions in the register.
*   **Security:** A single LFSR produces a predictable, periodic sequence and is cryptographically insecure. Practical systems like A5/1 (used in GSM) and E0 (Bluetooth) use complex, non-linear combinations of multiple LFSRs, but many of these have also been found to be weak.

#### **6.3 Modern Stream Ciphers (e.g., eSTREAM)**

Modern stream ciphers address the key reuse problem at the design level by incorporating a **nonce**.

*   **Nonce:** A nonce is a "number used once." For a given key, the nonce is a unique, non-repeating value for each encryption operation. It does not need to be secret, only unique.
*   **Construction (Slide 27):**
    `E(k, m; r) = m ⊕ PRG(k; r)`
    where `k` is the secret key and `r` is the public nonce.
*   **Security Rule:** The pair `(k, r)` must never be used more than once. By changing the nonce for every message, a different keystream is generated even when the same key `k` is used, thus preventing the catastrophic key reuse attack.
*   **Examples (eSTREAM Competition):** The eSTREAM project selected a portfolio of well-analysed, high-performance stream ciphers.
    *   **Software Profile:** Salsa20 (and its successor ChaCha), HC-128, Rabbit.
    *   **Hardware Profile:** Trivium, Grain.
*   **Caveat:** While these ciphers have withstood years of public scrutiny and are considered secure, they do not have formal proofs of security in the way a system like OTP has perfect secrecy. Their security relies on the conjectured hardness of distinguishing their output from random.

