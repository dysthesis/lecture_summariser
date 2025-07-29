Of course. Here is a comprehensive and detailed set of lecture notes based on the provided materials.

***

### **COMP6453 — Lecture Notes: Zero-Knowledge Proofs (ZKP)**

#### **1.0 Introduction and Motivation for Zero-Knowledge Proofs**

Zero-Knowledge Proofs (ZKPs) are cryptographic protocols that allow one party, the **Prover**, to prove to another party, the **Verifier**, that a certain statement is true, without revealing any information beyond the validity of the statement itself. While the foundational concepts are decades old, recent advancements, particularly driven by applications in blockchain technology, have led to significant research and development in this area.

##### **1.1 The Essence of Proofs and Verifiability**

At its core, a proof is a method to establish the truth of a claim. This concept is fundamental across various domains, from legal and scientific to mathematical proofs built upon axioms and propositions. In the context of computer science and cryptography, we are primarily concerned with mathematical and probabilistic proofs.

A common real-world analogy is a driver's license. When used as a form of identification, for instance, to enter a venue that requires patrons to be over 18, the user reveals their exact date of birth, address, and other personal information. However, the only information the verifier (e.g., the venue's security) actually needs is whether the user's age is greater than 18. A ZKP, in this scenario, would allow the user to prove they are over 18 *without* revealing their date of birth. This concept is central to modern identity solutions like **verifiable credentials**, which enable selective disclosure of information.

The fundamental goal is to answer a query and prove that the result is correct without disclosing the underlying data used to generate that result. Key examples include:
*   Proving possession of sufficient funds in a bank account for a purchase without revealing the account balance.
*   Verifying that a Machine Learning (ML) algorithm has generated a correct model without accessing the proprietary algorithm or the sensitive training data.

**Slide Cross-Reference:** 4

##### **1.2 Key Applications of ZKPs**

ZKPs and their underlying proof systems have a wide range of applications, many of which focus on enhancing privacy, anonymity, and security.

*   **Identification and Signature Schemes:** ZKPs form the basis for advanced cryptographic schemes.
    *   **Anonymous Credentials:** As discussed, these allow a user to prove they possess certain attributes (e.g., are a student of a university, are over 18) without revealing their identity. The transcript also mentions the desirable "no phone home" property, where the issuer of a credential is not notified each time it is used, preventing surveillance.
    *   **Blind Signatures:** Proposed by David Chaum, these allow a user to have a message signed by an authority without the authority learning the content of the message. This is crucial in applications like e-voting, where a voter's choice must remain secret, but the vote itself must be authenticated as valid.
    *   **Ring Signatures:** These allow a member of a group (a "ring") to sign a message on behalf of the group, without revealing which specific member produced the signature. This provides anonymity within a set of potential signers. The Monero cryptocurrency uses ring signatures for anonymous transactions.

*   **Privacy-Preserving Transactions on Blockchains:**
    *   Standard blockchains like Bitcoin are pseudonymous but transparent; transaction amounts and the addresses of the sender/receiver are public.
    *   ZKP-enabled blockchains like **Zcash** and **Aleo** can conceal the value of transactions and the identities of the participants.
    *   **Tornado Cash** used ZKPs to create "privacy pools" for mixing transactions, though it faced legal sanctions.

