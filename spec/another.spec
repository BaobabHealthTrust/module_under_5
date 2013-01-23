P.1. Surgical history [program: MATERNITY PROGRAM, scope: TODAY, parent: 1, pos: 1]
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

Q.1.1.1.3.1.2.1.2.1. For how long (in days) were you admitted? [pos: 3, field_type: number]

Q.1.1.2. Ever had hypertension? [pos: 4] 
O.1.1.2.1. No
O.1.1.2.2. Yes

Q.1.1.3. Outcome [pos: 5] 
O.1.1.3.1. Admitted
O.1.1.3.2. Absconded
O.1.1.3.3. Delivered
O.1.1.3.4. Discharged
O.1.1.3.5. Patient died

