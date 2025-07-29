### **1.0 Introduction to Cloud Security**

#### **1.1 The Cloud Computing Paradigm**

Cloud computing offers a model where computational and storage resources are rented from a third-party provider rather than purchased and maintained on-premise. This model, colloquially summarised as "Why buy when we can rent?", provides services at various levels, including Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). However, because a user's data and computations are no longer under their direct physical control, significant security and privacy challenges arise.

#### **1.2 Security and Privacy Challenges in the Cloud**

The delegation of data storage and computation to a third-party Cloud Service Provider (CSP) introduces several critical security concerns.

*   **Key Security Requirements:**
    1.  A user's data must be protected from unauthorised access by other users or external adversaries.
    2.  The CSP should be oblivious to the content of the data it stores. This implies the need for encryption or anonymisation to protect data even in the event of a breach.
    3.  The CSP should be oblivious to the nature of the computations it performs on user data.
    4.  The CSP must be held accountable for its services, particularly for data loss or corruption, as stipulated in the Service Level Agreement (SLA).

*   **The CSP as an Adversary:** The CSP itself can be a potential adversary. It could:
    *   Read or modify user data without authorisation.
    *   Sell user data to third parties.
    *   Fail to provide the contractually agreed-upon levels of redundancy, storage, or computational resources specified in the SLA.

*   **Privacy Issues:**
    *   The CSP should not be able to track a user's metadata, such as their physical location or the devices used to access the cloud services.
    *   There are significant legal and jurisdictional challenges. Data may be stored in servers across different countries, each with its own privacy laws (e.g., GDPR in the EU). Ensuring data remains within a specific jurisdiction (e.g., Australia) is a compliance requirement that is difficult for a user to independently verify.

#### **1.3 A Multi-Faceted Approach to Cloud Security**

Cloud security is a broad field encompassing several domains:

1.  **Cryptographic Security:** This involves authenticating users, ensuring data confidentiality and integrity, managing access control, and auditing data.
2.  **Network Security:** This focuses on securing all communication channels between the user and the cloud.
3.  **Operating System Security:** This addresses challenges related to virtualization and securing the underlying OS of the cloud infrastructure.

This lecture focuses on the cryptographic techniques employed to address these challenges.

*   **Slide Cross-reference:** Slides 4-9.

### **2.0 Cryptographic Techniques for Cloud Computing**

A suite of cryptographic tools has been developed to address the security and privacy issues inherent in cloud computing.

*   **Data Auditing:** Mechanisms to verify that the CSP is storing the user's data correctly and without tampering (i.e., verifying data integrity).
*   **Fine-Grained Access Control:** Systems that grant authorised users access to specific data while denying access to unauthorised parties. Attribute-Based Encryption (ABE) is a key technique in this area.
*   **Homomorphic Encryption:** Allows the cloud to perform computations on encrypted data without decrypting it first, thus preserving the privacy of the data being processed.
*   **Searchable Encryption:** Enables a user to query an encrypted database, where the cloud can retrieve the relevant encrypted results without learning the content of the query itself.
*   **Secure Multi-Party Computation (MPC):** Facilitates joint computation on data distributed across multiple servers without any single server learning the private inputs of the others.

*   **Slide Cross-reference:** Slide 10.

### **3.0 Data Auditing and Proofs of Storage**

Data auditing schemes, also known as Proofs of Storage, are protocols designed to allow a data owner or a designated third-party auditor to efficiently verify that a CSP is faithfully storing the owner's data.

#### **3.1 Naive Auditing Approaches and Their Limitations**

1.  **Full Download and Hash:** The owner could download the entire file from the cloud, re-compute its cryptographic hash, and compare it with a locally stored hash.
    *   **Caveat:** This is prohibitively expensive in terms of communication bandwidth and computation, especially for large datasets (e.g., petabytes), defeating the purpose of outsourcing storage.

2.  **Random Sampling of Blocks:** The owner can break the file into `n` blocks, `m₁, m₂, ..., mₙ`, store them on the cloud, and locally keep a copy of a subset of these blocks. To audit, the owner requests a randomly chosen block and compares it with their local copy.
    *   **Caveat:** This still requires significant local storage for the sampled blocks and high communication costs to download them. Furthermore, it provides only a probabilistic guarantee; corruption in an unchallenged block will go undetected.

*   **Slide Cross-reference:** Slide 12.

#### **3.2 Formalisms: PDP and PoR**

Two primary formalisms for proofs of storage have been established in the literature.

