P.1. Medical history [program: MATERNITY PROGRAM, scope: TODAY]
C.1.1. Given a registered patient, capture their medical history
Q.1.1.1. Ever had asthma? [concept: Asthma]
O.1.1.1.1. Yes
O.1.1.1.2. No
O.1.1.1.3. Not sure
Q.1.1.1.3.1. Ever had problems breathing? [concept: Rapid breathing]
O.1.1.1.3.1.1. No
O.1.1.1.3.1.2. Yes
Q.1.1.1.3.1.2.1. Did you have to be admitted afterwards? [concept: Admitted] 
O.1.1.1.3.1.2.1.1. No
O.1.1.1.3.1.2.1.2. Yes
Q.1.1.1.3.1.2.1.2.1. For how long (in days) were you admitted? [field_type: number, tt_pageStyleclass: NumbersOnly, min: 2, max: 5, concept: Days]
Q.1.1.2. Ever had hypertension? [concept: Hypertension]
O.1.1.2.1. No
O.1.1.2.2. Yes
Q.1.1.3. Ever had STIs? [concept: STI]
O.1.1.3.1. Yes
Q.1.1.3.1.1. Specify [concept: Specify, multiple: multiple]
O.1.1.3.1.1.1. Syphilis
O.1.1.3.1.1.2. Gonorrhea
O.1.1.3.1.1.3. Chylamidia
O.1.1.3.1.1.4. Trichomoniasis
O.1.1.3.1.1.5. Unspecified urethritis
O.1.1.3.1.1.6. Bacterial vaginosis, non-specified
O.1.1.3.2. No
Q.1.1.4. Outcome
O.1.1.4.1. Admitted
O.1.1.4.2. Absconded
O.1.1.4.3. Delivered
O.1.1.4.4. Discharged
O.1.1.4.5. Patient died
