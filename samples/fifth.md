### **1.0 Introduction and Recap**

This lecture delves into the formal definitions and notions of security in cryptography, moving beyond the concept of perfect secrecy to computational security.

#### **1.1. Lecture Recap**

A review of concepts from the previous lecture includes:
*   The **One-Time Pad (OTP)** and its property of **perfect secrecy**.
*   The construction of **stream ciphers** using **Pseudorandom Generators (PRGs)**, where a short seed is expanded into a long keystream.
*   The use of **statistical tests** to verify that a PRG's output is computationally indistinguishable from a truly random stream.
*   **Block ciphers**, including historical (DES) and modern (AES) standards.
*   **Modes of operation** for block ciphers.

#### **1.2. Overview of Security Concepts**

The lecture contrasts different levels and models of security:
*   **Perfect Security:** An information-theoretic notion achieved by the OTP, where the ciphertext reveals absolutely no information about the plaintext. Stream ciphers, however, are not perfectly secure because the key (or seed) is shorter than the message.
*   **Computational Security:** A more practical approach where security holds against adversaries with bounded computational power (e.g., those running in probabilistic polynomial time).
*   **Attack Models:** These define the capabilities of an adversary.
    *   **Ciphertext-Only Attack (COA):** The adversary only has access to ciphertexts.
    *   **Known-Plaintext Attack (KPA):** The adversary has access to a set of plaintext-ciphertext pairs.
    *   **Chosen-Plaintext Attack (CPA):** The adversary can choose plaintexts and receive their corresponding ciphertexts from an encryption oracle.
    *   **Chosen-Ciphertext Attack (CCA):** The adversary can choose ciphertexts and receive their corresponding plaintexts from a decryption oracle.
*   **Adaptive vs. Non-adaptive Attacks:** An adaptive adversary can choose its queries to encryption/decryption oracles based on the results of previous queries. A non-adaptive adversary must decide all its queries in advance.
*   **Indistinguishability:** A core principle in modern cryptography. A scheme is secure if an adversary cannot distinguish between the encryptions of two different messages of their choice, or between a "real" cryptographic object (like a PRG output) and an "ideal" one (a truly random string).

### **2.0 Revisiting Symmetric Key Encryption (SKE)**

A formal definition of a Symmetric Key Encryption (SKE) scheme is foundational to discussing its security.

#### **2.1. Key Concept: Formal Definition of an SKE Scheme**

An SKE scheme `ℰ` is a tuple of three algorithms `(KeyGen, E, D)` defined over a message space `ℳ`, a ciphertext space `𝒞`, and a key space `𝒦`.

1.  **`KeyGen(1^k) → k ∈ 𝒦`**: The key generation algorithm takes a security parameter `k` (sometimes denoted `λ`) as input and outputs a key `k` from the key space `𝒦`.
2.  **`E(k, m) → c`**: The encryption algorithm takes a key `k ∈ 𝒦` and a message `m ∈ ℳ` as input and outputs a ciphertext `c ∈ 𝒞`. This can be a probabilistic algorithm.
3.  **`D(k, c) → m'`**: The decryption algorithm takes a key `k ∈ Ω` and a ciphertext `c ∈ 𝒞` as input and outputs a message `m' ∈ ℳ`. This is typically a deterministic algorithm.

#### **2.2. Key Concept: Correctness**

For an SKE scheme to be useful, it must be correct. This means that decrypting a ciphertext must yield the original plaintext.

**Formal Definition:**
An SKE scheme `ℰ` is correct if for all keys `k ∈ 𝒦` and all messages `m ∈ ℳ`, the following holds with probability 1:
`D(k, E(k, m)) = m`

This can be expressed as: if `c ← E(k, m)` and `m' ← D(k, c)`, then `m = m'`.

### **3.0 Semantic Security**

Semantic security is a formal, game-based definition of security for encryption schemes. It captures the intuition that a ciphertext should reveal no partial information about the underlying plaintext.

#### **3.1. Key Concept: The Semantic Security Game (IND-OT-CPA)**

