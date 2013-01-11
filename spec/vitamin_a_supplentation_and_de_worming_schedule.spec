P.1. VITAMIN A SUPPLEMENTATION AND DE-WORMING SCHEDULE [program: UNDER 5 PROGRAM, label: Supplementation]
C.1. Give VITAMIN A every 6 months from 6 months of age until 5 years
Q.1.1. Vitamin A 100,000 IU given? [condition: <%= @patient.age_in_months(session["datetime"] || Date.today).to_i < 12 && @patient.age_in_months(session["datetime"] || Date.today).to_i > 6 && @patient.age_in_months(session["datetime"] || Date.today).to_i < 60 %>]
O.1.1.1. Yes
O.1.1.2. No
Q.1.2. Vitamin A 200,000 IU given? [condition: <%= @patient.age_in_months(session["datetime"] || Date.today).to_i >= 12 && @patient.age_in_months(session["datetime"] || Date.today).to_i > 6 && @patient.age_in_months(session["datetime"] || Date.today).to_i < 60 %>]
O.1.2.1. Yes
O.1.2.2. No

C.1.2. Give de-worming tablets every 6 months from 12 months of age.
Q.1.2.1. Select drug [disabled: disabled]
O.1.2.1.1. Albendazole
O.1.2.1.2. Mebendazole

C.1.2.1.1.1. If Albendazole is to be given:
Q.1.2.1.1.1.1. Has half a tablet Albendazole been given?  [condition: <%= (@patient.age_in_months(session["datetime"] || Date.today).to_i >= 12 && @patient.age_in_months(session["datetime"] || Date.today).to_i <= 23) %>]

Q.1.2.1.1.1.2. Has 1 tablet Albendazole been given? [condition: <%= @patient.age_in_months(session["datetime"] || Date.today).to_i >= 24 && @patient.age_in_months(session["datetime"] || Date.today).to_i <= 59 %>]

Q.1.2.1.2.1. Has 1 tablet Mebendazole been given? [condition: <%= @patient.age_in_months(session["datetime"] || Date.today).to_i >= 12 && @patient.age_in_months(session["datetime"] || Date.today).to_i <= 59 %>]

Q.1.3.1. Visit date [field_type: date]

Q.1.4.1. Have long-lasting insecticidal nets for malaria been given?
O.1.4.1.1. No
O.1.4.1.2. Yes

Q.1.4.1.2.1. Date nets received [field_type: date]