*   **Blockchain Scalability (Rollups):**
    *   Blockchains face a scalability challenge, as every node must process every transaction, which can be slow (e.g., Bitcoin's 10-minute block time).
    *   **Rollups** are a "Layer 2" scaling solution where numerous transactions are executed off-chain. An operator batches these transactions, computes the resulting state change, and submits a small amount of compressed data along with a cryptographic proof (typically a SNARK) to the main blockchain.
    *   This proof efficiently convinces the main chain that all the off-chain transactions were executed correctly according to the rules, without the main chain needing to re-execute them. This dramatically increases transaction throughput.

*   **Verifiable Computation:** A client can outsource a heavy computation to a powerful but untrusted server (e.g., in a cloud environment). The server returns the result along with a proof that the computation was performed correctly. ZKPs can be used here to ensure the correctness of the computation without revealing sensitive inputs.

**Slide Cross-Reference:** 5, 6, 7, 8, 9, 74

---

#### **2.0 Foundations of Proof Systems**

A formal proof system involves a **Prover** (P) who makes a claim and provides a proof, and a **Verifier** (V) who checks the proof to either accept or reject the claim.

##### **2.1 Formal Definition**

Let `L` be a formal language, which is a set of strings over some alphabet Σ (e.g., the set of all binary strings representing 3-colourable graphs). The Prover wishes to prove the statement `x ∈ L` (e.g., "this graph `x` is in the language `L` of 3-colourable graphs").

The language `L` is defined as the set of statements `x` for which a **witness** `w` exists, such that a verification algorithm `V` would accept:
`L = {x | ∃w, V(w, x) = ACCEPT}`

A **proof system** for membership in `L` is an algorithm `V` that satisfies two fundamental properties:

1.  **Completeness:** If the statement is true, an honest Prover can convince the honest Verifier.
    *   For any true statement `x ∈ L`, there exists a witness `w` such that `V(w, x) = ACCEPT`.

2.  **Soundness:** If the statement is false, no Prover (even a cheating one) can convince the honest Verifier that it is true.
    *   For any false statement `x ∉ L`, for all possible witnesses `w'`, `V(w', x) = REJECT`.

**Citation:**
*   Babai, L. (1985). Trading Group Theory for Randomness.
*   Goldwasser, S., Micali, S., & Rackoff, C. (1985). The Knowledge Complexity of Interactive Proof-Systems.

**Slide Cross-Reference:** 11, 12, 14

##### **2.2 Efficient Proofs (NP-Proofs)**

For a proof system to be practical, it must be efficient. This leads to the notion of an **NP-Proof System**, which adds efficiency constraints. The class NP (Nondeterministic Polynomial-Time) consists of problems for which a proposed solution (a witness or certificate) can be verified in polynomial time.

An **NP-Proof System** adds the following requirements to the standard definition:

1.  **Completeness (with short witness):** If `x ∈ L`, there exists a witness `w` whose size is polynomial in the size of the input `x` (i.e., `|w| = poly(|x|)`) such that `V(w, x) = ACCEPT`.
2.  **Soundness:** (Same as before) If `x ∉ L`, for all `w'`, `V(w', x) = REJECT`.
3.  **Efficiency (Fast Verification):** The verification algorithm `V(w, x)` must run in time that is polynomial in the size of the input `x` (i.e., it halts after at most `poly(|x|)` steps).

In this model, the Prover may have unbounded computational power to find the witness `w`, but verifying the witness must be fast. For practical systems, reducing the Prover's computational cost is also a major goal of modern research.

**Slide Cross-Reference:** 13, 15

##### **2.3 The Problem: Proofs Leak Secrets**

A naive proof system often involves the Prover simply sending the witness `w` to the Verifier.

**Example: Quadratic Residuosity**
Let `QRN` be the language of quadratic residues modulo `N`. A number `x` is a quadratic residue modulo `N` if there exists a number `w` such that `x ≡ w² mod N`. `w` is the square root of `x`.

*   **Claim:** `x ∈ QRN`.
*   **Prover's Proof:** The Prover, knowing `w` such that `x ≡ w² mod N`, sends `w` to the Verifier.
*   **Verifier's Check:** The Verifier computes `w² mod N` and checks if it equals `x`.

This system is complete and sound. However, the Prover has revealed `w` (the secret) to the Verifier. This is information the Verifier could not have computed on their own (as finding square roots modulo `N` is computationally hard and equivalent to factoring `N`). This leakage is undesirable.

**The goal of Zero-Knowledge is to prove knowledge of `w` without revealing `w` or any information about it.**

**Slide Cross-reference:** 16, 17

---

#### **3.0 Interactive and Probabilistic Proofs**

To achieve zero-knowledge, the proof model is extended to be **interactive** and **probabilistic**.

*   **Interactive:** The Prover and Verifier engage in a multi-round conversation, rather than the Prover sending a single, static proof.
*   **Probabilistic:** The Verifier is randomized (uses random coin flips) and is allowed to make errors with a very small, negligible probability.

##### **3.1 Interactive Proof Systems**

In an interactive proof system, the Prover and Verifier exchange a series of messages.

*   **Completeness:** An honest Prover P can convince the Verifier V that a true statement `x ∈ L` is true (typically with probability 1).
*   **Computational Soundness:** A cheating Prover P* cannot convince the Verifier V to accept a false statement `x ∉ L`, except with a negligible probability. The probability is taken over the Verifier's random choices.

A common type is a **public-coin protocol**, where the Verifier's messages are simply the outcomes of its random coin flips, sent to the Prover as challenges.

**Definition [GMR85]:** An interactive proof system for a language `L` is a pair of algorithms (P, V), where V is a Probabilistic Polynomial-Time (PPT) algorithm, satisfying:
1.  **Completeness:** For all `x ∈ L`, `Pr[(P, V) accepts x] ≥ c(|x|)` (e.g., `c(|x|) = 1`).
2.  **Soundness:** For all `x ∉ L` and for any cheating prover P*, `Pr[(P*, V) accepts x] ≤ s(|x|)`.

The gap between completeness `c` and soundness `s` can be amplified by repeating the protocol multiple times. If there is a "completeness-soundness gap" (e.g., `c(|x|) ≥ 2/3` and `s(|x|) ≤ 1/3`), repeating the protocol `k` times reduces the soundness error to `(1/3)^k`, which quickly becomes negligible. The class of languages that have interactive proofs is denoted **IP**.

**Slide Cross-Reference:** 19, 20, 24, 25

##### **3.2 Example: Interactive Proof for Quadratic Residuosity**

Here is a zero-knowledge interactive proof for the statement `x ∈ QRN`. The Prover (P) knows a secret `w` such that `x ≡ w² mod N`.

1.  **P's Commitment:**
    *   P chooses a random number `r`.
    *   P computes a commitment `z = r² mod N`.
    *   P sends `z` to the Verifier (V).

2.  **V's Challenge:**
    *   V chooses a random bit `b ∈ {0, 1}`.
    *   V sends `b` to P as a challenge.

3.  **P's Response:**
    *   If `b = 0`, P sends `t = r mod N`.
    *   If `b = 1`, P sends `t = r * w mod N`.

4.  **V's Verification:**
    *   V checks if `t² ≡ z * x^b mod N`.
    *   If `b = 0`, the check is `t² ≡ z * x⁰ mod N`, which simplifies to `r² ≡ z mod N`. This is true by construction.
    *   If `b = 1`, the check is `t² ≡ z * x¹ mod N`, which simplifies to `(r * w)² ≡ (r²) * (w²) mod N`. This is also true since `z = r²` and `x = w²`.

**Analysis:**
*   **Completeness:** If the Prover knows `w`, they can correctly answer either challenge, so the Verifier will always accept.
*   **Soundness:** If the claim is false (i.e., `x` is not a quadratic residue), a cheating Prover cannot answer both challenges. The Prover can prepare for one challenge (e.g., choose `z = r²` to answer `b=0`), but they will be caught if the Verifier chooses the other challenge. The probability of fooling the Verifier in one round is exactly 1/2. By repeating the protocol 100 times, the probability of successfully cheating becomes `(1/2)^100`, which is negligible.
*   **Zero-Knowledge:** The Verifier learns nothing about `w`. In each round, the transcript consists of `(z, b, t)`.
    *   If `b=0`, the transcript is `(r², 0, r)`.
    *   If `b=1`, the transcript is `(z, 1, r*w)`.
    In either case, the Verifier just sees two numbers, one of which is the square of the other (modulo `N`). The Verifier could have generated such a pair on their own without interacting with the Prover. This intuition is formalized by the concept of a **simulator**.

**Slide Cross-Reference:** 21, 22, 23

---

#### **4.0 Formalizing Zero-Knowledge**

The intuitive notion of "leaking no information" is formalized by the **Simulation Paradigm**.

##### **4.1 The Verifier's View and the Simulator**

The **Verifier's view** of an interaction is everything it sees: its own random coin tosses and the transcript of messages exchanged with the Prover.
`View_V[P, V] = {Q1, A1, ..., Qn, An, coins_of_V}`

An interactive protocol is **zero-knowledge** if a probabilistic polynomial-time (PPT) algorithm, called a **Simulator (Sim)**, can generate a view that is "indistinguishable" from a real view, using only the public statement `x` and *without* access to the secret witness `w`.

If such a simulator exists, it implies that the view generated during a real interaction contains no information that the Verifier couldn't have generated for itself. The interaction is useless in terms of gaining knowledge, other than being convinced that `x ∈ L`.

**Slide Cross-reference:** 26, 27, 28

##### **4.2 Computational Indistinguishability**

Two probability distributions (e.g., the distribution of real views and the distribution of simulated views) are **computationally indistinguishable** if no efficient (PPT) algorithm, called a **Distinguisher**, can tell them apart with a probability significantly better than random guessing.

Formally, for any PPT distinguisher D, given a sample `s` from one of two distributions `D1` or `D2`:
`| Pr[D(s) = 1 | s ← D1] - Pr[D(s) = 1 | s ← D2] | < negl(λ)`
where `negl(λ)` is a negligibly small function in the security parameter `λ`.

**Slide Cross-reference:** 29

##### **4.3 Formal Definition of Zero-Knowledge**

An interactive protocol (P, V) for a language `L` is **zero-knowledge** if for every PPT Verifier V*, there exists a PPT simulator Sim such that for every true statement `x ∈ L`, the following two distributions are computationally indistinguishable:

1.  The real view: `view_V*[(P, V*)(x)]`
2.  The simulated view: `Sim(x)`

There are variations:
*   **Perfect ZK:** The real and simulated views are identically distributed.
*   **Statistical ZK:** The statistical distance between the distributions is negligible.
*   **Computational ZK:** The distributions are computationally indistinguishable (most common in practice).
*   **Honest-Verifier ZK (HVZK):** The ZK property holds only for the honest Verifier specified in the protocol, not for any arbitrary malicious V*. Many practical schemes start by proving HVZK and are then transformed to full ZK.

**Theorem [GMW86]:** If one-way functions exist (a standard cryptographic assumption), then every language in NP has a computational zero-knowledge interactive proof. This is a landmark result showing the broad applicability of ZKPs. The proof relies on constructing a ZK proof for an NP-complete problem (like graph 3-coloring) using bit commitments.

**Slide Cross-reference:** 30, 31, 32, 34

##### **4.4 Example: ZK Proof for Graph Colouring**

*   **Problem:** Prover wants to prove they know a valid 3-colouring for a graph G, without revealing the colouring.
1.  **Commitment:** The Prover has a valid 3-colouring. They randomly permute the colours (e.g., map red to blue, blue to green, etc.) and then "commit" to the colour of each node. A commitment is like putting a value in a locked box; it's **binding** (the value can't be changed) and **hiding** (the value is secret). The Prover sends all these locked boxes to the Verifier.
2.  **Challenge:** The Verifier chooses a single edge `(u, v)` from the graph at random and asks the Prover to "open" the commitments for the two nodes on that edge.
3.  **Response/Opening:** The Prover reveals the colours for nodes `u` and `v` and the information needed to verify the commitment.
4.  **Verification:** The Verifier checks that the two revealed colours are different and that they match the commitments.

