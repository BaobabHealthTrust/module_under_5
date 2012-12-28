P.1. Another Patient medical history [program: ANC PROGRAM, scope: EXISTS, label: Medical History 2]
C.1.1. Given a registered patient, capture their medical history
Q.1.1.1. Ever had asthma?
O.1.1.1.1. Yes
O.1.1.1.2. No
O.1.1.1.3. Not sure
Q.1.1.1.3.1. Ever had problems breathing?
O.1.1.1.3.1.1. No
O.1.1.1.3.1.2. Yes
Q.1.1.1.3.1.2.1. Did you have to be admitted afterwards? 
O.1.1.1.3.1.2.1.1. No
O.1.1.1.3.1.2.1.2. Yes
Q.1.1.1.3.1.2.1.2.1. For how long (in days) were you admitted? [field_type: number]
Q.1.1.2. Ever had hypertension?
O.1.1.2.1. No
O.1.1.2.2. Yes

P.2. Surgical history [program: MATERNITY PROGRAM, scope: TODAY]
C.2.1. Given a registered patient, capture their medical history
Q.2.1.1. Ever had asthma?
O.2.1.1.1. Yes
O.2.1.1.2. No
O.2.1.1.3. Not sure
Q.2.1.1.3.1. Ever had problems breathing?
O.2.1.1.3.1.1. No
O.2.1.1.3.1.2. Yes
Q.2.1.1.3.1.2.1. Did you have to be admitted afterwards? 
O.2.1.1.3.1.2.1.1. No
O.2.1.1.3.1.2.1.2. Yes
Q.2.1.1.3.1.2.1.2.1. For how long (in days) were you admitted? [field_type: number]
Q.2.1.2. Ever had hypertension?
O.2.1.2.1. No
O.2.1.2.2. Yes
Q.2.1.3. Outcome
O.2.1.3.1. Admitted
O.2.1.3.2. Absconded
O.2.1.3.3. Delivered
O.2.1.3.4. Discharged
O.2.1.3.5. Patient died

