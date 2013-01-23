P.1. Another Patient medical history [program: ANC PROGRAM, scope: EXISTS, label: Medical History 2, pos: 0, parent: 1]
C.1.1. Given a registered patient, capture their medical history
Q.1.1.1. Ever had asthma? [pos: 0] 
O.1.1.1.1. Yes
O.1.1.1.2. No
O.1.1.1.3. Not sure

Q.1.1.1.3.1. Ever had problems breathing? [pos: 1] 
O.1.1.1.3.1.1. No
O.1.1.1.3.1.2. Yes

Q.1.1.1.3.1.2.1. Did you have to be admitted afterwards? [pos: 2]  
O.1.1.1.3.1.2.1.1. No
O.1.1.1.3.1.2.1.2. Yes

Q.1.1.1.3.1.2.1.2.1. For how long (in days) were you admitted? [field_type: number, pos: 3]

Q.1.1.2. Ever had hypertension? [pos: 4] 
O.1.1.2.1. No
O.1.1.2.2. Yes