This protocol is repeated many times with independent, random colour permutations.

*   **Completeness:** An honest Prover always succeeds.
*   **Soundness:** If the graph is not 3-colourable, any colouring the Prover commits to must have at least one edge with same-coloured nodes. The Verifier will find this edge with probability `1/|E|` (where |E| is the number of edges). Repeating the protocol `k*|E|` times makes the soundness error negligible.
*   **Zero-Knowledge:** In each round, the Verifier only sees the colours of two adjacent nodes, which they already knew must be different. The random permutation of colours ensures no information about the "true" colouring is leaked across rounds.

**Slide Cross-reference:** 33, 35

---

#### **5.0 From Interactive to Non-Interactive Proofs**

Interactive proofs require back-and-forth communication, which is impractical for many applications, especially on blockchains. The **Fiat-Shamir transform (or heuristic)** is a powerful technique to convert a public-coin interactive proof into a non-interactive one.

##### **5.1 The Fiat-Shamir Transform**

In a public-coin interactive proof, the Verifier's only role is to provide random challenges. The Fiat-Shamir transform replaces the Verifier with a cryptographic hash function (modeled as a **random oracle**).

*   **Interactive Protocol:**
    1.  Prover sends message `α₁`.
    2.  Verifier sends random challenge `β₁`.
    3.  Prover sends message `α₂`.
    4.  Verifier sends random challenge `β₂`.
    5.  ...