1.  **Provable Data Possession (PDP):** A scheme where the CSP (Prover) can prove to the data owner (Verifier) that it possesses the original data file without the verifier having to retrieve the file itself.
    *   **Citation:** Ateniese, G., Burns, R., Curtmola, R., Herring, J., Kissner, L., Peterson, Z., & Song, D. (2007). *Provable data possession at untrusted stores*. CCS '07.

2.  **Proofs of Retrievability (PoR):** A scheme that not only proves data possession but also guarantees that the owner can recover the entire file. If some data is corrupted, the scheme allows for its reconstruction.
    *   **Caveat:** This is typically achieved by first encoding the file with an **erasure code** before uploading it. An erasure code adds redundancy, allowing the original file to be reconstructed from a sufficient subset of the encoded blocks, even if others are lost.
    *   **Example:** Reed-Solomon codes are a type of Maximum Distance Separable (MDS) code, which is a highly efficient erasure code. An `(n, k)` MDS code can reconstruct the original `k` blocks from any `k` of the `n` encoded blocks.
    *   **Citation:** Juels, A., & Kaliski, B. S. (2007). *Pors: proofs of retrievability for large files*. CCS '07.

*   **Slide Cross-reference:** Slides 13, 15, 16.

#### **3.3 Towards Efficient Auditing: Homomorphic Authenticators**

A more advanced approach involves attaching an unforgeable tag (authenticator) `σᵢ` to each data block `mᵢ`. To audit, the owner challenges the server for a set of random blocks, and the server returns the corresponding `(mᵢ, σᵢ)` pairs for verification.

*   **Private vs. Public Verifiability:**
    *   **Private:** If the authenticator `σᵢ` is a Message Authentication Code (MAC), only the owner (who holds the secret MAC key) can perform the audit.
    *   **Public:** If `σᵢ` is a digital signature, anyone with the public verification key can act as an auditor. This allows the data owner to delegate the auditing task to a Third-Party Auditor (TPA).

*   **The Aggregation Problem:** The primary limitation of this tag-based approach is that the proof size and communication cost are proportional to the number of challenged blocks. To overcome this, the goal is to **aggregate** the responses for multiple blocks into a single, compact proof. This requires a special type of authenticator.

*   **Homomorphic Linear Authenticators (HLA):** An HLA is a construction where authenticators can be combined in a way that corresponds to a linear combination of the underlying data blocks. The key idea is that given authenticators `σ₁` and `σ₂` for messages `m₁` and `m₂`, one can compute a single authenticator `σ` for a combined message `μ`.

*   **Slide Cross-reference:** Slides 14, 17, 18, 19, 23.

#### **3.4 Constructing an Auditing Scheme with BLS Signatures**

A powerful tool for building publically verifiable HLAs is the Boneh-Lynn-Shacham (BLS) signature scheme, which is based on bilinear pairings.

*   **Key Concept: Bilinear Pairings**
    *   **Definition:** Given two cyclic groups, `G` and `G_T`, of the same prime order `p`, a bilinear pairing (or map) is an efficient function `e: G × G → G_T` with the following properties:
        1.  **Bilinearity:** For any `g ∈ G` and `a, b ∈ Z_p`, `e(gᵃ, gᵇ) = e(g, g)ᵃᵇ`.
        2.  **Non-degeneracy:** There exists `g ∈ G` such that `e(g, g) ≠ 1` (where `1` is the identity element in `G_T`).
    *   **Significance:** The bilinear property allows for moving exponents "out" of the pairing function, enabling multiplicative operations in the exponent to be checked with additions and pairings.

*   **Key Concept: Boneh-Lynn-Shacham (BLS) Signatures**
    *   **Setup:** Choose groups `G`, `G_T` and a pairing `e`. Select a generator `g ∈ G`. Define a hash function `H: {0,1}* → G` that maps arbitrary messages to points in the group `G`.
    *   **Key Generation:** The signer's private key is a random exponent `sk = x ∈ Z_p`. The corresponding public key is `pk = gˣ`.
    *   **Signing:** To sign a message `M`, the signer computes `σ = H(M)ˣ`.
    *   **Verification:** A verifier checks if the equation `e(σ, g) = e(H(M), pk)` holds.
    *   **Correctness:** The verification works because `e(σ, g) = e(H(M)ˣ, g) = e(H(M), g)ˣ = e(H(M), gˣ) = e(H(M), pk)`.
    *   **Properties:** BLS signatures are very short (a single group element) and are highly aggregatable.