Semantic security is defined via a game between a **Challenger** and an **Adversary `A`**. This specific game formalises security against a one-time chosen-plaintext attack.

**The Game:**
1.  **Setup:** The Adversary `A` chooses two distinct messages, `m₀` and `m₁`, from the message space `ℳ`. A critical constraint is that the messages must have the same length: `|m₀| = |m₁|`. The adversary sends these to the Challenger.
2.  **Challenge:** The Challenger secretly and uniformly at random selects a bit `b ∈ {0, 1}`. It then generates a fresh key `k ← KeyGen(1^k)` and computes the challenge ciphertext `c ← E(k, m_b)`. The Challenger sends `c` back to the Adversary.
3.  **Guess:** After receiving `c`, the Adversary `A` must output a guess, `b'`, for the bit `b`.
4.  **Winning:** The Adversary wins the game if its guess is correct, i.e., `b' = b`.

The game can be viewed as two distinct experiments, `EXP(0)` and `EXP(1)`, where in `EXP(b)`, the Challenger encrypts `m_b`. The adversary's goal is to distinguish which experiment was run.

**Diagram of the Game:**
```
      Challenger                           Adversary A
      ----------                           -----------
      b R {0, 1}
      k ← KeyGen()
                                     m₀, m₁  (where |m₀|=|m₁|)
                                     --------------------------->
      c ← E(k, m_b)
                                     <---------------------------
                                           c

                                     b' ∈ {0, 1}
                                     --------------------------->
```

#### **3.2. Key Concept: Adversarial Advantage**

The advantage of an adversary `A` in the semantic security game measures how much better `A` is at guessing the bit `b` than random chance (which would be a probability of 1/2).

Let `W_b` be the event that the adversary outputs `1` when the challenger's bit was `b`.
*   `Pr[W₀]` is the probability that `A` outputs `1` given an encryption of `m₀`.
*   `Pr[W₁]` is the probability that `A` outputs `1` given an encryption of `m₁`.

The **Semantic Security Advantage** of `A` against the scheme `ℰ` is defined as:
`AdvSS[A, ℰ] := | Pr[W₀] - Pr[W₁] |`

Alternatively, this can be expressed as: `Adv[A, ℰ] = 2 * | Pr[A wins] - 1/2 |`.

#### **3.3. Key Concept: Definition of Security**

An encryption scheme `ℰ` is **semantically secure** if for all efficient (Probabilistic Polynomial Time, or PPT) adversaries `A`, the advantage `AdvSS[A, ℰ]` is a **negligible function** in the security parameter `k`.

A negligible function `negl(k)` is one that decreases faster than the inverse of any polynomial in `k`. Intuitively, this means the adversary's advantage is effectively zero for any practical security level.

#### **3.4. Example: Breaking Semantic Security with an LSB Oracle**

This example demonstrates that if an adversary can learn even a single bit of information about the plaintext from the ciphertext, the scheme is not semantically secure.

**Scenario:** Suppose we have an efficient adversary `A` that, given a ciphertext `c`, can always correctly deduce the Least Significant Bit (LSB) of the original plaintext. We will use `A` to construct another adversary, `B`, that wins the semantic security game with a non-negligible advantage.