*   **Non-Interactive Protocol (using Fiat-Shamir):**
    1.  The Prover computes their first message `α₁`.
    2.  To get the Verifier's challenge `β₁`, the Prover hashes the public input `x` and their first message: `β₁ = H(x, α₁)`.
    3.  The Prover uses `β₁` to compute their next message `α₂`.
    4.  The next challenge is computed as `β₂ = H(x, α₁, α₂)`.
    5.  This continues until all messages are generated. The Prover then sends the entire transcript `(α₁, α₂, ...)` as a single proof `π`.
    6.  The Verifier can check the proof by re-computing the challenges `βᵢ` using the same hash function and verifying that the Prover's responses `αᵢ` are valid given those challenges.

The security of this transformation relies on the assumption that the hash function `H` behaves like a truly random function.

**Slide Cross-reference:** 36, 37, 38, 64

---

#### **6.0 ZK-SNARKs: Succinct Non-Interactive Arguments of Knowledge**

SNARKs represent the state-of-the-art in practical proof systems.

**ZK-SNARK** stands for **Zero-Knowledge Succinct Non-Interactive Argument of Knowledge**.

*   **Zero-Knowledge:** (Optional property) The proof `π` reveals nothing about the secret witness `w`.
*   **Succinct:** The proof `π` is very short (e.g., logarithmic in the size of the computation) and verification is very fast. `|π| = O(log|C|)` and verification time is `O(|x|, log|C|)`.
*   **Non-Interactive:** The proof is a single string, requiring no back-and-forth communication (often achieved via Fiat-Shamir).
*   **Argument (of Knowledge):** This is a proof with computational soundness (sound against a polynomially-bounded Prover) rather than statistical soundness (sound against an all-powerful Prover). The "of Knowledge" part means the proof demonstrates that the Prover actually *knows* a valid witness `w`, and there exists an "Extractor" algorithm that could recover `w` from a successful Prover.