*   **Application to Data Auditing (Shacham-Waters Scheme):**
    The BLS signature scheme can be used to construct a publically verifiable HLA for data auditing. The owner pre-computes a BLS-like signature `σᵢ` for each block `mᵢ`.
    *   When the auditor issues a challenge for a set of blocks `Q = {(i, νᵢ)}` (where `i` is the block index and `νᵢ` is a small random coefficient), the server computes an aggregated proof:
        *   An aggregated data block: `μ = Σ νᵢmᵢ`
        *   An aggregated signature: `σ = Π (σᵢ)ᵛᵢ`
    *   The server sends the single pair `(μ, σ)` to the auditor. Using the bilinear property of the underlying pairing, the auditor can verify this aggregated proof with a single, constant-size equation, regardless of how many blocks were challenged. This makes the proof size `O(1)` and dramatically reduces communication and verification costs.

*   **Slide Cross-reference:** Slides 20, 21, 22, 24.
*   **Citation:** Shacham, H., & Waters, B. (2013). *Compact proofs of retrievability*. Journal of Cryptology.

#### **3.5 Dynamic Auditing and Data Freshness**

The schemes described so far are for static data. In a dynamic setting, where data blocks can be added, modified, or deleted, the auditing scheme must also provide a **guarantee of freshness**. This ensures that the CSP is not passing audits using stale data.

*   **Challenge:** If a file is updated, the server must not only update the data block but also its corresponding tag. To prevent the server from passing an audit using an old version of the file, the audit protocol must check the timeliness of the data.
*   **Solution:** This typically involves using an authenticated data structure, such as a Merkle Tree or a Skip List, to maintain the set of all tags. When a block is modified, its tag is updated, and this change is reflected in the authenticated data structure. The audit proof must then include a proof of inclusion/freshness derived from this data structure.

*   **Slide Cross-reference:** Slides 25, 26, 27.

### **4.0 Fine-Grained Access Control**

Access control determines which users are permitted to access which data. Traditional models like Access Control Lists (ACLs) or Role-Based Access Control (RBAC) are often too coarse for cloud environments with many users and complex policies.

#### **4.1 Attribute-Based Encryption (ABE)**

ABE is an advanced form of public-key cryptography that provides highly flexible, fine-grained access control.

*   **Core Idea:** In ABE, a user's secret key and a ciphertext are associated with sets of attributes. Decryption is successful only if the attributes in the user's key satisfy an access policy specified in the ciphertext.
*   **Example Scenario (Medical Records):** A patient's medical record is encrypted with an access policy like `("Doctor" AND "Cardiology Department") OR "Patient"`.
    *   A doctor in the cardiology department would have a key with attributes `{"Doctor", "Cardiology Department", "Hospital A"}` and would be able to decrypt.
    *   A researcher with attributes `{"Researcher", "University X"}` would not be able to decrypt.
    *   The patient themselves would have a key with the attribute `{"Patient"}` and could also decrypt.

This allows data to be encrypted once under a policy, and any user whose attributes satisfy that policy can access it, without the data owner needing to re-encrypt the data for each new user.

*   **Slide Cross-reference:** Slides 28-36.

#### **4.2 Building ABE from Secret Sharing**

The concept of ABE is closely related to secret sharing.

*   **Key Concept: Shamir's Secret Sharing**
    A `(t, n)` threshold secret sharing scheme allows a dealer to split a secret `s` into `n` shares, such that any `t` or more shares can be combined to reconstruct `s`, but any `t-1` or fewer shares reveal no information about `s`.
    *   **Mechanism:** The dealer chooses a random polynomial `P(x)` of degree `t-1` such that the constant term is the secret, `P(0) = s`.
        `P(x) = s + c₁x + c₂x² + ... + c_{t-1}x^{t-1}`
    *   The `i`-th share is the point `(i, P(i))`.
    *   With `t` points, the polynomial `P(x)` can be uniquely reconstructed using Lagrange Interpolation, and the secret `s` can be found by evaluating `P(0)`.

*   **ABE Construction (Conceptual):**
    One can build a simple `t`-out-of-`n` threshold ABE scheme using this idea. A central authority generates keys for users based on their attributes. To encrypt a message `M`, one would use a master secret `s` to blind it (e.g., `C = M * Y^s`, where `Y` is a public parameter). The secret `s` is then shared using a polynomial `P(x)` where `P(0) = s`. Each attribute `i` is associated with a share `P(i)`. A user with `t` attributes can collect `t` shares, reconstruct `P(x)`, find `s = P(0)`, and decrypt the message.
    *   **Caveat:** Simple versions of this approach are insecure against collusion. More sophisticated schemes, like the Sahai-Waters scheme, use techniques like bilinear pairings and individualised polynomials for each user to prevent collusion attacks.

*   **Slide Cross-reference:** Slides 37-41.