**Adversary `B`'s Strategy:**
`B` plays the semantic security game against a challenger for the scheme `ℰ`.
1.  **Setup:** `B` chooses two messages, `m₀` and `m₁`, such that `LSB(m₀) = 0` and `LSB(m₁) = 1`. `B` sends these to its challenger.
2.  **Challenge:** The challenger responds with a ciphertext `c = E(k, m_b)` for some secret bit `b`.
3.  **Guess:** `B` feeds the ciphertext `c` to the given adversary `A`. Since `A` can deduce the LSB of the encrypted message, `A` will output `LSB(m_b)`. By our construction, `LSB(m_b) = b`. Therefore, `B` uses `A`'s output as its own guess, `b'`.

**Analysis of `B`'s Advantage:**
*   If the challenger's bit was `b=0`, `A` receives `c = E(k, m₀)` and outputs `LSB(m₀) = 0`. So, `B` guesses `0`.
*   If the challenger's bit was `b=1`, `A` receives `c = E(k, m₁)` and outputs `LSB(m₁) = 1`. So, `B` guesses `1`.

`B` always wins. Let's calculate its advantage formally:
`Pr[B outputs 1 | b=0] = Pr[W₀] = 0`
`Pr[B outputs 1 | b=1] = Pr[W₁] = 1`

`AdvSS[B, ℰ] = | Pr[W₀] - Pr[W₁] | = |0 - 1| = 1`

Since the advantage is 1 (which is non-negligible), the encryption scheme `ℰ` is **not semantically secure**. This method of using a hypothetical adversary for one task to build a winning adversary for another is a standard proof technique called a **security reduction**.

### **4.0 Relationship to Other Security Notions**

#### **4.1. Key Concept: Message Recovery Attacks**

Intuitively, a basic security requirement is that an adversary should not be able to recover the entire plaintext from a ciphertext. We can formalise this and show that semantic security is a stronger guarantee.

**The Message Recovery (MR) Game:**
1.  **Challenge:** The Challenger chooses a message `m` uniformly at random from the message space `ℳ` (`m R ℳ`). It generates a key `k R 𝒦` and computes `c ← E(k, m)`. The challenger sends `c` to the Adversary `A`.
2.  **Guess:** The Adversary `A` outputs a guess `m̂ ∈ ℳ`.
3.  **Winning:** The Adversary wins if `m̂ = m`.

The probability of winning by random guessing is `1/|ℳ|`. The **Message Recovery Advantage** is defined as how much better the adversary does than random guessing:
`AdvMR[A, ℰ] = |Pr[A wins] - 1/|ℳ||`

#### **4.2. Proof Sketch: Semantic Security implies Security against Message Recovery**

We can prove that if a scheme `ℰ` is semantically secure, then no efficient adversary can succeed in a message recovery attack with non-negligible advantage. The proof is a reduction: we assume an adversary `A` exists that can win the MR game and use it to build an adversary `B` that breaks semantic security.

**Adversary `B`'s Strategy (using MR adversary `A`):**
`B` plays the semantic security game against a challenger.
1.  **Setup:** `B` chooses two messages: `m₀` is a fixed, arbitrary message, and `m₁` is chosen uniformly at random from `ℳ`. `B` sends `m₀, m₁` to its challenger.
2.  **Challenge:** The challenger returns `c = E(k, m_b)`.
3.  **Guess:** `B` gives `c` to the MR adversary `A`. `A` returns a guess `m̂`. `B` then makes its own guess `b'` as follows:
    *   If `m̂ = m₁`, `B` guesses `b' = 1`.
    *   Otherwise, `B` guesses `b' = 0`.

**Analysis of `B`'s Advantage:**
Let `p` be the probability that adversary `A` wins the MR game, i.e., `p = Pr[A(E(k,m))=m]`.
Let `p_b` be the probability that `B` outputs `1` when the challenger's bit is `b`.
`AdvSS[B, ℰ] = |p₀ - p₁|`

*   **Case b=1:** The challenge is `c = E(k, m₁)`. `A` receives an encryption of the message it is trying to guess. The probability that `A` outputs `m₁` is exactly its success probability, `p`. Since `B` outputs `1` if and only if `A` outputs `m₁`, we have `p₁ = p`.
*   **Case b=0:** The challenge is `c = E(k, m₀)`. `A`'s output `m̂` is now independent of `m₁` (since `m₁` was chosen randomly by `B` and never used by the challenger). The probability that `A`'s output happens to equal `m₁` is the same as random guessing, so `p₀ = 1/|ℳ|`.

Putting it together:
`AdvSS[B, ℰ] = |p₀ - p₁| = |1/|ℳ| - p| = |p - 1/|ℳ|| = AdvMR[A, ℰ]`

