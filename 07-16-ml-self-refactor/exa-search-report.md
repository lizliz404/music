# Exa Search Report — ML Self Refactor

> Search date: 2026-07-16
> Scope: Academic and grey literature at the intersection of ML/RL concepts and psychological phenomena relevant to self-worth, learned helplessness, attachment, overfitting in education.

---

## Executive Summary

The search was surprisingly productive. There is a substantial body of **computational psychiatry** and **predictive processing** literature that formalizes exactly the psychological phenomena being reframed — using the same mathematical frameworks (RL, Bayesian inference, active inference) that the article's metaphor draws on. The core finding: this is not just a metaphor. Researchers are already building computational models where low self-esteem = aberrant prediction error weighting; learned helplessness = a Bayesian prior over controllability; anxious attachment = precision-weighted interoceptive prediction errors under unreliable caregiver feedback.

---

## 1. Self-Esteem as Reinforcement Learning (Prediction Error)

### Key Paper: Will et al. (2017) — *Neural and computational processes underlying dynamic changes in self-esteem*
- **eLife** | https://elifesciences.org/articles/28098
- Self-esteem fluctuations are driven by **social approval prediction errors (SPEs)** — the difference between expected and received social feedback.
- SPEs correlate with activity in **ventral striatum/subgenual ACC** (the brain's prediction error machinery).
- Self-esteem updates are reflected in **vmPFC** activity (the brain's value representation hub).
- A dimension of "interpersonal vulnerability" (low self-esteem + anxiety + depression) is characterized by **amplified SPE responses in anterior insula** and greater insula-vmPFC connectivity — i.e., self-worth is *more reactive* to social feedback in vulnerable individuals.

### Key Paper: Will et al. (2020) — *Neurocomputational mechanisms underpinning aberrant social learning in young adults with low self-esteem*
- **Translational Psychiatry** | https://www.nature.com/articles/s41398-020-0702-4
- Low self-esteem individuals show a **dissociation**: reduced tendency to use social feedback to learn about how others view them (reflected appraisal), BUT enhanced tendency to use the same feedback for subjective feelings of self-worth (direct appraisal).
- This is a **dual learning rate asymmetry** — the "learning about others" rate is suppressed while the "feeling about self" rate is amplified.

### Relevance to article:
- Directly validates the ML analogy: self-esteem IS a learned value estimate updated by prediction errors.
- The "low self-esteem paradox" (not learning from positive data while being hyper-reactive to negative) is formally modeled as **asymmetric learning rates**.
- "外部评价依赖" literally maps to: reward model outsourcing — the vmPFC value signal is driven entirely by external SPEs rather than an internally stabilized prior.

---

## 2. Learned Helplessness as Bayesian Prior over Controllability

### Key Paper: Huys & Dayan (2009) — *A Bayesian formulation of behavioral control*
- **Cognition** | http://www.gatsby.ucl.ac.uk/~dayan/papers/huysdayan09.pdf
- **THE canonical computational model of learned helplessness.**
- Formalizes "controllability" as characteristics of **prior distributions** over action-outcome transitions.
- Helplessness = a Bayesian prior that actions have high outcome entropy (i.e., actions don't matter).
- Two routes to pathology: (1) normative inference from genuinely uncontrollable experience, or (2) normal inference from a **pessimistic prior** (genetic/constitutional).
- This directly maps to your "前期标注员不是本人 / 基因彩票" argument.

### Key Paper: Lieder, Goodman, & Huys (2013) — *Learned helplessness as Bayesian generalization*
- https://web.stanford.edu/~ngoodman/papers/LiederGoodmanHuys2013.pdf
- Shows that a **three-level hierarchical Bayesian model** of action-outcome contingencies is sufficient to reproduce all key features of learned helplessness — escape deficits, impaired appetitive learning, generalization across contexts.
- Helplessness = a high-level prior belief that "situations in general are uncontrollable" (low c, low σ²c).

### Key Paper: Huys, Vogelstein, & Dayan (2008) — *Psychiatry: Insights into depression through normative decision-making models*
- **NeurIPS** | https://papers.nips.cc/paper_files/paper/2008
- Formalized helplessness as **prior over outcome entropy** and anhedonia as **effective reward size**.
- Used these parameters to **classify MDD patients vs. controls from behavior alone** — no questionnaires needed.

### Key Paper: Dorfman et al. — *The influence of exposure to early-life adversity on agency-modulated reinforcement learning*
- **Learning & Memory (2025)** | https://learnmem.cshlp.org/content/32/1/a054047
- Early-life adversity → decreased **agency beliefs** → reduced **learning rates**.
- Agency beliefs are formalized as a Bayesian parameter ψ that modulates how much an outcome is attributed to one's own action vs. external forces.

### Relevance to article:
- Learned helplessness is THE most computationally formalized psychological phenomenon. It literally IS a Bayesian prior problem.
- "习得性无助 = credit assignment failure → value function → 0" is not just an analogy — Huys & Dayan formalized exactly this in 2009.
- The "gene lottery" argument has a formal twin: Huys' "two routes" (normative inference from bad experience vs. pessimistic prior from genetics).

---

## 3. Attachment as Active Inference / Generative Model

### Key Paper: Cittern, Nolte, Friston, & Edalat (2018) — *Intrinsic and extrinsic motivators of attachment under active inference*
- **PLOS ONE** | https://pmc.ncbi.nlm.nih.gov/articles/PMC5886414/
- The first paper to formulate **infant attachment types in terms of active inference**.
- Shows how secure, avoidant, ambivalent, and disorganized attachment emerge from **free energy minimization** over interoceptive states (stress levels) when seeking proximity to caregivers with different response patterns.
- Disorganized attachment arises when caregiver's **exteroceptive cues are misleading** (high epistemic value of proximity seeking despite consistently increasing stress) — the infant can't form a coherent behavioral policy.

### Key Paper: Santaguida & Bergamasco (2023) — *Attachment Theory in an Active Inference Framework*
- https://doi.org/10.1007/978-3-031-28719-0_13
- Maps Bowlby's **Internal Working Model** onto **hierarchical generative models** in the active inference framework.
- Attachment styles = different precision-weighting strategies for interoceptive vs. exteroceptive prediction errors.

### Key Paper: Santaguida, Pagnoni, & Bergamasco (2026) — *The fetus/infant-mother as a co-evolving dyadic system*
- **Frontiers in Psychology** | https://doi.org/10.3389/fpsyg.2026.1836911
- Extends the active inference attachment model to the **gestational period**.
- Internal Working Models develop through reciprocal inferential exchanges across the Markov blankets of two asymmetrically coupled agents.

### Key Paper: Attachment as Prediction (2025) — *Insights from Cognitive and Developmental Neuroscience*
- **PMC** | https://pmc.ncbi.nlm.nih.gov/articles/PMC12333888/
- Attachment schemas = **predictive memory schemas** encoded in mPFC-cortico-subcortical circuitry.
- Formalizes the Bayesian update: P(CR|E) ∝ P(E|CR) × P(CR), where CR = caregiver response, E = current evidence.

### Key Paper: Lin (2025) — *Attachment: a predictive coding approach*
- https://doi.org/10.31234/osf.io/yqtr8
- Type A (avoidant) = **suppression of interoceptive prediction errors** (adaptive response to maltreatment — short-term stress relief at the cost of long-term interoceptive awareness).
- Type C (anxious/ambivalent) = **suppression of exteroceptive prediction errors** — obsessive seeking of information through increased vigilance.

### Relevance to article:
- Bowlby's "Internal Working Model" was always already a generative model — the computational literature just made it formal.
- Anxious attachment = intermittent reward schedule → high-variance, low-confidence policy — validated by the precision-weighting account.
- The "emotion as un-modeled loss term" argument from Block 2 has a direct formal twin in the interoceptive prediction error suppression model.

---

## 4. Overfitting in Education

### Blog: Gaurav Jain (2015) — *Overfitting in Education*
- http://gaurav1302.github.io/computer-science/2015/11/08/Overfitting-In-Education/
- Classic blog post explicitly using the ML overfitting analogy for exam-oriented education.
- Suggests regularization (simpler fundamental models) as the fix.

### Essay: *Dead Reading* (死读书) (2026)
- https://garden.theory-a.com/education/si-du-shu
- **Excellent essay** — overfitting as "a high-dimensional lookup table built without ever writing a compression algorithm."
- Key insight: "The loss function rewards exact textual replication and punishes novel synthesis → the agent will rationally allocate zero compute to building a generalized latent space."
- "Goodhart's law in the cognitive register: the moment recall becomes the metric, recall ceases to be a measure of understanding."
- "死读书 is the permanent resident of the overfit state, because the exam environment supplies no weight decay on storage."
- Links to the Bitter Lesson, grokking, and the class dynamics of credentialism.

### Menefee (2025) — *The Logic of Exclusion: High-Stakes Testing as Epistemic Infrastructure*
- https://doi.org/10.31235/osf.io/sb57h_v1
- Exams as "socio-technical infrastructures designed to exclude" — cognitive styles systematically filtered out.
- "The exam's narrow bandwidth of cognitive recognition" = a reward function that only recognizes one type of output.

### Dagogliano (2026) — *ZLT-P16: The Curricular Uniformity Trap*
- https://doi.org/10.5281/zenodo.19501526
- Formal model: SDI_edu (Structural Delusion Index for Education) — proxy/competence decoupling under forced exposure ratios.
- ρ(FER, SDI_edu) = 0.795 across 33 OECD countries. "The prison self-conceals."

### Schwartz, Chase, & Bransford (2012) — *Resisting Overzealous Transfer*
- https://aaalab.stanford.edu/assets/papers/2012/Resisting_Overzealous_Transfer.pdf
- "Overzealous transfer" (OZT) — when prior successful routines block new learning.
- Maps to negative transfer and the stability-plasticity dilemma.

### Relevance to article:
- The education → overfitting analogy has multiple existing treatments, from casual blogs to formal mathematical models.
- The "死读书" essay is particularly relevant — it makes the same Goodhart's law / lookup-table argument the article develops.

---

## 5. Goodhart's Law & Reward Misspecification

### Key Paper: *Dead rats, dopamine, performance metrics, and peacock tails: Proxy failure is an inherent risk in goal-oriented systems* (2023)
- **Behavioral and Brain Sciences** | https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/dead-rats-dopamine-performance-metrics-and-peacock-tails-proxy-failure-is-an-inherent-risk-in-goaloriented-systems/
- **Unifying framework for proxy failure across domains.** Identifies Goodhart's law, Campbell's law, the cobra effect as instances of the same mechanism.
- "Whenever incentivization or selection is based on an imperfect proxy measure of the underlying goal, a pressure arises that tends to make the proxy a worse approximation of the goal."

### Key Paper: Karwowski et al. (2023) — *Goodhart's Law in Reinforcement Learning*
- https://arxiv.org/html/2310.09144
- Formal proof that optimizing an imperfect proxy reward beyond a critical point decreases true objective performance.
- Proposes optimal early stopping methods that provably avoid Goodharting.

### Key Paper: El-Mhamdi & Lê-Nguyên (2024) — *On Goodhart's law, with an application to value alignment*
- https://arxiv.org/html/2410.09638
- Distinguishes **weak Goodhart** (over-optimizing the metric is useless) vs. **strong Goodhart** (over-optimizing the metric is harmful).
- Strong Goodhart emerges when the discrepancy between proxy and goal has **heavy-tailed distributions** — relevant to "conditional approval" as reward misspecification.

### LessWrong: *Forcing Yourself is Self Harm, or Don't Goodhart Yourself*
- https://www.greaterwrong.com/posts/Ym7JR4TgXTyawZTgH/forcing-yourself-is-self-harm-or-don-t-goodhart-yourself
- Explicitly applies Goodhart's law to **self-improvement**: "by trying to force yourself to be a particular way you harm yourself by engaging mental behaviors that will make you less aware of yourself."

### Contingent Self-Worth Literature:
- **Crocker & Wolfe (2001)** — Psychological Review: Foundational theory of CSW. "Self-esteem depends on perceived successes or failures in domains of contingency."
- **Crocker & Park (2004)** — Psychological Bulletin: "The Costly Pursuit of Self-Esteem." CSW undermines learning, autonomy, self-regulation, relationships, and health.
- The entire CSW literature is, in effect, a psychological description of **reward misspecification**: self-esteem becomes the proxy optimized, while well-being/learning/growth are the true objectives that suffer.

### Relevance to article:
- "Contingent self-worth = reward misspecification / Goodhart's law" is validated by both the CSW literature (psychology side) and the formal Goodhart literature (ML/economics side).
- The proxy failure framework paper explicitly unifies these across domains.

---

## 6. Computational Psychiatry (Broad Framework)

### Friston (2023) — *Computational psychiatry: from synapses to sentience*
- **Molecular Psychiatry** | https://www.nature.com/articles/s41380-022-01743-z
- The canonical overview: psychopathology = **false inference** under aberrant precision-weighting.
- "Any symptom of psychopathology must, at some level, entail aberrant belief updating."
- Prediction errors are encoded by superficial pyramidal cells; precision-weighting by neuromodulators (dopamine, serotonin, acetylcholine).

### Badcock & Davey (2024) — *Active Inference in Psychology and Psychiatry: Progress to Date?*
- **Entropy** | https://doi.org/10.3390/e26100833
- Honest assessment: active inference has strong theoretical promise but "has achieved very little" in practical clinical applications so far.
- The framework unifies evolutionary, developmental, and clinical psychology under one mathematical formalism.

### Kao & Rutledge (2023) — *Computational models of subjective feelings in psychiatry*
- https://rutledge-lab.squarespace.com/s/KaoRutledgeNBR2023.pdf
- Reviews how **momentary happiness** depends on reward prediction errors, not absolute reward levels.
- "Happiness reflects not how well people are doing, but whether they are doing better than expected."
- Low self-esteem = intact prediction error computation but **altered baseline expectations** and **amplified reactivity**.

### Relevance to article:
- The entire computational psychiatry field is built on the premise that psychological phenomena ARE model training/updating problems.
- This provides academic credibility to the article's central move.

---

## 7. Self-Modeling as Regularization

### Key Paper: *Unexpected Benefits of Self-Modeling in Neural Systems* (2024)
- https://arxiv.org/html/2407.10188v2
- When neural networks learn to predict their own internal states as an auxiliary task, they **self-regularize**: narrower weight distributions, lower RLCT (a measure of complexity).
- "Learning to self-model is learning to make oneself modelable."
- This suggests a computational basis for why **meta-cognition / self-awareness** might have adaptive value beyond introspection.

### Relevance to article:
- The "元学习 / meta-cognition as the real asset upgrade" argument from Block 3 and Block 5 has a computational twin: self-modeling reduces complexity and increases parameter efficiency.
- This is arguably the most novel finding from this search — it directly supports the "architecture search权限在你手上" framing.

---

## 8. Other Notable Finds

### Forgetting Survey (2024) — *"Forgetting" in Machine Learning and Beyond*
- https://arxiv.org/html/2405.20620v1
- Comprehensive survey linking forgetting in ML, psychology, and education.
- "Overfitting arises when we simply memorise specific examples rather than generalise patterns from them" — applies to both humans and machines.
- Forgetting as necessary for generalization — connects to the "catastrophic forgetting" argument in Block 2.

### Agency Circuit (2026) — *A Neuro-Symbolic Solution for Mitigating Policy Collapse in RL*
- https://doi.org/10.65109/trfj2704
- Builds an RL agent that avoids learned helplessness by implementing a "Control Exertion Module" that triggers micro-actions to restore agency when helplessness metrics cross a threshold.
- Inspired by the mPFC-DRN neural circuit that governs resilience to uncontrollable stress in mammals.

---

## Gap Analysis

**What we DID NOT find:**
- No paper that explicitly frames ALL the listed psychological constructs (unworthiness, impostor syndrome, scarcity mindset, etc.) as a unified "training misconfiguration" framework.
- No clinical intervention protocol that uses ML training concepts as therapeutic metaphors (though the Goodhart's Law self-help blog post comes closest).
- The "ML as therapeutic reframe" is novel as a **synthesis** — the individual pieces exist in the computational literature, but no one has bundled them into a coherent reframe for non-academics.

**What this means for the article:**
The article's value-add is precisely the **synthesis and translation** — taking the scattered computational psychiatry findings and packaging them into an actionable, engineer-friendly framework. This is genuinely original at the level of presentation and accessibility, even though the individual formal models exist.

---

## Top 10 Most Relevant Sources (ranked)

1. **Will et al. (2017)** — Self-esteem as social prediction error (eLife)
2. **Huys & Dayan (2009)** — Bayesian formulation of learned helplessness (Cognition)
3. **Cittern, Nolte, Friston, & Edalat (2018)** — Attachment under active inference (PLOS ONE)
4. **Lieder, Goodman, & Huys (2013)** — Hierarchical Bayesian model of helplessness
5. **Dead Reading (死读书)** — Overfitting in education essay (theory-a.com)
6. **Will et al. (2020)** — Low self-esteem and aberrant social learning (Translational Psychiatry)
7. **Crocker & Park (2004)** — The Costly Pursuit of Self-Esteem (Psychological Bulletin)
8. **Dorfman et al. (2025)** — Early-life adversity and agency-modulated RL (Learning & Memory)
9. **Self-Modeling in Neural Systems (2024)** — Self-modeling as regularization (arXiv)
10. **Dead rats, dopamine, and proxy failure (2023)** — Unifying framework for Goodhart's law (BBS)