**Slide Cross-reference:** 46, 50, 51

##### **6.1 The SNARK Pipeline**

Constructing a SNARK for a computational statement `C(x, w) = 0` (where `x` is the public input and `w` is the secret witness) typically follows a pipeline:

1.  **Arithmetization:** The computation `C` is converted into a formal mathematical representation, like an **Arithmetic Circuit** or a system of polynomial equations called a **Constraint System**. Common constraint systems include R1CS (Rank-1 Constraint System), PlonKish, and AIR (Algebraic Intermediate Representation). This step converts the problem from "does a witness exist for this code?" to "does a set of values exist that satisfy these polynomial equations?".

2.  **Information-Theoretic Compiler:** An **Interactive Oracle Proof (IOP)** or a **Polynomial IOP** is created for the constraint system. This is an information-theoretic protocol where the Prover sends oracles (representing polynomials) and the Verifier checks them by making queries at random points. This step is abstract and does not involve real cryptography yet.

3.  **Cryptographic Compiler:** The abstract IOP is made concrete using a **Polynomial Commitment Scheme (PCS)**. The Prover commits to the polynomials from the IOP, and the Verifier's queries are answered using the PCS. The PCS ensures the Prover cannot cheat (binding property) while hiding the polynomial (hiding property). The result is a concrete cryptographic proof `π`.

**Slide Cross-reference:** 56, 71

##### **6.2 Arithmetization Example**

Consider the computation `(x₁ + x₂)(x₂ + w₁)`. This can be represented as an arithmetic circuit with input wires for `x₁, x₂, w₁` and gates for addition and multiplication. This is then converted to a computation trace that must satisfy certain constraints.

*   **Inputs:** `x₁=5`, `x₂=6`, `w₁=1`
*   **Gate 0 (add):** `g₀ = x₁ + x₂ = 5 + 6 = 11`
*   **Gate 1 (add):** `g₁ = x₂ + w₁ = 6 + 1 = 7`
*   **Gate 2 (mul):** `g₂ = g₀ * g₁ = 11 * 7 = 77` (output)

This trace can be represented by vectors for the left inputs, right inputs, and outputs of each gate, which must satisfy constraints that enforce the circuit's logic.

**Slide Cross-reference:** 47, 48

##### **6.3 Preprocessing SNARKs and Trusted Setups**

Many efficient SNARKs are **preprocessing SNARKs**. In a setup phase, a **Common Reference String (CRS)** or public parameters `(pp, vp)` are generated based on the circuit `C`. The Prover uses `pp` to create a proof, and the Verifier uses `vp` to verify it.

`S(C) → (pp, vp)`
`P(pp, x, w) → π`
`V(vp, x, π) → Accept/Reject`