This reduction shows that the advantage of adversary `B` in the semantic security game is equal to the advantage of adversary `A` in the message recovery game. Therefore, if `ℰ` is semantically secure, `AdvSS[B, ℰ]` must be negligible, which implies `AdvMR[A, ℰ]` must also be negligible.

### **5.0 Security of Specific Ciphers**

#### **5.1. Proof: One-Time Pad (OTP) is Semantically Secure**

We can formally prove that the OTP meets the definition of semantic security.

**Game Analysis:**
Consider the semantic security game for OTP, where `E(k, m) = k ⊕ m`.
*   In `EXP(0)`, the adversary receives `c₀ = k ⊕ m₀`.
*   In `EXP(1)`, the adversary receives `c₁ = k ⊕ m₁`.

Since the key `k` is chosen uniformly at random from `{0,1}^n` and is used only once, both `c₀` and `c₁` are uniformly random strings in `{0,1}^n`. The distributions of the ciphertexts in both experiments are identical. An adversary receiving a uniformly random string can gain no information to distinguish whether it came from `m₀` or `m₁`.

**Formal Advantage Calculation:**
For any adversary `A` (even an unbounded one):
`Pr[A outputs 1 | c = k ⊕ m₀] = Pr[A outputs 1 | c = k ⊕ m₁]`
Because the inputs `k ⊕ m₀` and `k ⊕ m₁` follow the same probability distribution (the uniform distribution on n-bit strings).
Therefore, `Pr[W₀] = Pr[W₁]`.

`AdvSS[A, OTP] = | Pr[W₀] - Pr[W₁] | = 0`

Since the advantage is 0 (which is negligible), the OTP is semantically secure.

### **6.0 Indistinguishability and Pseudorandom Generators (PRGs)**

The concept of indistinguishability is central to proving the security of practical ciphers like stream ciphers, which rely on PRGs.

#### **6.1. Key Concept: Indistinguishability**

Indistinguishability is a general principle, often illustrated by the Turing Test (1950), where a human judge tries to distinguish between another human and a machine based on conversation. If the judge cannot tell them apart with significant success, the machine is said to be indistinguishable from a human in that context.

In cryptography, we apply this to computational objects. A **distinguisher** is an efficient (PPT) algorithm that tries to tell two types of objects apart.

#### **6.2. Key Concept: PRG Security via Indistinguishability**

A Pseudorandom Generator `G: 𝒦 → {0,1}^n` (where `|s| < n`) expands a short random seed `s ∈ 𝒦` into a longer pseudorandom string `G(s)`.

**The PRG Indistinguishability Game:**
1.  **Challenge:** A challenger flips a coin.
    *   If heads, it generates a truly random string `r` of length `n` (`r R {0,1}^n`).
    *   If tails, it generates a random seed `s R 𝒦` and computes the pseudorandom string `y = G(s)`.
    The challenger sends the resulting string (`r` or `y`) to a **Distinguisher** `D`.
2.  **Guess:** The distinguisher `D` outputs a bit: `1` if it thinks the string was pseudorandom, `0` if it thinks it was truly random.

**Definition of a Secure PRG:**
A PRG `G` is **secure** if its output is **computationally indistinguishable** from a truly random string. Formally, for any efficient distinguisher `D`, its advantage must be negligible:
`AdvPRG[D, G] := | Pr[D(G(s)) = 1] - Pr[D(r) = 1] | ≤ negl(k)`

#### **6.3. Theorem: Secure PRG implies Semantically Secure Stream Cipher**

This is a cornerstone theorem for practical symmetric cryptography.
**Theorem:** If `G` is a secure PRG, then the stream cipher `E` constructed from it, where `E(s, M) = G(s) ⊕ M`, is semantically secure.

**Proof Sketch:**
The proof is a reduction. We show that for any adversary `A` that can break the semantic security of the stream cipher `E`, we can construct a distinguisher `B` that breaks the security of the PRG `G`.
`∀ SS adversary A, ∃ a PRG distinguisher B s.t. AdvSS[A, E] ≤ 2 * AdvPRG[B, G]`

