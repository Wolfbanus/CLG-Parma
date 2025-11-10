# Sistema di voto ponderato CLG

## 1. Categorie di votanti
I votanti sono suddivisi in tre categorie:
- **Associazioni** ($A$)
- **Gruppi informali** ($G$)
- **Persone singole** ($S$)

## 2. Pesi di voto $(p)$
Ad ogni categoria è attribuito un peso:
- Associazione: peso $p_A = 10$
- Gruppo informale: peso $p_G = 7$
- Singolo: peso $p_S = 1$

## 3. Calcolo del potere di voto $(P)$
Il potere di voto totale per ciascuna categoria è:
$$
P_A = N_A \cdot p_A
$$
$$
P_G = N_G \cdot p_G
$$
$$
P_S = N_S \cdot p_S
$$
dove $N_A$, $N_G$, $N_S$ sono il numero di associazioni, gruppi e singoli.

## 4. Regola di equilibrio (limite $50/50$)
Il potere di voto dei singoli non può superare quello dei collettivi (associazioni + gruppi):
$$
P_{collettivi} = P_A + P_G
$$

Se $P_S > P_{collettivi}$, allora il potere dei singoli viene ridotto per mezzo di un fattore correttivo $(f)$:
$$
f = \frac{P_{collettivi}}{P_S}
$$

$$
p_S^{eff} = p_S \cdot f
$$

Altrimenti (rimane come prima):

$$
p_S^{eff} = p_S
$$

Quindi:

$$
P_{singoli}^{eff} = N_S \cdot p_S^{eff}
$$

$$

$$


## 5. Voto "uno vale uno" (caso speciale)
Se è presente una sola categoria di soci, ogni membro ha peso 1:
$$
p = 1
$$

## 6. Approvazione
La proposta si considera approvata se la somma dei voti favorevoli supera il 50% del potere di voto totale:
$$
\text{Approvata se} \quad \frac{V_{favorevoli}}{P_{totale}} > 0.5
$$
dove:
$$
V_{favorevoli} = V_A \cdot p_A + V_G \cdot p_G + V_S \cdot p_S^{eff}
$$
$$
P_{totale} = P_A + P_G + P_{singoli}^{eff}
$$

---

**Nota:** Le formule sono scritte in sintassi $\LaTeX$ per chiarezza e precisione.