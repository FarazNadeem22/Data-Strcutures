## **Week 1: Probability Theory & Distributions**

### **📌 Part 1: Probability Review**
Probability is the **foundation of quantitative finance**. A quick refresher:

#### **Basic Probability Rules**
- **Union Rule**: 
  \[ P(A \cup B) = P(A) + P(B) - P(A \cap B) \]
- **Conditional Probability**: 
  \[ P(A | B) = \frac{P(A \cap B)}{P(B)} \]
- **Independence**: 
  \[ P(A \cap B) = P(A)P(B) \]

#### **Expectation & Variance**
- **Expected Value**:
  - Discrete: \[ E[X] = \sum x P(x) \]
  - Continuous: \[ E[X] = \int x f(x) dx \]
- **Variance**:
  \[ Var(X) = E[X^2] - (E[X])^2 \]
- **Standard Deviation**:
  \[ \sigma_X = \sqrt{Var(X)} \]

### **📌 Application in Finance**
- **Expected Return**: 
  \[ E[R] = \sum p_i R_i \]
- **Portfolio Variance**: 
  \[ Var(R_p) = w_1^2 Var(R_1) + w_2^2 Var(R_2) + 2w_1w_2 Cov(R_1, R_2) \]

### **Applied Exercise: Expected Value & Variance of Stock Returns**
#### **Problem Statement**
You are given a set of daily stock returns for a company. Compute:
1. **Expected Return**: The average return of the stock.
2. **Variance & Standard Deviation**: Measure of risk.

#### **Stock Return Data (Example)**
| Day | Return (%) |
|----|-----------|
| 1  |  0.5      |
| 2  | -0.2      |
| 3  |  1.0      |
| 4  | -0.5      |
| 5  |  0.8      |

#### **Tasks**
1. Compute the **expected return** using:
   \[ E[R] = \frac{1}{N} \sum R_i \]
2. Compute the **variance**:
   \[ Var(R) = \frac{1}{N} \sum (R_i - E[R])^2 \]
3. Compute the **standard deviation**:
   \[ \sigma_R = \sqrt{Var(R)} \]