A critical aspect of the setup is its trust assumption:
*   **Trusted Setup per Circuit:** A secret `r` (toxic waste) is generated to create the CRS for a *specific* circuit `C`. `r` must be destroyed; if any party learns `r`, they can forge proofs. This is inflexible as a new ceremony is needed for every circuit. (e.g., Groth16)
*   **Universal and Updatable Trusted Setup:** The secret `r` is independent of any specific circuit. The same initial setup can be used for all circuits up to a certain size. It can also be updated by multiple parties in a way that as long as one party is honest and destroys their secret contribution, the final CRS is secure. (e.g., PLONK, Marlin, Sonic)
*   **Transparent Setup:** The setup phase requires no secrets at all; it is fully public and deterministic. These schemes often rely on different cryptographic assumptions (e.g., hash functions) and may have larger proof sizes or slower verification. (e.g., STARKs, Aurora)

**Slide Cross-reference:** 49, 52, 53, 54

##### **6.4 Polynomial Commitment Schemes (PCS)**

A PCS is a core building block for modern SNARKs. It allows a Prover to commit to a polynomial `f(X)` of degree at most `d`.

*   **Commit(f) → Com_f**: The Prover generates a short, binding commitment to the polynomial.
*   **Open(Com_f, z) → (y, π_z)**: The Prover can prove that `f(z) = y` for any point `z`.
*   **Verify(Com_f, z, y, π_z) → Accept/Reject**: The Verifier checks the opening proof `π_z`.

The security of a PCS relies on the **Schwartz-Zippel Lemma**, which states that two different polynomials of degree `d` can agree on at most `d` points. Therefore, if `f(r) = g(r)` for a random point `r` from a large field, then `f` and `g` are identical with overwhelmingly high probability. This allows the Verifier to check complex polynomial identities by just checking them at one random point.

**Slide Cross-reference:** 57, 58, 61, 62, 63, 65

---

#### **7.0 Schnorr Identification and Signature Schemes**

A classic application of ZKP principles is the **Schnorr Identification Scheme**, a three-move (challenge-response) protocol that allows a Prover to prove knowledge of a discrete logarithm. It is a **Sigma Protocol**, a common structure for ZK proofs.

Let `G` be a cyclic group of prime order `q` with generator `g`.
*   **Prover's Secret Key (sk):** `α ∈ ℤq`
*   **Prover's Public Key (vk):** `u = g^α`

**Goal:** Prover wants to prove to the Verifier that they know `α` corresponding to the public `u`.

1.  **Commitment (Prover):**
    *   Choose a random nonce `α_t ∈ ℤq`.
    *   Compute commitment `u_t = g^(α_t)`.
    *   Send `u_t` to the Verifier.

2.  **Challenge (Verifier):**
    *   Choose a random challenge `c ∈ ℤq`.
    *   Send `c` to the Prover.

3.  **Response (Prover):**
    *   Compute the response `α_z = α_t + α * c mod q`.
    *   Send `α_z` to the Verifier.

4.  **Verification (Verifier):**
    *   Check if `g^(α_z)` equals `u_t * u^c`.
    *   `g^(α_z) = g^(α_t + α*c) = g^(α_t) * (g^α)^c = u_t * u^c`.
    *   If the equation holds, the Verifier accepts.

This protocol is a proof of knowledge of the discrete logarithm `α`.

##### **7.1 From Identification to Signatures**

The Schnorr protocol can be converted into a digital signature scheme using the **Fiat-Shamir transform**. The Verifier's random challenge `c` is replaced by the hash of the message `m` and the Prover's commitment `u_t`.

*   **KeyGen:** `sk = α`, `vk = u = g^α`.
*   **Sign(m, sk):**
    1.  Choose random `α_t ∈ ℤq`, compute `u_t = g^(α_t)`.
    2.  Compute challenge `c = H(m, u_t)`.
    3.  Compute response `α_z = α_t + α * c mod q`.
    4.  The signature is `σ = (u_t, α_z)`.
*   **Verify(m, σ, vk):**
    1.  Parse signature `σ` as `(u_t, α_z)`.
    2.  Re-compute challenge `c = H(m, u_t)`.
    3.  Check if `g^(α_z) == u_t * u^c`.

**Slide Cross-reference:** 39, 41, 42, 43, 44, 45