**Intuition:**
The semantic security game for the stream cipher involves distinguishing `c₀ = G(s) ⊕ m₀` from `c₁ = G(s) ⊕ m₁`. The security of the PRG states that `G(s)` is indistinguishable from a truly random string `r`.
This suggests that the stream cipher game `(distinguishing E(s,m₀) from E(s,m₁))` should be as hard as the OTP game `(distinguishing r ⊕ m₀ from r ⊕ m₁)`. We know the OTP game is impossible to win. The "gap" in security between the stream cipher and the ideal OTP is entirely dependent on the "gap" in quality between the PRG output `G(s)` and a truly random string `r`.

**The Reduction (Constructing Distinguisher `B` from Adversary `A`):**
1.  Distinguisher `B` is given a challenge string `y` (which is either truly random `r` or pseudorandom `G(s)`) from its PRG challenger. `B` must guess the origin of `y`.
2.  `B` will use the SS adversary `A` to help it guess. `B` simulates the semantic security challenger for `A`.
3.  `B` receives `m₀, m₁` from `A`.
4.  `B` computes a ciphertext `c = y ⊕ m₀` and sends it to `A`.
5.  `A` responds with its guess `b'`. `B` uses this to make its own decision. Let's say `B` outputs `1` if `A` outputs `1`.

**Analysis:**
Let's analyze the probability that `B` outputs 1.
`AdvPRG[B, G] = | Pr[B(r) = 1] - Pr[B(G(s)) = 1] |`
*   `Pr[B(G(s)) = 1]`: Here, `y = G(s)`. `B` gives `c = G(s) ⊕ m₀` to `A`. The probability that `A` outputs `1` is exactly `Pr[W₀]` from the original SS game.
*   `Pr[B(r) = 1]`: Here, `y = r`. `B` gives `c = r ⊕ m₀` to `A`. This is an OTP encryption of `m₀`. Let `Pr[R₀]` be the probability `A` outputs `1` in this OTP scenario.

So, `AdvPRG[B, G] = | Pr[R₀] - Pr[W₀] |`.

Using a proof technique involving a "hybrid argument" or the triangle inequality, we can relate the terms:
`AdvSS[A, E] = |Pr[W₀] - Pr[W₁]| ≤ |Pr[W₀] - Pr[R₀]| + |Pr[R₀] - Pr[R₁]| + |Pr[R₁] - Pr[W₁]|`

*   `|Pr[R₀] - Pr[R₁]| = AdvSS[A, OTP] = 0`, as shown before.
*   `|Pr[W₀] - Pr[R₀]| = AdvPRG[B, G]` for the adversary `B` we constructed using `m₀`.
*   `|Pr[W₁] - Pr[R₁]| = AdvPRG[B', G]` for a similar adversary `B'` constructed using `m₁`.

Assuming the best distinguisher can be constructed, this leads to the result: `AdvSS[A, E] ≤ 2 * AdvPRG[B, G]`.
Since `G` is a secure PRG, `AdvPRG[B, G]` is negligible. Therefore, `AdvSS[A, E]` must also be negligible, proving that the stream cipher `E` is semantically secure.

### **7.0 Summary and Methodological Takeaways**

The lecture establishes the modern, formal approach to proving cryptographic security. The key methodology for creating a security proof is as follows:

1.  **Define the Attack Model/Game:** Clearly specify the capabilities of the adversary and the rules of interaction with a challenger (e.g., semantic security game, message recovery game).
2.  **Define Adversarial Advantage:** Quantify what it means for an adversary to "win" the game, measuring its success relative to random guessing. A scheme is secure if this advantage is negligible for any efficient adversary.
3.  **Prove Security via Reduction:** To prove a new construction (e.g., a stream cipher) is secure, show that any adversary who breaks the new construction can be used as a subroutine to solve a problem believed to be hard (e.g., distinguishing a PRG's output from random). This demonstrates that the new construction is "at least as hard to break" as the underlying primitive.

